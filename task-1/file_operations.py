def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Written contents to {filename}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

def append_to_file(filename, content):
    with open(filename, 'a') as f:
        f.write(content)
    print(f"Appended contents to {filename}")

# Example Usage
if __name__ == "__main__":
    write_file("example.txt", "Hello Sir!, I'm Aayush Singh and i am a DevOps and cloud computing engineer.\n")
    append_to_file("example.txt", " I know about Python, linux, scripting, aws, jenkins, github, etc.\n")
    print("File Contents:\n", read_file("example.txt"))
