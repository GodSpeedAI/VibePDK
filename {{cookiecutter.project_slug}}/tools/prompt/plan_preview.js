/* Plan preview: concatenates a prompt file for token estimation (simple).
Implements: PRD-014/017; DEV-PRD-007/010 */
const fs = require('node:fs');
const { estimateTokensByHeuristic, evaluateAgainstBudget } = require('./budgets');

function planPreview(file, mode = 'default') {
    const content = fs.readFileSync(file, 'utf8');
    const tokens = estimateTokensByHeuristic(content);
    const budget = evaluateAgainstBudget(tokens, mode);
    return { content, tokens, budget };
}

if (require.main === module) {
    const file = process.argv[2];
    const mode = process.argv[3] || 'default';
    if (!file) {
        console.error('Usage: plan_preview.js <prompt-file> [mode]');
        process.exit(2);
    }
    const res = planPreview(file, mode);
    console.log(`[prompt:plan] tokens=${res.tokens} budget=${res.budget.level}`);
    if (!res.budget.within) process.exit(1);
}

module.exports = { planPreview };
