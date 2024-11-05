source_filename = 'source.txt'
destination_filename = 'destination.txt'

try:
    with open(source_filename, 'r') as source_file:
        content = source_file.read()

    with open(destination_filename, 'w') as destination_file:
        destination_file.write(content)

    print("file copied successfully")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"error: {e}")