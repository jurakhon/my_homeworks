filename = 'example.txt'

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

    non_empty_lines = [line for line in lines if line.strip() != '']

    with open(filename, 'w') as file:
        for line in non_empty_lines:
            file.write(line)

    print("empty lines have been deleted successfully")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"error: {e}")