import random
import datetime

# Configuration
file_to_edit = "random_text_file.txt"  # File to modify
lines_to_add = [
    "Random line 1.",
    "Automated random commit.",
    "Another random addition!",
    "Randomness is fun!",
    "Keeping it random and automated.",
]

# Define the maximum commits per day
MAX_COMMITS = 8

def count_today_commits():
    """Count the number of commits made today."""
    import subprocess
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

if __name__ == "__main__":
    # Check how many commits have been made today
    today_commits = count_today_commits()

    # Decide if another commit should be made
    if today_commits < MAX_COMMITS:
        # Ensure at least 1 commit per day by running once unconditionally
        if today_commits == 0 or random.choice([True, False]):
            add_random_line_to_file()
        else:
            print("Skipping commit this time.")
    else:
        print("Maximum commits reached for today.")
