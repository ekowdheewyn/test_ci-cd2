import os
import subprocess
import sys

# Define GitHub repository URL
GITHUB_REPOSITORY = "https://github.com/yourusername/yourrepository.git"

# Define branch name
BRANCH_NAME = "main"

def run_unit_tests():
    """
    Runs unit tests using pytest.
    """
    try:
        subprocess.run(["pytest", "tests"], check=True)
        print("Unit tests passed!")
    except subprocess.CalledProcessError as e:
        print(f"Unit tests failed: {e}")
        exit(1)

def check_for_changes():
    """
    Checks if there are any changes to commit.
    """
    try:
        # Check for changes
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if result.stdout.strip():
            return True
        else:
            print("No changes to commit.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Failed to check for changes: {e}")
        exit(1)

def commit_and_push_changes():
    """
    Commits and pushes changes to the GitHub repository.
    """
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit changes with a message
        subprocess.run(["git", "commit", "-m", "Automated commit from CI/CD pipeline"], check=True)

        # Push changes to the GitHub repository
        subprocess.run(["git", "push", GITHUB_REPOSITORY, f"HEAD:{BRANCH_NAME}"], check=True)
        print("Changes committed and pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit and push changes: {e}")
        exit(1)

if __name__ == "__main__":
    run_unit_tests()

    if check_for_changes():
        commit_and_push_changes()
    else:
        print("No changes to commit. Exiting.")
        exit(0)