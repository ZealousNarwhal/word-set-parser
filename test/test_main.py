from main import read_file
import os

def test_read_file():
    errors = []
    os.chdir("test")

    # Does read return false if given an improper file path?
    if not(read_file("") == False):
        errors.append("read_file failed to return False with an incorrect file path.")

    if not(read_file("testfile.txt") == "Hello World! How are you?"):
        errors.append("read_file failed to parse correctly.")

    assert not errors, errors