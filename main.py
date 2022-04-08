import sys
import os

# get the root path of our project
ROOT_DIR = os.path.abspath(os.curdir)

def main():
    args = sys.argv[1:]
    for arg in args:
        file_path = f"{ROOT_DIR}\input\{arg}"
        file_text = read_file(file_path)
        if file_text:
            file_path = f"{ROOT_DIR}\output\{arg}"
            write_file(file_path, file_text)

def read_file(file):
    try:
        with open(file, 'r') as f:
            text = f.read().replace('\n', ' ')
        return text
    except:
        print(f"Failed to read file {file}.")
        return False


def write_file(file, text):
    try:
        with open(file, 'w') as f:
            f.write(text)
            return True
    except:
        print(f"Failed to write to file {file}.")
        return False


if __name__ == '__main__':
    main()