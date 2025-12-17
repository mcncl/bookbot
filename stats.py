def word_count(extract):
    count = len(extract.split())
    return f"Found {count} total words"


def character_count(extract):
    stripped_extract = extract.lower().strip()
    letter_counts = {}
    for letter in stripped_extract:
        if not letter.isalpha():
            continue
        elif letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    return letter_counts

def sort_on(items):
    return items["num"]

def sort_counts(character_counts):
    character_dicts = []
    for entry in character_counts:
        character_dicts.append({"char": entry, "num": character_counts[entry]})
    character_dicts.sort(reverse=True, key=sort_on)
    return character_dicts
