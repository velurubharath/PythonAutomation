import argparse
from sys import exception

parser = argparse.ArgumentParser()
parser.add_argument("logfile")
#parser.add_argument("threshold")
parser.add_argument("--threshold", type = int, default=3)
args = parser.parse_args()
threshold = int(args.threshold)


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

# with open ("app.log","r") as file:
#     info_count,error_count,warn_count = analyze_log(file)
#     print(info_count,error_count,warn_count)


def validate_line(line):
    parts = line.split()
    if len(parts) < 6:
        return False
    return True
  
        
def generate_alerts(error_counts, threshold):
    if error_counts > threshold:
        return True
    else:
        return False

def get_error_counts(file): 
    service_counts={}
    for line in file:
        if not validate_line(line):
            print(f"Warning: Invalid log line format: {line.strip()}")
            continue
        parts = line.split()
        service_name = parts[3]
        service_counts[service_name] = service_counts.get(service_name,0)+1
        
    return service_counts  
    
with open ("app.log","r") as file:
    service_counts = get_error_counts(file)
    #threshold = 3
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




# try:

#     with (open(args.logfile,"r")) as file:
#         print(get_error_counts(file))

# except FileNotFoundError:
#     print(f"Error: The file {args.logfile} was not found.")
#     exit(1)