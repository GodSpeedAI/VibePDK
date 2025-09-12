// Unit tests for Just recipes functionality
// Implements TDD approach for spec-kit integration Cycle 5
import { execSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import assert from 'node:assert';

// Test directory for temporary files
const testDir = join(__dirname, '../../test-temp');
const docsSpecsDir = join(testDir, 'docs', 'specs');
const templatesDir = join(testDir, '.github', 'prompts');

// Path to the spec_scaffold.sh script
const scriptPath = join(__dirname, '../../scripts/spec_scaffold.sh');

// Create test directory structure
function setupTestDir() {
  if (existsSync(testDir)) {
    rmSync(testDir, { recursive: true });
  }
  mkdirSync(testDir, { recursive: true });
  mkdirSync(docsSpecsDir, { recursive: true });
  mkdirSync(templatesDir, { recursive: true });

  // Create test template files
  writeFileSync(join(templatesDir, 'spec.feature.template.md'), 'Feature: {% raw %}{{ FEATURE_NAME }}{% endraw %} Thread: {% raw %}{{ THREAD_ID }}{% endraw %} PRD: {% raw %}{{ PRD_ID }}{% endraw %}');
  writeFileSync(join(templatesDir, 'spec.plan.adr.prompt.md'), 'Plan ADR: {% raw %}{{ FEATURE_NAME }}{% endraw %} Thread: {% raw %}{{ THREAD_ID }}{% endraw %} ADR: {% raw %}{{ ADR_ID }}{% endraw %}');
  writeFileSync(join(templatesDir, 'spec.plan.prd.prompt.md'), 'Plan PRD: {% raw %}{{ FEATURE_NAME }}{% endraw %} Thread: {% raw %}{{ THREAD_ID }}{% endraw %} PRD: {% raw %}{{ PRD_ID }}{% endraw %}');
  writeFileSync(join(templatesDir, 'spec.plan.sds.prompt.md'), 'Plan SDS: {% raw %}{{ FEATURE_NAME }}{% endraw %} Thread: {% raw %}{{ THREAD_ID }}{% endraw %} SDS: {% raw %}{{ SDS_ID }}{% endraw %}');
  writeFileSync(join(templatesDir, 'spec.plan.ts.prompt.md'), 'Plan TS: {% raw %}{{ FEATURE_NAME }}{% endraw %} Thread: {% raw %}{{ THREAD_ID }}{% endraw %} TS: {% raw %}{{ TS_ID }}{% endraw %}');
  writeFileSync(join(templatesDir, 'spec.plan.task.prompt.md'), 'Plan Task: {% raw %}{{ FEATURE_NAME }}{% endraw %} Thread: {% raw %}{{ THREAD_ID }}{% endraw %} Task: {% raw %}{{ TASK_ID }}{% endraw %}');
  writeFileSync(join(templatesDir, 'spec.tasks.template.md'), 'Tasks: {% raw %}{{ FEATURE_NAME }}{% endraw %} Thread: {% raw %}{{ THREAD_ID }}{% endraw %} Task: {% raw %}{{ TASK_ID }}{% endraw %}');
}

// Clean up test directory
function cleanupTestDir() {
  if (existsSync(testDir)) {
    rmSync(testDir, { recursive: true });
  }
}

// Helper function to run spec_scaffold.sh and capture output/exit code
function runScaffoldScript(args: string[]): { stdout: string; stderr: string; code: number | null } {
  try {
    const stdout = execSync(`bash ${scriptPath} ${args.join(' ')}`, {
      encoding: 'utf8',
      cwd: testDir,
      stdio: ['ignore', 'pipe', 'pipe']
    });
    return { stdout, stderr: '', code: 0 };
  } catch (error: any) {
    return {
      stdout: error.stdout?.toString() || '',
      stderr: error.stderr?.toString() || '',
      code: error.status || 1
    };
  }
}

// Test functions
function testSpecFeatureRecipe() {
  // Test valid feature spec creation
  const result = runScaffoldScript([
    join(templatesDir, 'spec.feature.template.md'),
    docsSpecsDir,
    'thread-123',
    'TestFeature',
    '', // family
    'prd-456' // prd_id
  ]);

  assert.strictEqual(result.code, 0, 'Should exit with code 0 for valid feature spec');
  assert(result.stdout.includes('Scaffolded'), 'Should output success message');
  assert(existsSync(join(docsSpecsDir, 'spec.md')), 'Should create spec.md file');

  const content = readFileSync(join(docsSpecsDir, 'spec.md'), 'utf8');
  assert(content.includes('TestFeature'), 'Should replace FEATURE_NAME');
  assert(content.includes('thread-123'), 'Should replace THREAD_ID');
  assert(content.includes('prd-456'), 'Should replace PRD_ID');
}

function testSpecPlanRecipe() {
  // Test valid plan spec creation for each family
  const families = ['adr', 'prd', 'sds', 'ts', 'task'];
  const idParams = ['', 'adr-789', '', '', '', 'task-999']; // adr_id for adr, task_id for task

  families.forEach((family, index) => {
    const args = [
      join(templatesDir, `spec.plan.${family}.prompt.md`),
      docsSpecsDir,
      'thread-123',
      'TestFeature',
      family
    ];

    // Add specific ID parameter based on family
    if (family === 'adr') {
      args.push('', 'adr-789'); // prd_id, adr_id
    } else if (family === 'task') {
      args.push('', '', '', '', 'task-999'); // prd_id, adr_id, sds_id, ts_id, task_id
    } else {
      args.push('prd-456'); // prd_id for others
    }

    const result = runScaffoldScript(args);
    assert.strictEqual(result.code, 0, `Should exit with code 0 for valid ${family} plan spec`);
    assert(result.stdout.includes('Scaffolded'), `Should output success message for ${family}`);
    assert(existsSync(join(docsSpecsDir, `plan.${family}.md`)), `Should create plan.${family}.md file`);

    const content = readFileSync(join(docsSpecsDir, `plan.${family}.md`), 'utf8');
    assert(content.includes('TestFeature'), `Should replace FEATURE_NAME for ${family}`);
    assert(content.includes('thread-123'), `Should replace THREAD_ID for ${family}`);
  });
}

function testSpecTasksRecipe() {
  // Test valid tasks spec creation
  const result = runScaffoldScript([
    join(templatesDir, 'spec.tasks.template.md'),
    docsSpecsDir,
    'thread-123',
    'TestFeature',
    '', // family
    '', '', '', '', 'task-789' // prd_id, adr_id, sds_id, ts_id, task_id
  ]);

  assert.strictEqual(result.code, 0, 'Should exit with code 0 for valid tasks spec');
  assert(result.stdout.includes('Scaffolded'), 'Should output success message');
  assert(existsSync(join(docsSpecsDir, 'tasks.md')), 'Should create tasks.md file');

  const content = readFileSync(join(docsSpecsDir, 'tasks.md'), 'utf8');
  assert(content.includes('TestFeature'), 'Should replace FEATURE_NAME');
  assert(content.includes('thread-123'), 'Should replace THREAD_ID');
  assert(content.includes('task-789'), 'Should replace TASK_ID');
}

function testPromptLintRecipe() {
  // This test will be implemented after the recipe is created
  assert.ok(true);
}

function testSpecMatrixRecipe() {
  // This test will be implemented after the recipe is created
  assert.ok(true);
}

function testSpecPlanUnknownFamily() {
  // Test error handling for unknown family
  const result = runScaffoldScript([
    join(templatesDir, 'spec.plan.adr.prompt.md'),
    docsSpecsDir,
    'thread-123',
    'TestFeature',
    'invalid' // unknown family
  ]);

  assert.strictEqual(result.code, 1, 'Should exit with code 1 for unknown family');
  assert(result.stderr.includes('Unknown family'), 'Should output error message for unknown family');
  assert(result.stderr.includes('Supported families: adr, prd, sds, ts, task'), 'Should list supported families');
}

function testMissingRequiredParameters() {
  // Test error handling for missing PRD_ID in feature template
  const result = runScaffoldScript([
    join(templatesDir, 'spec.feature.template.md'),
    docsSpecsDir,
    'thread-123',
    'TestFeature'
    // Missing PRD_ID parameter
  ]);

  assert.strictEqual(result.code, 1, 'Should exit with code 1 for missing PRD_ID');
  assert(result.stderr.includes('PRD_ID is required'), 'Should output error message for missing PRD_ID');
}

function testMissingFamilyForPlan() {
  // Test error handling for missing family in plan template
  const result = runScaffoldScript([
    join(templatesDir, 'spec.plan.adr.prompt.md'),
    docsSpecsDir,
    'thread-123',
    'TestFeature'
    // Missing family parameter
  ]);

  assert.strictEqual(result.code, 1, 'Should exit with code 1 for missing family');
  assert(result.stderr.includes('FAMILY is required'), 'Should output error message for missing family');
}

function testMissingAdrIdForAdrPlan() {
  // Test error handling for missing ADR_ID in ADR plan template
  const result = runScaffoldScript([
    join(templatesDir, 'spec.plan.adr.prompt.md'),
    docsSpecsDir,
    'thread-123',
    'TestFeature',
    'adr'
    // Missing ADR_ID parameter
  ]);

  assert.strictEqual(result.code, 1, 'Should exit with code 1 for missing ADR_ID');
  assert(result.stderr.includes('ADR_ID is required'), 'Should output error message for missing ADR_ID');
}

function testMissingTaskIdForTasks() {
  // Test error handling for missing TASK_ID in tasks template
  const result = runScaffoldScript([
    join(templatesDir, 'spec.tasks.template.md'),
    docsSpecsDir,
    'thread-123',
    'TestFeature'
    // Missing TASK_ID parameter
  ]);

  assert.strictEqual(result.code, 1, 'Should exit with code 1 for missing TASK_ID');
  assert(result.stderr.includes('TASK_ID is required'), 'Should output error message for missing TASK_ID');
}

// Run tests
setupTestDir();
try {
  testSpecFeatureRecipe();
  testSpecPlanRecipe();
  testSpecTasksRecipe();
  testPromptLintRecipe();
  testSpecMatrixRecipe();
  testSpecPlanUnknownFamily();
  testMissingRequiredParameters();
  testMissingFamilyForPlan();
  testMissingAdrIdForAdrPlan();
  testMissingTaskIdForTasks();
  console.log('All script tests passed');
} finally {
  cleanupTestDir();
}
