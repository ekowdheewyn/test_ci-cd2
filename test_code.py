import subprocess
import os

# Define the path to your GitHub repository
REPO_PATH = 'https://github.com/ekowdheewyn/test_ci-cd.git'

# Define the path to your unit tests
TEST_PATH = './test_script.py'

# Run unit tests using pytest
subprocess.run(['pytest', TEST_PATH])

# Commit and push changes to GitHub
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Automated commit from CI/CD pipeline'])
subprocess.run(['git', 'push', REPO_PATH, 'master'])