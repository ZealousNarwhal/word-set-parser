from main import read_file
import os

def test_read_file():
    os.chdir("test")
    assert (read_file("testfile.txt") == "Hello World! How are you?")