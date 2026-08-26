def analyze_log(file):
    info_count = 0
    error_count = 0
    warn_count = 0
    for line in file:
        if line.contains("INFO"):
         info_count+=1
        elif line.contains("ERROR"):
            error_count+=1
        elif line.contains("WARN"):
            warn_count+=1
    return info_count,error_count,warn_count 

# with open ("app.log","r") as file:
#     info_count,error_count,warn_count = analyze_log(file)
#     print(info_count,error_count,warn_count)


def get_error_counts(file):
    service_counts={}
    for line in file:
        parts = line.split()
        service_name = parts[3]
        service_counts[service_name] = service_counts.get(service_name,0)+1
        
    return service_counts    
        
def generate_alerts(error_counts, threshold):
    if error_counts > threshold:
        return True
    else:
        return False
    
with open ("app.log","r") as file:
    service_counts = get_error_counts(file)
    threshold = 3
    for service_name, count in service_counts.items():
        if generate_alerts(count, threshold):
            print(f"ALERT: {service_name} has {count} errors, which exceeds the threshold of {threshold}.")
        

def get_repeated_errors(file):
    repeated_errors={}
    for line in file:
        if "ERROR" not in line:
            continue
        parts = line.split()
        error = " ".join(parts[4:6])
        repeated_errors[error] = repeated_errors.get(error,0)+1
        
    return repeated_errors    
        

# with open ("app.log","r") as file:
#     repeated_errors = get_repeated_errors(file)
#     for repeated_errors, count in repeated_errors.items():
#         print(repeated_errors,count)

