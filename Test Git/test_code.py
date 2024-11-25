import subprocess

# Define GitHub repository URL
GITHUB_REPOSITORY = "https://github.com/ekowdheewyn/test_ci-cd2.git"

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

def commit_and_push_changes():
    """
    Commits and pushes changes to the GitHub repository.
    """
    try:
        # Check if there are any changes to commit
        try:
            subprocess.run(["git", "diff", "--quiet", "--exit-code"], check=True)
            print("No changes to commit.")
            return
        except subprocess.CalledProcessError:
            # Changes exist, proceed with commit
            pass

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
    except ValueError as e:
        print(f"Invalid repository URL or branch name: {e}")
        exit(1)

if __name__ == "__main__":
    run_unit_tests()
    commit_and_push_changes()