import sys
import os

# get the root path of our project
ROOT_DIR = os.path.abspath(os.curdir)

def main():
    args = sys.argv[1:]
    is_single_output = False
    for arg in args:
        # if -all is passed, compile every input file into a single output.
        if arg == "-all":
            is_single_output = True
    if is_single_output:
        compile_single_output(get_files_in_folder("input", ".txt"))
    else:
        compile_individual_output(args)

def read_file(file):
    '''reads a specified file.'''
    try:
        with open(file, 'r') as f:
            text = f.read().replace('\n', ' ')
        return text
    except:
        print(f"Failed to read file {file}.")
        return False


def write_file(file, text):
    '''writes to a speicified file.'''
    try:
        with open(file, 'w') as f: 
            f.write(text)
            return True
    except:
        print(f"Failed to write to file {file}.")
        return False

def compile_individual_output(args):
    '''Reads an array of files and creates individual output files.'''
    for arg in args:
        file_path = f"{ROOT_DIR}/input/{arg}"
        file_text = read_file(file_path)
        if file_text:
            file_path = f"{ROOT_DIR}/output/{arg}"
            return write_file(file_path, file_text)


def compile_single_output(args):
    '''Reads an array of files and creates a single output file.'''
    file_text = ""
    for arg in args:
        file_path = f"{ROOT_DIR}/input/{arg}"
        file_text += f"{read_file(file_path)} "
    if file_text:
        file_path = f"{ROOT_DIR}/output/single_output.txt"
        return write_file(file_path, file_text)


def get_files_in_folder(directory_path, type=""):
    '''Returns a list of matching files from a directory path.'''
    list = []
    for item in os.listdir(directory_path):
        if type in item:
            list.append(item)
    return list
    

if __name__ == '__main__':
    main()