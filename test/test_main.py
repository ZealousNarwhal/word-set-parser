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
    e1 = False
    if not(t1 == e1):
        errors.append(f'read_file("") expected {e1}. Instead got {t1}')
    # Does read parse the file correctly?
    t2 = read_file(testfiles[0])
    e2 = "hello world hello world"
    if not(t2 == e2):
        errors.append(f'read_file({testfiles[0]}) expected {e2}. Insead got {t2}')
    assert not errors, errors

def test_get_files_in_folder():
    errors = []
    # Can the function see folders with no substring?
    t1 = get_files_in_folder("")
    e1 = False
    if t1:
        errors.append(f'get_files_in_folder("") expected {e1}. Instead got {t1}')
    # Can the function see substrings within a folder?
    t2 = get_files_in_folder(abspath, ".txt")
    e2 = testfiles
    if t2 != e2:
        errors.append(f'get_files_in_folder(abspath, ".txt" expected {e2}. Instead got {t2}')
        print(errors)
    assert not errors, errors
