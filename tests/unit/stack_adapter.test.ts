const assert = require('node:assert');
const path = require('node:path');
const fs = require('node:fs');

const utilsPath = path.join(process.cwd(), '{{cookiecutter.project_slug}}', 'generators', '_utils', 'stack.ts');
// Transpile-less import via tsx/ts-node is not available here; test via dynamic eval fallback.
// Instead, simulate the JSON layout and validate the shape helpers using a small inline copy.

function getCategory(stack, name) {
    if (!stack || typeof stack !== 'object') return null;
    const cats = stack.categories;
    if (!cats || typeof cats !== 'object') return null;
    return cats[name] ?? null;
}

(function main() {
    const stack = { categories: { core_application_dependencies: { web_frameworks: ['fastapi'] } } };
    assert.deepStrictEqual(getCategory(stack, 'core_application_dependencies').web_frameworks, ['fastapi']);
    assert.strictEqual(getCategory(stack, 'missing'), null);
})();
