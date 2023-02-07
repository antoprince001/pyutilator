from src.pyutilator.print.print_kwargs import print_kwargs


@print_kwargs
def method(a, b):
    return a + b


def test_print_args(capfd):
    expected_output = "Function Key Word Arguments : {'a': 1, 'b': 2}\n"

    method(a=1, b=2)
    actual_output, err = capfd.readouterr()

    assert actual_output == expected_output
