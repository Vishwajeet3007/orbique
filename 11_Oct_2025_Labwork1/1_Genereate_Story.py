import random

def generate_story(word):
    # A set of templates to create a story around the user-provided word
    templates = [
        f"Once upon a time, there was a small {word} who lived in a quiet village. Every day, it dreamed of adventure and excitement.",
        f"A {word} named Charlie set off on a journey across the world. Along the way, it met many interesting characters.",
        f"In the kingdom of {word}, a young hero set out to defeat an ancient monster. Only the bravest dared enter the dark forest.",
        f"The wise {word} was the village's greatest secret. It could solve any problem, but only when the moon was full.",
        f"Long ago, a magical {word} appeared in the middle of a bustling city. People from all around came to see its mysterious powers."
    ]

    # Randomly choose one of the templates
    story = random.choice(templates)

    return story

def main():
    user_word = input("Enter a word to generate a story: ")
    story = generate_story(user_word)
    print("\nHere's your story:\n")
    print(story)

if __name__ == "__main__":
    main()
