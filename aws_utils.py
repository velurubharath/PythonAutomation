def get_instance_count(client):
    total_instances = 0

    response = client.describe_instances()

    while True:
        for reservation in response.get("Reservations", []):
            instances = reservation.get("Instances", [])
            total_instances += len(instances)

        next_token = response.get("NextToken")

        if not next_token:
            break

        response = client.describe_instances(
            NextToken=next_token
        )

    return total_instances
