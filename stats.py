def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    chars = {}
    for c in text:
        low = c.lower()
        if low in chars:
            chars[low] += 1
        else:
            chars[low] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(item):
    return item["num"]

def get_book_report(char_counts):
    report_list = []
    
    for char, count in char_counts.items():
        if char.isalpha():
            report_list.append({"char": char, "num": count})
            
    report_list.sort(reverse=True, key=sort_on)
    
    return report_list