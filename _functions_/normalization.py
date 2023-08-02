import json


def norm(string_list, file_slang):
    res = []
    with open(file_slang) as f:
        data = f.read()
        data = json.loads(data)
        for word in string_list:
            if word in data:
                word = data[word]
            else:
                word = word
            res.append(word)
    return res