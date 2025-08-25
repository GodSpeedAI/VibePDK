import { getCategory } from './stack';

export type ServiceDefaults = {
    language: 'python' | 'typescript';
    backendFramework: 'fastapi' | 'express' | 'nest' | 'none';
    packageManager: 'pnpm' | 'npm' | 'yarn';
};

/**
 * Derive generator defaults from resolved tech stack (deterministic, minimal).
 * Pure function; safe to use in dry-runs and planning.
 */
export function deriveServiceDefaults(stack: any | null): ServiceDefaults {
    // Hard defaults (stable)
    let language: ServiceDefaults['language'] = 'python';
    let backendFramework: ServiceDefaults['backendFramework'] = 'none';
    let packageManager: ServiceDefaults['packageManager'] = 'pnpm';

    // Frontend package manager preference (if present)
    const frontend = getCategory(stack, 'frontend_client_dependencies');
    if (frontend && typeof frontend === 'object') {
        // Keep default pnpm unless explicit hint found (none for now)
    }

    // Backend framework detection
    const core = getCategory(stack, 'core_application_dependencies');
    if (core && typeof core === 'object') {
        const webFrameworks: any = (core as any).web_frameworks;
        if (Array.isArray(webFrameworks)) {
            const lower = webFrameworks.map(String).map((s) => s.toLowerCase());
            if (lower.includes('fastapi')) backendFramework = 'fastapi';
            else if (lower.includes('express')) {
                backendFramework = 'express';
                language = 'typescript';
            } else if (lower.includes('nest') || lower.includes('@nestjs')) {
                backendFramework = 'nest';
                language = 'typescript';
            }
        }
    }

    return { language, backendFramework, packageManager };
}
