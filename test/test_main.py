from main import *
import os

os.chdir("test")
abspath = os.path.abspath(os.curdir)
testfiles = [
            "testinput.txt",
            "testinput2.txt",
            ]

def test_read_file():
    errors = []
    # Does read return false if given an improper file path?
    t1 = read_file("")
    if not(t1 == False):
        errors.append(f'read_file("") expected False. Instead got {t1}')
    # Does read parse the file correctly?
    t2 = read_file(testfiles[0])
    if not(t2 == "Hello World! Hello World!"):
        errors.append(f'read_file({testfiles[0]}) expected "Hello World! Hello World!". Insead got {t2}')
    assert not errors, errors

def test_get_files_in_folder():
    errors = []
    # Can the function see folders with no substring?
    t1 = get_files_in_folder("")
    if t1:
        errors.append(f'get_files_in_folder("") expected False. Instead got {t1}')
    # Can the function see substrings within a folder?
    t2 = get_files_in_folder(abspath, ".txt")
    if testfiles != t2:
        errors.append(f'get_files_in_folder(abspath, ".txt" expected {testfiles}. Instead got {t2}')
        print(errors)
    assert not errors, errors
