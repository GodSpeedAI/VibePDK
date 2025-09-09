#!/usr/bin/env bash
# Token counter for prompt files.
# Default: approximate by counting words.
# Accurate: if PROMPT_TOKENIZER=accurate and Node tokenizer present, use tools/prompt/plan_preview.js

set -eu

if [[ "$#" -lt 1 ]]; then
  echo "Usage: $0 <prompt-file>" >&2
  exit 1
fi

PROMPT_FILE="$1"
if [[ ! -f "${PROMPT_FILE}" ]]; then
  echo "Error: prompt file '${PROMPT_FILE}' does not exist." >&2
  exit 1
fi

if [[ "${PROMPT_TOKENIZER:-}" == "accurate" ]]; then
  if command -v node >/dev/null 2>&1; then
    TOKENS=$(node tools/prompt/plan_preview.js --accurate "${PROMPT_FILE}" 2>/dev/null | sed -n 's/.*tokens=\([0-9]\+\).*/\1/p' || true)
    if [[ -n "${TOKENS}" ]]; then
      echo "[measure_tokens] Accurate tokens for ${PROMPT_FILE}: ${TOKENS}"
      exit 0
    fi
  fi
fi

WORD_COUNT=$(wc -w < "${PROMPT_FILE}")
CHAR_COUNT=$(wc -c < "${PROMPT_FILE}")

echo "[measure_tokens] Approximate word count for ${PROMPT_FILE}: ${WORD_COUNT}"
echo "[measure_tokens] Approximate character count for ${PROMPT_FILE}: ${CHAR_COUNT}"

exit 0
