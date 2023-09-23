from src.pyutilator.timing.measure_time import measure_time
import time
import re

@measure_time
def method(a, b):
    time.sleep(1)
    return a+b


def test_measure_time(capfd):
    expected_pattern = r"Function 'method' took (\d+\.\d+) seconds to execute"

    method(1, 2)
    actual_output, err = capfd.readouterr()
    print(actual_output)
    assert re.search(expected_pattern, actual_output) is not None
