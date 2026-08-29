from logAnalysis import generate_alerts, get_error_counts, get_repeated_errors, validate_line, read_log
from io import StringIO
import pytest

def test_generate_alerts():
    #above boundary
    assert generate_alerts(5,3) is True

def test_no_alerts():
    assert generate_alerts(1,3) is False

def test_boundary_alerts():
    assert generate_alerts(5,5) is False

def test_get_error_counts():
    log_data = """2026-08-28 10:00:01 ERROR payment-api Database connection failed
    2026-08-28 10:00:02 ERROR payment-api Database connection failed
    2026-08-28 10:00:03 ERROR inventory-api Redis connection failed
    """

    file = StringIO(log_data)
    result = get_error_counts(file) 
    assert result == {'payment-api': 2, 'inventory-api': 1}

def test_malformed_line():
    log_data = """2026-08-28 10:00:01 ERROR 
    """

    file = StringIO(log_data)
    result = validate_line(log_data)
    assert result is False

def test_read_log():
    with pytest.raises(FileNotFoundError):
        read_log("non_existenet_file.log")

