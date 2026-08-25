pods = [
    {"name": "payment-api-1", "namespace": "prod", "restarts": 12, "status": "Running"},
    {"name": "payment-api-2", "namespace": "prod", "restarts": 0, "status": "Running"},
    {"name": "checkout-api-1", "namespace": "prod", "restarts": 7, "status": "Running"},
    {"name": "inventory-api-1", "namespace": "prod", "restarts": 15, "status": "CrashLoopBackOff"},
    {"name": "frontend-1", "namespace": "dev", "restarts": 2, "status": "Running"},
    {"name": "worker-1", "namespace": "dev", "restarts": 9, "status": "Running"},
    {"name": "worker-2"}
]

##Function for getting pods with high restarts based on a threshold
def get_high_restart_pods(pods, threshold):
    high_restart_pods = []
    for pod in pods:
        if pod["restarts"] > threshold:
            high_restart_pods.append(pod)
    return high_restart_pods

##Definition for getting pods with high restarts with a fixed threshold of 5
def high_restart_pod(pods):
    high_restarts_pods = []
    for pod in pods:
        if pod["restarts"] > 5:
            high_restarts_pods.append(pod)
    return high_restarts_pods


#Definition for getting the pod with the highest restarts
def get_highest_restart_pods(pods):
    highest = pods[0]
    
    for pod in pods:
        if pod["restarts"] > highest["restarts"]:
            highest = pod
    return highest

#Definition for getting the count of pods based on their status
def get_status_count(pods):
    status_counts = {}
    for pod in pods:
        status = pod["status"]
        
        if status not in status_counts:
            status_counts[status] = 0
            
        status_counts[status]+=1
    return status_counts

#Definition for getting the count of restarts per namespace
def get_namespace_restart_counts(pods):
    namespace_restarts = {}
    
    for pod in pods:
        namespace = pod["namespace"]
        
        if namespace not in namespace_restarts:
            namespace_restarts[namespace]=0
        
        namespace_restarts[namespace]+=pod["restarts"]
    return namespace_restarts

def check_alert(pods):
    for pod in pods:
        if pod["restarts"] > 10 or pod["status"] == "CrashLoopBackOff" :
            print(f"ALERT: {pod['name']} requires investigation")


#Validate if the pod has all the required fields
def validate_pod(pod):
    required_fields = ["namespace","status","restarts","name"]
    
    for field in required_fields:
        if field not in pod:
            return False
            
    return True

#Process pods to get counts of statuses and namespaces with default values for missing fields
def process_pods(pods):
    status_counts = {}
    namespace_counts = {}
    
    for pod in pods:
        status = pod.get("status","unknown")
        namespace = pod.get("namespace","default")
        restarts = pod.get("restarts",0)
        
        status_counts[status] = status_counts.get(status,0)+1
        namespace_counts[namespace] = namespace_counts.get(namespace,0)+1
        
    return status_counts, namespace_counts


def get_health_status(pod):
    status = pod.get("status","unknown")
    restarts = pod.get("restarts",0)

    if not validate_pod(pod) or status.lower() == "unknown":
        return "INVALID"

    if status == "CrashLoopBackOff" or restarts > 10:
        return "CRITICAL"
    elif restarts  > 5:
        return "WARNING"
    else:
        return"HEALTHY"
    

for pod in pods:
    health = get_health_status(pod)
    name = pod.get("name", "unknown")
    print (f" {name}  {health}")

# for pod in pods:
#     if not validate_pod(pod):
#         print (f"Pod name {pod['name']} has improper data")
    
# for pod in pods:
#     if not validate_pod(pod):
#         print(f" Pod {pod['name']} has not proper data")
#check_alert(pods)

# status_counts = get_status_count(pods)

# print(status_counts)

# for status,count in status_counts.items():
#     print(status,count)
    
# highest_restart_pod = get_highest_restart_pods(pods)
# print(highest_restart_pod["name"] , highest_restart_pod["restarts"])

# high_restarts_pods = high_restart_pod(pods)

# print("Pods with high restarts:")
# for pod in high_restarts_pods:
#      print(pod["name"], pod["restarts"])



# print("Name of pods: ")
# for pod in pods:
#     print(pod["name"])

