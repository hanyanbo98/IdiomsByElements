

"""
Decode the .json files of idioms to lists.
"""


def get_idioms_json(json_object):
    idioms_dict = {}
    for keys, item in json_object[0].items():
        idioms_dict[keys] = []
    for items in json_object:
        for keys, item in items.items():
            idioms_dict[keys].append(item)
    return idioms_dict

if __name__ == "__main__":
    import json
    import os
    from config import PROJECT_ROOT
    with open(os.path.join(PROJECT_ROOT,"data/chinese-xinhua/data/idiom.json"),"rb") as json_file:
        content = json.load(json_file)
    print(get_idioms_json(content))