import { Tree, formatFiles, installPackagesTask } from '@nx/devkit';

export default async function (tree: Tree, schema: any) {
  // This generator scaffolds a new service based on domain or CALM specs.
  // The logic should read translator output (domain/domain.yaml) and create
  // Nx applications and libraries using @nxlv/python for Python services or
  // other generators for TypeScript or other languages.
  // Use the Nx devkit to generate files deterministically.

  // TODO: implement service scaffolding.
  await formatFiles(tree);
  return () => {
    installPackagesTask(tree);
  };
}