from ctypes import sizeof
from operator import indexOf
import sys
import os

ROOT_DIR = os.path.abspath(os.curdir)

def main():
    args = set(sys.argv[1:])
    flags = set()
    for arg in args:
        # if checks for flags in args, compile every input file into a single output.
        if arg == "-all":
            flags.add("-all")
        if arg == "-csv":
            flags.add("-csv")
    args -= flags
    if "-all" in flags:
        compile_single_output(get_files_in_folder("input", ".txt"), flags)
    else:
        compile_individual_output(args, flags)

def read_file(file):
    '''reads a specified file.'''
    try:
        with open(file, 'r') as f:
            text = f.read().replace('\n', " ")
            text = remove_characters(text, ['!', '?', '.', ','])
            text = text.lower()

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

def compile_individual_output(args, flags):
    '''Reads an array of files and creates individual output files.'''
    for arg in args:
        file_path = f"{ROOT_DIR}/input/{arg}"
        file_text = read_file(file_path)
        if "-csv" in flags:
            file_text = text_to_csv(file_text)
        if file_text:
            file_path = f"{ROOT_DIR}/output/{arg}"
            write_file(file_path, file_text)
    return True


def compile_single_output(args, flags):
    '''Reads an array of files and creates a single output file.'''
    files_text = []
    for arg in args:
        file_path = f"{ROOT_DIR}/input/{arg}"
        files_text.append(f"{read_file(file_path)} ")
    file_text = "".join(files_text)
    if "-csv" in flags:
        file_text = text_to_csv(file_text)
    if file_text:
        file_path = f"{ROOT_DIR}/output/single_output.txt"
        write_file(file_path, file_text)
        return True
    return False


def get_files_in_folder(directory_path, type=""):
    '''Returns a list of matching files from a directory path.'''
    list = []
    try:
        for item in os.listdir(directory_path):
            if type in item:
                list.append(item)
        return list
    except:
        print("Invalid directory path provided to get_files_in_folder")
        return False


def text_to_csv(text):
    '''Takes raw text input and outputs unique words in csv format.'''
    text = text.rstrip()
    words = set()
    for word in text.split():
        if word.isalpha():
            words.add(f"{word},")
    # Remove the comma delimiter from the final word
    return "".join(words).rstrip(',')


def remove_characters(text, chars):
    '''scans a string and will remove any characters specified in a list.'''
    text_string = []
    for char in text:
        if char not in chars:
            text_string.append(char)    
    return "".join(text_string)

if __name__ == '__main__':
    main()