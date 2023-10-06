# BEGIN: be15d9bcejpp
from co_pilot_test import hello_world


def test_hello_world(capsys):
    """
    Test function to check if the hello_world() function outputs "Hello World!" to the console.
    """
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"
# END: be15d9bcejpp