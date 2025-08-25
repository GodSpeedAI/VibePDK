import { Tree, formatFiles, installPackagesTask } from '@nx/devkit';
import { getCategory, loadResolvedStack } from '../_utils/stack';
import { deriveServiceDefaults } from '../_utils/stack_defaults';

export default async function (tree: Tree, schema: any) {
  // This generator scaffolds a new service based on domain or CALM specs.
  // The logic should read translator output (domain/domain.yaml) and create
  // Nx applications and libraries using @nxlv/python for Python services or
  // other generators for TypeScript or other languages.
  // Use the Nx devkit to generate files deterministically.

  // TODO: implement service scaffolding.
  // Optional: seed defaults from resolved tech stack (if present)
  try {
    const root = tree.root;
    const stack = loadResolvedStack(root);
    const _backend = getCategory(stack, 'core_application_dependencies');
    // Feature flag: only use derived defaults when explicitly enabled
    // When enabled, derive defaults from the resolved tech stack and only
    // apply them if the user hasn't provided explicit values. This keeps the
    // behavior opt-in and non-breaking. (DEV-PRD, DEV-SDS)
    if (process.env.VIBEPDK_USE_STACK_DEFAULTS === '1') {
      const defaults = deriveServiceDefaults(stack);
      // Apply defaults only if user hasn't provided values.
      // Keep this minimal and non-breaking.
      schema.language = schema.language ?? defaults.language;
      schema.backendFramework = schema.backendFramework ?? defaults.backendFramework;
      schema.packageManager = schema.packageManager ?? defaults.packageManager;
    }
  } catch {
    // Best-effort only; never fail generator on missing stack.
  }
  await formatFiles(tree);
  return () => {
    installPackagesTask(tree);
  };
}
