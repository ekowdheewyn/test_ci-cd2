import subprocess
import os

# Define the GitHub repository URL
repo_url = "https://github.com/ekowdheewyn/test_ci-cd.git"

# Define the branch to push changes to
branch = "main"

# Define the path to the pytest script
pytest_script = "test_script.py"

# Run unit tests using pytest
subprocess.run(["pytest", pytest_script], check=True)

# Commit and push changes to the GitHub repository
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Automated commit from CI/CD pipeline"])
subprocess.run(["git", "push", repo_url, branch])