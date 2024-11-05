filename = 'example.txt'

try:
    with open(filename, 'r') as file:
        content = file.read()

    words = content.split()

    word_count = len(words)

    print(f"number of words in file: {word_count}")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"error: {e}")