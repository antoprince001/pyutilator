from src.pyutilator.print.print_return_value import print_return_value


@print_return_value
def method(a, b):
    return a + b


def test_print_args(capfd):
    expected_output = "Function return value : 3 \n"

    method(1, 2)
    actual_output, err = capfd.readouterr()

    assert actual_output == expected_output
