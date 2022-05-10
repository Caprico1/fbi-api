import requests as r
import json

url = "https://api.fbi.gov"


def _is_list(obj):
    if type(obj) is list:
        return True
    return False

def _is_dict(obj):
    if type(obj) is dict:
        return True
    return False

def most_wanted():
    rt = "/wanted/v1/list"

    data = json.loads(r.get(f"{url}{rt}").text)


    for crook in data['items']:
        print(f"==== FBI POSTING FOR: {crook['title']} ====")
        for key,val in crook.items():
            if _is_list(val):
                print(f"{key} :\n")
                for i in val:
                    if _is_dict(i):
                        for key2,val2 in i.items():
                            print(f"\t{key2} : {val2}")
                    else:
                        print(f"\t{val}")
                print("\n")
            elif _is_dict(val):
                print(f"{key} :\n")
                for key2,val2 in val.items():
                    print(f"\t{key2} : {val2}")
                print("\n")
            else:
                print(f"{key} : {val}")
            
        print("==== END OF POST ====")




def main():

    most_wanted()

if __name__ == "__main__":
    main()

