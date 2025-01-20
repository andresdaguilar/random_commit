import random
import datetime
import subprocess

# Configuration
file_to_edit = "random_text_file.txt"  # File to modify
lines_to_add = [
    "Random line 1.",
    "Automated random commit.",
    "Another random addition!",
    "Randomness is fun!",
    "Keeping it random and automated.",
]
MAX_COMMITS = 8  # Maximum commits per day

def count_today_commits():
    """Count the number of commits made today."""
    result = subprocess.run(
        ["git", "log", "--since=midnight", "--oneline"], stdout=subprocess.PIPE
    )
    return len(result.stdout.decode().strip().split("\n"))

def add_random_line_to_file():
    """Adds a random line to the specified file."""
    with open(file_to_edit, "a") as file:
        line = random.choice(lines_to_add)
        file.write(f"{datetime.datetime.now()}: {line}\n")
    print(f"Added a random line to {file_to_edit}")

def switch_to_dev_branch():
    """Switch to the dev branch, creating it if it doesn’t exist."""
    subprocess.run(["git", "fetch"], check=True)
    subprocess.run(["git", "checkout", "-B", "dev"], check=True)

if __name__ == "__main__":
    # Ensure the script runs on the dev branch
    switch_to_dev_branch()

    # Check how many commits have been made today
    today_commits = count_today_commits()

    # Decide if another commit should be made
    if today_commits < MAX_COMMITS:
        # Ensure at least 1 commit per day by running once unconditionally
        if today_commits < 3 or random.random() < 0.75:  # 70% chance to commit
            add_random_line_to_file()
        else:
            print("Skipping commit this time (30% chance).")
    else:
        print("Maximum commits reached for today.")
