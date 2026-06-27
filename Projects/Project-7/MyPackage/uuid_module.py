import uuid

def UUID_Module():
    uid = uuid.uuid4()
    print("Generated UUID:", uid)

if __name__=="__main__":
    UUID_Module()