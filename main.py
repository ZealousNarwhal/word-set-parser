import sys

def main():
    args = sys.argv[1:]
    for arg in args:
        with open('output.txt', 'w') as f:
            f.write(read_file(arg))

def read_file(file):
    with open(file, 'r') as f:
        text = f.read().replace('\n', ' ')
    return text


if __name__ == '__main__':
    main()