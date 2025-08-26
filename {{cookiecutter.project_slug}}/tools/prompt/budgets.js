/* Token budget utilities (approximate via words/chars). Implements: PRD-017; DEV-PRD-010 */
function estimateTokensByHeuristic(text) {
    const words = (text.trim().match(/\S+/g) || []).length;
    // crude heuristic: ~0.75 tokens per word for English prose
    return Math.round(words * 0.75);
}

const DEFAULT_BUDGETS = {
    default: { warn: 2000, hard: 3000 },
};

function evaluateAgainstBudget(tokens, mode = 'default', budgets = DEFAULT_BUDGETS) {
    const cfg = budgets[mode] || budgets.default;
    if (!cfg) return { within: true, level: 'none' };
    if (tokens >= cfg.hard) return { within: false, level: 'hard' };
    if (tokens >= cfg.warn) return { within: true, level: 'warn' };
    return { within: true, level: 'ok' };
}

module.exports = { estimateTokensByHeuristic, evaluateAgainstBudget, DEFAULT_BUDGETS };
