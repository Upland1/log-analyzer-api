def analyze_logs(log_text: str):
    lines = log_text.strip().split("\n")

    total_lines = len(lines)
    error_count = 0
    ip_count = {}
    status_count = {}

    for line in lines: 
        parts = line.split()

        if len(parts) < 2:
            continue

        ip = parts[0]
        status = parts[-1] # if last word is status

        # count IPs
        ip_count[ip] = ip_count.get(ip, 0) + 1

        # count status codes
        status_count[status] = status_count.get(status, 0) + 1

        # detect errors
        if "ERROR" in line or status.startswith("5"):
            error_count += 1

    # top 5 IPs 
    top_ips = sorted(ip_count.items(), key = lambda x: x[1], reverse = True)[:5]

    error_rate = error_count / total_lines if total_lines > 0 else 0

    return {
            "total_lines": total_lines,
            "error_count": error_count,
            "error_rate": round(error_rate, 3),
            "top_ips": top_ips,
            "status_codes": status_count
            }
