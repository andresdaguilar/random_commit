import random

# Configuration
file_to_edit = "random_text_file.txt"  # Relative path to the file to be edited
commit_message = "Automated random update"
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
        file.write(random.choice(lines_to_add) + "\n")
    print(f"Random line added to {file_to_edit}")

if __name__ == "__main__":
    add_random_line_to_file()