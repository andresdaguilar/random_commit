import random
import datetime

# Configuration
file_to_edit = "random_text_file.txt"  # File to edit
lines_to_add = [
    "This is a random line.",
    "Another random line added!",
    "Automated commit, because why not?",
    "Randomness is fun!",
    "Here's another random thought."
]

def add_random_line_to_file():
    """Adds a random line to the specified file."""
    with open(file_to_edit, "a") as file:
        line = random.choice(lines_to_add)
        file.write(f"{datetime.datetime.now()}: {line}\n")
    print(f"Random line added to {file_to_edit}")

if __name__ == "__main__":
    add_random_line_to_file()
