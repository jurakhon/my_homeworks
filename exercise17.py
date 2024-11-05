filename = 'example.txt'
old_word = 'world'
new_word = 'Python'

try:
    with open(filename, 'r') as file:
        content = file.read()

    updated_content = content.replace(old_word, new_word)

    with open(filename, 'w') as file:
        file.write(updated_content)

    print(filename)
    print(f"'{old_word}' has been changed to '{new_word}'.")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"error: {e}")