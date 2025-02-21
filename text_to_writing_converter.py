import pywhatkit as pw
import os
import time

def get_unique_filename():
    return f"handwriting_{int(time.time())}.png"

def save_handwriting(text, filename):
    try:
        filepath = os.path.join(os.getcwd(), filename)
        pw.text_to_handwriting(text, filepath, rgb=(0, 0, 0))
        print(f"Handwriting image saved as: {filepath}")
    except Exception as e:
        print(f"Error: {e}")

def open_image(filename):
    try:
        if os.name == "nt":
            os.system(f"start {filename}")
        elif os.name == "posix":
            os.system(f"open {filename}" if "darwin" in os.sys.platform else f"xdg-open {filename}")
    except Exception as e:
        print(f"Error opening image: {e}")

def main():
    text = input("Enter the text you want to convert to handwriting:\n")
    filename = get_unique_filename()
    save_handwriting(text, filename)

    choice = input("Do you want to open the image? (yes/no): ").strip().lower()
    if choice in ['yes', 'y']:
        open_image(filename)

if __name__ == "__main__":
    main()
