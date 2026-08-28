from logAnalysis import generate_alerts

def test_generate_alerts():
    #above boundary
    assert generate_alerts(5,3) is True

def test_no_alerts():
    assert generate_alerts(1,3) is False

def test_boundary_alerts():
    assert generate_alerts(5,5) is False




