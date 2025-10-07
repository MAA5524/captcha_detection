# Contributing to This Project

Thank you for considering contributing to this project! To ensure consistency and clarity in our Git history, we use the **Conventional Commits** standard for commit messages. Please follow the guidelines below when writing commit messages.

## Commit Message Format

Each commit message consists of a **header**, an optional **body**, and an optional **footer**. The format is as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

- **type**: The type of change (see below for valid types).
- **scope**: Optional, specifies the module or area affected (e.g., `scraper`, `model`, `data`).
- **description**: A short, imperative summary of the change (max 50 characters).
- **body**: Optional, provides more details (max 72 characters per line).
- **footer**: Optional, for breaking changes or issue references (e.g., `Closes #123`).

### Valid Types
- **feat**: A new feature (e.g., `feat(scraper): add support for reCAPTCHA v3`).
- **fix**: A bug fix (e.g., `fix(scraper): resolve timeout in CAPTCHA scraping`).
- **docs**: Documentation changes (e.g., `docs(readme): add scraper setup guide`).
- **style**: Code style changes without logic changes (e.g., `style(scraper): format Python code`).
- **refactor**: Code refactoring without adding features or fixing bugs (e.g., `refactor(model): simplify CNN architecture`).
- **perf**: Performance improvements (e.g., `perf(scraper): optimize image download speed`).
- **test**: Adding or modifying tests (e.g., `test(model): add unit tests for CAPTCHA recognition`).
- **chore**: Maintenance tasks (e.g., `chore(deps): update TensorFlow to v2.15`).
- **ci**: CI/CD changes (e.g., `ci(github): add workflow for model training`).
- **build**: Build system changes (e.g., `build: configure Docker for scraper`).
- **revert**: Revert a previous commit (e.g., `revert: undo feat(scraper) for broken parser`).

### Tips
- Write descriptions in the imperative mood (e.g., "add" instead of "added").
- Use `!` to denote breaking changes (e.g., `feat!: change scraper API structure`).
- Keep the body concise, with a maximum of 72 characters per line.
- Use the footer for breaking changes or to reference issues (e.g., `Closes #123`).

### Example
```
feat(scraper): implement CAPTCHA image extraction

- Add support for downloading CAPTCHA images from target site
- Implement retry logic for failed HTTP requests
- Prepare data pipeline for deep learning model integration

Closes #45
```

## Additional Resources
For more details, see the [Conventional Commits specification](https://www.conventionalcommits.org).