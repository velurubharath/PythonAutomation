
def analyze_log(file):
    info_count = 0
    error_count = 0
    warn_count = 0
    for line in file:
        if "INFO" in line:
            info_count+=1
        elif "ERROR" in line:
            error_count+=1
        elif "WARN" in line:
            warn_count+=1
    return info_count,error_count,warn_count


with open ("app.log","r") as file:
    info_count,error_count,warn_count = analyze_log(file)
    print (f"INFO: {info_count}")
    print (f"ERROR: {error_count}")
    print (f"WARN: {warn_count}")
