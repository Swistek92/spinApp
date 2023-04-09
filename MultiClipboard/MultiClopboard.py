
import sys
import clipboard
import json 

SAVED_DATA="clipboard.json"


def save_items(filepath, data):
# w == write
    with open(filepath, "w") as f: 
        json.dump(data, f)
    
# save_items("test.json", {"key":"value"})

def load_data(filepath):
    # r== read
    try:
        with open(filepath, "r") as f:
            data= json.load(f)
            return data
    except:
        return {}






# print(sys.argv[:1])

if len(sys.argv)==2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    # print(command)
    
    if command == "save":
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA ,data)
        print("Data saved!")
    elif command == "load":
        key = input("enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipoard")
        else:
            print("key does not exist")
    elif command == "list":
        print(data)
    else:
        print("unknow command")
else:
    print("please pass exctly one command.")


# data = clipboard.paste()

# print(data)


