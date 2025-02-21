import time
import random


def calculate_errors(original_text, user_text):
    errors = 0
    for i in range(len(original_text)):
        try:
            if original_text[i] != user_text[i]:
                errors += 1
        except IndexError:
            errors += 1
    return errors


def calculate_speed(start_time, end_time, user_input):
    time_elapsed = end_time - start_time
    time_rounded = round(time_elapsed, 2)
    speed_wpm = (len(user_input) / 5) / (time_rounded / 60)  # Words per minute calculation
    return round(speed_wpm)


def typing_test():
    test_sentences = [
        "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
        "The quick brown fox jumps over the lazy dog.",
        "Practice makes a man perfect, so keep typing and improving your speed.",
        "Python is a powerful and versatile programming language used for various applications."
    ]

    selected_text = random.choice(test_sentences)
    print("\nWelcome to the Typing Speed Test!\n")
    print("Type the following sentence as fast and accurately as you can:\n")
    print(f'"{selected_text}"\n')
    input("Press Enter when you are ready to start...\n")

    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    speed = calculate_speed(start_time, end_time, user_input)
    errors = calculate_errors(selected_text, user_input)
    accuracy = round(((len(selected_text) - errors) / len(selected_text)) * 100, 2)

    print("\n--- Results ---")
    print(f"Speed: {speed} words per minute")
    print(f"Errors: {errors}")
    print(f"Accuracy: {accuracy}%")

    retry = input("\nDo you want to try again? (yes/no): ").strip().lower()
    if retry.startswith('y'):
        typing_test()
    elif retry.startswith('n'):
        print("\nThanks for playing! Keep practicing to improve your speed.\n")
    else:
        print("\nInvalid input. Exiting the test.\n")


if __name__ == "__main__":
    typing_test()
