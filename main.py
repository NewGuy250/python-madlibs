def read_story(filename):
    """Read the story from a file."""
    with open(filename, "r") as file:
        return file.read()


def find_placeholders(story, start_char="[", end_char="]"):
    """Extract all unique placeholders from the story."""
    words = set()
    start_of_word = -1

    for i, char in enumerate(story):
        if char == start_char:
            start_of_word = i
        elif char == end_char and start_of_word != -1:
            word = story[start_of_word: i + 1]
            words.add(word)
            start_of_word = -1
    return words


def get_replacements(words):
    """Prompt the user for replacements for each placeholder word."""
    answers = {}
    for word in words:
        answer = input(f"Enter a word for {word}: ")
        answers[word] = answer
    return answers


def replace_placeholders(story, replacements):
    """Replace placeholders in the story with the user-provided replacements."""
    for word, replacement in replacements.items():
        story = story.replace(word, replacement)
    return story


def main():
    """Main function to handle the full process."""
    filename = "story.txt"  # or any filename you wish
    story = read_story(filename)
    
    words = find_placeholders(story)
    
    replacements = get_replacements(words)
    
    updated_story = replace_placeholders(story, replacements)
    
    print(updated_story)


if __name__ == "__main__":
    main()
