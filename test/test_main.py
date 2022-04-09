from main import read_file
import os

def test_read_file():
    errors = []
    os.chdir("test")

    # Does read return false if given an improper file path?
    r1 = read_file("")
    if not(r1 == False):
        errors.append(f'read_file("") expected False. Instead got {r1}')

    r2 = read_file("testfile.txt")
    if not(r2 == "Hello World! Hello World!!"):
        errors.append(f'read_file("testfile.txt") expected "Hello World! Hello World!". Insead got {r2}')

    assert not errors, errors