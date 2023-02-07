from src.pyutilator.print.print_args import print_args


@print_args
def method(a, b):
    return a+b


def test_print_args(capfd):
    expected_output = "Function Arguments : (1, 2) \n"

    method(1, 2)
    actual_output, err = capfd.readouterr()

    assert actual_output == expected_output
