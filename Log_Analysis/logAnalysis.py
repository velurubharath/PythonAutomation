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
        

with open ("app.log","r") as file:
    service_counts = get_error_counts(file)
    for service_name, count in service_counts.items():
        print(service_name, count)