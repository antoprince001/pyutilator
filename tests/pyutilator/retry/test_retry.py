from src.pyutilator.retry.retry import retry, MaxRetriesExceededException
import pytest

retry_count = 0
MAX_RETRIES = 3


@retry(max_retries=MAX_RETRIES)
def function_that_raises_exception():
    raise Exception("Custom Exception for Testing")


@retry(max_retries=MAX_RETRIES)
def function_that_succeeds_on_retry():
    global retry_count
    if retry_count < 2:
        retry_count += 1
        raise Exception("Custom Exception for Testing")
    return "Success"


def test_retry_decorator_raises_exception():
    with pytest.raises(MaxRetriesExceededException) as exception_info:
        function_that_raises_exception()

    assert str(exception_info.value) == "Max retries reached."


def test_retry_decorator_succeeds_on_retry():
    expected_output = "Success"

    result = function_that_succeeds_on_retry()

    assert result == expected_output
