import uuid

def generate_uuid4():
    print("The uuid is using uuid4 is:")
    print(uuid.uuid4())
    print("---------------------------------------------------------")



def generate_uuid3():
    namespace = uuid.NAMESPACE_DNS
    print("The uuid based on the given name using uuid3 is :\n")
    print(uuid.uuid3(namespace, "example.com"))
    print("---------------------------------------------------------")

def generate_uuid5():
    namespace = uuid.NAMESPACE_DNS
    print("The uuid based on the given name using uuid5 is :\n")
    print(uuid.uuid5(namespace, "example.com"))
    print("---------------------------------------------------------")






