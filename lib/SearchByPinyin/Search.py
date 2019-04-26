from config import MATCH_LEVEL, OUTPUT_PATTERN


def search_by_pinyin(idioms, elements):
    """

    :param idioms: A list of Dict with "derivation", "example", "explanation", "pinyin", "word" and "abbreviation".
    :param elements: A list of Dict with "pinyin", "elements" and "number".
    :return:
    """
    el_pin = elements["pinyin"]  # elements_pinyin
    id_pin = idioms["pinyin"]
    match_list = []
    # Critical
    if MATCH_LEVEL == "All":
        for index, item in enumerate(id_pin):
            flag = 0
            templist = ""
            for words in item.split(" "):
                if words not in el_pin:
                    flag = -1
                    break
                if words in el_pin:
                    templist+=elements["elements"][el_pin.index(words)]
            if flag == 0:
                match_list.append([item, idioms["word"][index], templist,idioms["explanation"][index]])
        return match_list
    # Loose
    if MATCH_LEVEL == "NoNeedTone":
        pass  # TODO(yanbohan98@gmail.com): Different match patterns need.
