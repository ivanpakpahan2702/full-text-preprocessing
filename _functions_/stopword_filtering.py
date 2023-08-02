def stop(string_list, file_stop):
    res = []
    with open(file_stop) as f:
        data = f.read()
        for word in string_list:
            print(word)
            if word not in data:
                res.append(word)
    return res