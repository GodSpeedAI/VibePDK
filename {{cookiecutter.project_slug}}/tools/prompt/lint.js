/* Prompt/Mode/Instruction linter
 - Validates title and YAML frontmatter presence
 - Enforces taxonomy fields: kind, domain, task (phase optional)
 Implements: PRD-014/017; DEV-PRD-007/010
*/
const fs = require('node:fs');
const path = require('node:path');

function extractFrontmatter(text) {
  const m = text.match(/^---\n([\s\S]*?)\n---/m);
  if (!m) return { raw: null, fields: {} };
  const raw = m[1];
  const fields = {};
  // naive YAML: key: value on single line (ignore arrays/objects except simple scalars)
  for (const line of raw.split(/\r?\n/)) {
    const mm = line.match(/^([A-Za-z0-9_\-]+)\s*:\s*(.+)$/);
    if (!mm) continue;
    const key = mm[1].trim();
    let val = mm[2].trim();
    // strip quotes if present
    if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith('\'') && val.endsWith('\''))) {
      val = val.slice(1, -1);
    }
    fields[key] = val;
  }
  return { raw, fields };
}

function classify(file) {
  if (file.endsWith('.prompt.md')) return 'prompt';
  if (file.endsWith('.chatmode.md')) return 'chatmode';
  if (file.endsWith('.instructions.md')) return 'instructions';
  return 'unknown';
}

function lintPromptFile(file) {
  const text = fs.readFileSync(file, 'utf8');
  const findings = [];

  // Title present
  if (!/^#\s+.+/m.test(text)) findings.push('Missing H1 title (# ...)');

  const { fields, raw } = extractFrontmatter(text);
  if (!raw) findings.push('Missing frontmatter (---)');

  const kind = classify(file);
  // Required taxonomy keys per kind
  if (kind === 'prompt' || kind === 'chatmode' || kind === 'instructions') {
    if (!fields.kind) findings.push("Missing frontmatter field: kind");
    if (!fields.domain) findings.push("Missing frontmatter field: domain");
    if (kind !== 'instructions' && !fields.task) findings.push("Missing frontmatter field: task");
    // Optional but recommended
    if ((kind === 'prompt' || kind === 'chatmode') && !fields.budget) findings.push("Recommend adding frontmatter field: budget (S|M|L)");
    if (kind === 'instructions' && !fields.precedence) findings.push("Recommend adding frontmatter field: precedence");
  }

  return { ok: findings.length === 0, findings };
}

if (require.main === module) {
  const file = process.argv[2];
  if (!file) {
    console.error('Usage: lint.js <file>');
    process.exit(2);
  }
  const res = lintPromptFile(path.resolve(file));
  if (!res.ok) {
    console.error(`[prompt:lint] FAIL ${file}:\n - ${res.findings.join('\n - ')}`);
    process.exit(1);
  } else {
    // If only recommendations present, still PASS
    console.log(`[prompt:lint] PASS ${file}${res.findings.length ? ' (notes)\n - ' + res.findings.join('\n - ') : ''}`);
  }
}

module.exports = { lintPromptFile, extractFrontmatter };
