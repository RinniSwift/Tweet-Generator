import sys


def autocomplete():

    with open('/usr/share/dict/words', 'r') as f:
        file_content = f.read()
    lines = file_content.split()

    matched_items = []
    letter = sys.argv[1]

    while (len(matched_items) != 10):
        for word in lines:
            if word.startswith(letter):
                matched_items.append(word)
            if len(matched_items) == 10:
                break
        
    return matched_items


if __name__ == "__main__":
    print(autocomplete())