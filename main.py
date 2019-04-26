import json
import os
from config import PROJECT_ROOT
from lib.IdiomsLexicon.IdiomsDict import get_idioms_json
from lib.SearchByPinyin.Search import search_by_pinyin

with open(os.path.join(os.path.abspath(PROJECT_ROOT), "data/chinese-xinhua/data/idiom.json"), "rb") as json_file:
    content = json.load(json_file)
# Dict with idioms info.
idioms_dict = get_idioms_json(content)

with open(os.path.join(os.path.abspath(PROJECT_ROOT), "data/elements-pinyin/data/elements.json"), "rb") as json_file:
    content = json.load(json_file)
# Dict with elements info.
elements_dict = get_idioms_json(content)

list_out = search_by_pinyin(idioms_dict, elements_dict)
# for item in list_out:
#     print("{}\t{}\n".format(item[1],item[2]))

with open("OUTPUT","w",encoding='utf-8') as F:
    for item in list_out:
        F.write("{}\t{}\t{}\n".format(item[1],item[2],item[3]))
