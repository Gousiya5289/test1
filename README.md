Python DevOps Automation with GitHub Actions
📌 Overview

This project demonstrates how to use Python scripting for DevOps automation and integrate it into a CI/CD pipeline using GitHub Actions.

The pipeline automatically runs a Python script on every push to the main branch to validate disk space on the CI runner. If the disk space falls below a defined threshold, the pipeline fails.

This simulates a real-world DevOps automation use case where Python is used as a validation and automation layer in CI/CD.

🛠️ Tools & Technologies Used

Python 3

GitHub Actions

GitHub Repository

Online VS Code / GitHub Web UI

📂 Project Structure
test1/
├── disk_check.py
├── README.md
└── .github/
    └── workflows/
        └── python-devops.yml

🐍 Python Script Description

The disk_check.py script:

Checks available disk space on the system

Accepts a threshold value as a command-line argument

Exits with a failure code if disk space is below the threshold

Can be reused across environments (CI/CD, servers, containers)

Script Features

Uses argparse for dynamic inputs

Uses shutil to fetch disk usage

Uses exit codes to control pipeline success/failure

▶️ Python Script Example
python disk_check.py --threshold 5

🔄 CI/CD Pipeline (GitHub Actions)
Workflow Trigger

Runs automatically on every push to the main branch

Pipeline Steps

Checkout source code

Setup Python runtime dynamically

Execute the Python automation script

Fail or pass the pipeline based on script output

📄 GitHub Actions Workflow

File location:

.github/workflows/python-devops.yml


Pipeline runs on:

ubuntu-latest runner

Python version 3.10

✅ Successful Pipeline Output

Python environment installed

Disk space checked

Pipeline marked SUCCESS if threshold is met

Pipeline marked FAILED if threshold is breached

🧠 DevOps Use Case

This approach can be extended for:

Pre-deployment validations

Infrastructure health checks

Kubernetes/Docker automation

Cloud resource monitoring

CI/CD quality gates

💬 Interview Explanation

“I developed a Python automation script and integrated it with GitHub Actions. The pipeline dynamically installs Python and executes the script on every push, acting as a validation step in CI/CD.”
