def read_book(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    num_chars = {}
    for line in text.split():
        for c in line.lower():
            if c in num_chars:
                num_chars[c] += 1
            else:
                num_chars[c] = 1
    return num_chars

def sort_num_chars(num_chars):
    list_num_chars = []
    for key in num_chars:
        list_num_chars.append({"name": key, "count": num_chars[key]})
    list_num_chars.sort(key=lambda d: d["count"], reverse=True)
    return list_num_chars
