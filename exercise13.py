filename = 'example.txt'
n = int(input())

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

        last_n_lines = lines[-n:]

        for line in last_n_lines:
            print(line, end='')
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"error: {e}")