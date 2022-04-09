from main import read_file
import os

def test_read_file():
    errors = []
    os.chdir("test")

    # Does read return false if given an improper file path?
    if not(read_file("") == False):
        errors.append('FAILED read_file("") == False.')

    if not(read_file("testfile.txt") == "Hello World! How are you?"):
        errors.append('FAILED read_file("testfile.txt") == "Hello World! How are you?".')

    assert not errors, errors