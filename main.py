import requests as r
import json

url = "https://api.fbi.gov"

def _is_list(obj):
    return type(obj) is list

def _is_dict(obj):
    return type(obj) is dict

def most_wanted():
    rt = "/wanted/v1/list"

    data = json.loads(r.get(f"{url}{rt}").text)

    def iterate_dict(key, theDict):
        print(f"{key} :\n")
        for key2,val2 in theDict.items():
            print(f"\t{key2} : {val2}")
        print("\n")

    def iterate_list(key, theList):
        print(f"{key} :\n")
        for i in theList:
            if _is_dict(i):
                iterate_dict(key, i)
            else:
                print(f"\t{val}")
        print("\n")

    for crook in data['items']:
        print(f"==== FBI POSTING FOR: {crook['title']} ====")
        for key,val in crook.items():
            if _is_list(val):
                iterate_list(key, val)
            elif _is_dict(val):
                iterate_dict(key, val)
            else:
                print(f"{key} : {val}")
            
        print("==== END OF POST ====")

if __name__ == "__main__":
    most_wanted()

