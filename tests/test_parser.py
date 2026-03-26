from app.services.parser import analyze_logs

def test_error_count():
    logs = [
        '127.0.0.1 GET / 200',
        '192.168.1.1 POST /login 500'
    ]
    
    # join the list into a single string separated
    log_string = "\n".join(logs)
    
    result = analyze_logs(log_string)

    assert result["error_count"] == 1

def test_top_ips():
    # an ip appearing twice, and another appearing once
    logs = "192.168.1.1 GET / 200\n192.168.1.1 GET /about 200\n10.0.0.1 POST /login 500"
    
    result = analyze_logs(logs)
    
    # the first item in the top_ips list should be the 192.168.1.1 tuple with a count of 2
    assert result["top_ips"][0][0] == "192.168.1.1"
    assert result["top_ips"][0][1] == 2