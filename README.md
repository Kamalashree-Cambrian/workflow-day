# Employee Task Tracker

A small Python + Streamlit app used to demonstrate an industry-style
source-control workflow: Git, GitHub, branching, pull requests, and CI/CD.

## Stack
- Python
- Streamlit (UI)
- Pandas (data)
- Pytest (tests)
- GitHub Actions (CI)

## Run in GitHub Codespaces (no local install needed)

1. Open this repository on GitHub.
2. Click **Code** → **Codespaces** tab → **Create codespace on main**.
3. Wait for the container to build. Dependencies install automatically
   (see `.devcontainer/devcontainer.json`).
4. In the Codespaces terminal, run:
   ```bash
   streamlit run app.py
   ```
5. A "Ports" popup/notification will appear — click **Open in Browser**
   (or open the **Ports** tab and click the globe icon next to port 8501).

## Run tests

```bash
pytest
```

## Project structure

```
employee-task-tracker/
├── app.py                      # UI
├── task_manager.py             # business logic
├── requirements.txt            # dependencies
├── tests/
│   └── test_task_manager.py
├── .devcontainer/
│   └── devcontainer.json       # Codespaces environment
└── .github/
    └── workflows/
        └── ci.yml              # CI: install + pytest on push/PR
```

## Branching workflow

```bash
git switch main
git pull
git switch -c feature/your-change
# edit code
git add .
git commit -m "feat: describe the change"
git push -u origin feature/your-change
# open a Pull Request on GitHub, let CI run, then merge
```

## Security

Never commit secrets, passwords, API keys, or tokens. Use GitHub Secrets
for any CI credentials.
