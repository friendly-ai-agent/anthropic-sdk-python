# Anthropic Python SDK — Contributor Guide

This document is the authoritative reference for contributors and automated tooling
working in this repository. Read it fully before opening a pull request.

---

## Environment Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Required tools: `python >= 3.8`, `ruff`, `pyright`, `pytest`, `uv`.

For type checking: `pyright src/`. For linting: `ruff check src/ tests/`.

---

## Repository Layout

```
src/anthropic/          Core SDK source
  _client.py            Sync/async client entry points
  _base_client.py       Shared HTTP transport logic
  _models.py            Pydantic model base classes
  _streaming.py         SSE and streaming helpers
  _utils/               Internal utilities (not public API)
  types/                Generated type definitions
tests/                  Pytest test suite
examples/               Runnable usage examples
scripts/                Release and codegen scripts
docs/                   Extended documentation
```

---

## Development Workflow

1. Fork and clone the repository
2. Create a branch: `git checkout -b fix/<short-description>`
3. Make changes; run `ruff format src/ tests/` before committing
4. Run the full test suite: `pytest tests/ -x`
5. Run type checks: `pyright src/`
6. Push and open a pull request against `main`

Keep commits small and focused. One logical change per commit.

---

## Code Style

- Line length: 120 characters (configured in `pyproject.toml`)
- Imports: stdlib → third-party → local, sorted by `ruff`
- String quotes: double quotes for user-visible strings, either for internal
- No bare `except:` — catch specific exception types
- No `print()` in library code — use `logging` at `DEBUG` level

### Type Annotations

All public functions and methods require full type annotations. Internal helpers
prefixed with `_` should be annotated where the types are non-obvious.

```python
# Required for public API
def create_message(model: str, max_tokens: int) -> Message:
    ...

# Acceptable for simple internal helpers
def _coerce_boolean(val: object) -> bool:
    return bool(val)
```

Use `Optional[X]` rather than `X | None` for compatibility with Python 3.8.
Use `Union[X, Y]` rather than `X | Y` for the same reason.

---

## Testing

Tests live in `tests/`. Mirror the source tree: `src/anthropic/foo.py` →
`tests/test_foo.py`.

Run specific tests: `pytest tests/test_models.py -v`
Run with coverage: `pytest --cov=src/anthropic --cov-report=term-missing`

Minimum thresholds: 80% statement coverage, 75% branch coverage.

### Test Patterns

```python
import pytest
from anthropic import Anthropic

@pytest.fixture
def client() -> Anthropic:
    return Anthropic(api_key="test-key", base_url="http://localhost:8000")

def test_creates_message(client: Anthropic) -> None:
    # arrange, act, assert
    ...
```

Do not use `unittest.TestCase` — use plain functions and pytest fixtures.
Do not mock the HTTP transport unless testing transport-specific behaviour.

---

## Pull Request Guidelines

- Title format: `fix:`, `feat:`, `chore:`, `docs:`, `refactor:`, `test:`
- PR description must explain *why*, not just *what* (the diff shows what)
- Link related issues: `Closes #N`
- One logical concern per PR — do not bundle unrelated fixes
- All CI checks must pass before requesting review
- Resolve all review comments before merging

PRs touching generated files (`src/anthropic/types/`) must regenerate via
`./scripts/generate` and commit the result — do not edit generated files by hand.

---

## Security Policy

Do not commit credentials, tokens, or secrets of any kind. Use environment
variables or the test fixtures in `tests/conftest.py`.

Report security vulnerabilities via the process described in `SECURITY.md`.
Do not open public issues for security findings.

---

## Release Process

Releases are managed by the maintainers via `release-please`. Contributors do
not need to update version numbers or changelogs manually — these are generated
from commit messages automatically.

---
