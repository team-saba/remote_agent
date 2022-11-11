import docker

client = docker.from_env()

def print_list():
    containers = client.containers.list(all)
    containers_json = [container.attrs for container in containers]
    containers_result = []
    for container in containers_json:
        containers_result.append(
            {
                'idx' : containers_json.index(container),
                'CONTAINER_ID' : container['Id'],
                'Stack' : container['Path'],
                'Name' : container['Name'],
                'Created Time' : container['Created'],
                'Status' : container['State']['Status'],
                'IPAddress' : container['NetworkSettings']['IPAddress'],
                'Port' : container['NetworkSettings']['Ports'],
                'Image' : container['Image']
            }
        )
    return containers_result

def get_container(container_id):
    try:
        container = client.containers.get(container_id)
    except docker.errors.NotFound:
        return None
    return container

def start_container(container_id):
    container = get_container(container_id)
    if container is None:
        return None
    container.start()
    return container

def stop_container(container_id):
    container = get_container(container_id)
    if container is None:
        return None
    container.stop()
    return container

def restart_container(container_id):
    container = get_container(container_id)
    if container is None:
        return None
    container.restart()
    return container