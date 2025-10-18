# 🤝 Contributing Guide

Thank you for taking the time to contribute to this project!
To keep our Git history clean and meaningful, we follow the **[Conventional Commits](https://www.conventionalcommits.org)** standard.
Please read these short guidelines before making a commit.

---

## 🧩 Commit Message Format

Each commit message should include a **header**, and may optionally include a **body** and/or **footer**.

```

<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

```

### 📌 Rules
| Part | Description |
|------|--------------|
| **type** | Describes the kind of change (see list below). |
| **scope** | *(optional)* — the part of the codebase affected (e.g. `scraper`, `model`, `data`). |
| **description** | Short, imperative summary *(max 50 chars)*. |
| **body** | *(optional)* — detailed explanation *(max 72 chars/line)*. |
| **footer** | *(optional)* — for breaking changes or issue references *(e.g. `Closes #42`)*. |

---

## 🧠 Valid Commit Types

| Type | Purpose | Example |
|------|----------|---------|
| **feat** | ✨ New feature | `feat(scraper): add reCAPTCHA v3 support` |
| **fix** | 🐛 Bug fix | `fix(scraper): resolve timeout issue` |
| **docs** | 📝 Documentation only | `docs(readme): update setup instructions` |
| **style** | 🎨 Code style or formatting | `style(scraper): apply Black formatter` |
| **refactor** | 🧹 Code refactor (no new features or fixes) | `refactor(model): simplify CNN layers` |
| **perf** | ⚡ Performance improvement | `perf(scraper): optimize download speed` |
| **test** | ✅ Adding or updating tests | `test(model): add unit tests for recognizer` |
| **chore** | 🔧 Maintenance tasks | `chore(deps): upgrade TensorFlow to 2.15` |
| **ci** | 🚀 CI/CD changes | `ci(github): add model training workflow` |
| **build** | 🏗️ Build system changes | `build: configure Docker for scraper` |
| **revert** | ⏪ Revert previous commit | `revert: undo feat(scraper)` |

---

## 💡 Writing Tips

- Use the **imperative mood** → “add” not “added”.
- Use `!` for **breaking changes** → `feat!: change scraper API`.
- Keep the body **concise** (≤72 chars per line).
- Use the footer for **issues or breaking notes** → `Closes #123`.

---

## 🧾 Example Commit

```

feat(scraper): implement CAPTCHA image extraction

* Add support for downloading CAPTCHA images from target site
* Implement retry logic for failed HTTP requests
* Prepare data pipeline for model integration

Closes #45

```

---

## 📚 Additional Resources
- 📖 [Conventional Commits Specification](https://www.conventionalcommits.org)
- 🧠 [CommitLint](https://commitlint.js.org) — useful for enforcing these rules automatically

---

> **Tip:** Keeping commits clean helps everyone understand the evolution of the project.
> Small, well-labeled commits are the best kind of commits. 💪


## ❤️ Thank You

Every contribution helps make this project a better learning resource for the community.
We truly appreciate your time and effort in improving it!
