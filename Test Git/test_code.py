import subprocess

# Define GitHub repository URL
GITHUB_REPOSITORY = "https://github.com/ekowdheewyn/test_ci-cd2.git"

# Define branch name
BRANCH_NAME = "main"


def run_unit_tests():
    """Runs unit tests using pytest."""
    try:
        subprocess.run(["pytest", "tests"], check=True)
        print("Unit tests passed!")
    except subprocess.CalledProcessError as e:
        print(f"Unit tests failed: {e}")
        exit(1)


def has_changes_to_commit():
    """
    Checks if there are any changes to commit.
    Returns True if changes exist, False otherwise.
    """
    result = subprocess.run(
        ["git", "status", "--porcelain"], stdout=subprocess.PIPE, text=True
    )
    return bool(result.stdout.strip())  # Returns True if there are staged/unstaged changes


def commit_and_push_changes():
    """Commits and pushes changes to the GitHub repository."""
    try:
        # Check if there are changes to commit
        if not has_changes_to_commit():
            print("No changes to commit. Skipping commit and push steps.")
            return

        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit changes with a message
        subprocess.run(
            ["git", "commit", "-m", "Automated commit from CI/CD pipeline"], check=True
        )

        # Validate the repository URL and branch name
        if not GITHUB_REPOSITORY.startswith("https://github.com/"):
            raise ValueError("Invalid GitHub repository URL.")

        # Push changes to the GitHub repository
        subprocess.run(
            ["git", "push", GITHUB_REPOSITORY, f"HEAD:{BRANCH_NAME}"], check=True
        )
        print("Changes committed and pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit and push changes: {e}")
        exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    run_unit_tests()
    commit_and_push_changes()
