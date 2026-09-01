from unittest.mock import Mock, patch

import pytest

from retry_utils import call_with_retry

def test_success_without_retry():
    operation = Mock(return_value="success")

    result = call_with_retry(operation)

    assert result == "success"
    operation.assert_called_once_with()

def test_retry_then_success():
    operation = Mock(
        side_effect=[
            RuntimeError("temporary failure"),
            "success"
        ]
    )

    with patch("retry_utils.time.sleep") as mock_sleep:
        result = call_with_retry(
            operation,
            max_attempts=3,
            base_delay=1
        )

    assert result == "success"

    assert operation.call_count == 2

    mock_sleep.assert_called_once_with(1)

def test_all_attempts_fail():
    operation = Mock(
        side_effect=RuntimeError("AWS unavailable")
    )

    with patch("retry_utils.time.sleep") as mock_sleep:

        with pytest.raises(RuntimeError):
            call_with_retry(
                operation,
                max_attempts=3,
                base_delay=1
            )

    assert operation.call_count == 3

    assert mock_sleep.call_count == 2

def test_exponential_backoff():
    operation = Mock(
        side_effect=[
            RuntimeError("failure 1"),
            RuntimeError("failure 2"),
            "success"
        ]
    )

    with patch("retry_utils.time.sleep") as mock_sleep:
        result = call_with_retry(
            operation,
            max_attempts=3,
            base_delay=1
        )

    assert result == "success"

    assert mock_sleep.call_count == 2

    mock_sleep.assert_any_call(1)
    mock_sleep.assert_any_call(2)