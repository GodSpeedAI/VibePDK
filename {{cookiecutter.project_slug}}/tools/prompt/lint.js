/* Prompt linter for .prompt.md files: checks title and basic frontmatter presence.
Implements: PRD-014; DEV-PRD-007 */
const fs = require('node:fs');

function lintPromptFile(file) {
    const text = fs.readFileSync(file, 'utf8');
    const findings = [];
    if (!/^#\s+.+/m.test(text)) findings.push('Missing H1 title (# ...)');
    if (!/^---[\s\S]*?---/m.test(text)) findings.push('Missing frontmatter (---)');
    return { ok: findings.length === 0, findings };
}

if (require.main === module) {
    const file = process.argv[2];
    if (!file) {
        console.error('Usage: lint.js <prompt-file>');
        process.exit(2);
    }
    const res = lintPromptFile(file);
    if (!res.ok) {
        console.error(`[prompt:lint] FAIL ${file}:\n - ${res.findings.join('\n - ')}`);
        process.exit(1);
    } else {
        console.log(`[prompt:lint] PASS ${file}`);
    }
}

module.exports = { lintPromptFile };
