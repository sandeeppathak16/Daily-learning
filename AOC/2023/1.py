def solve(filename="1.txt", part1=True):
    with open(filename) as f:
        lines = [line.strip() for line in f]

    WORD_TO_DIGIT = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    WORDS = sorted(WORD_TO_DIGIT.keys(), key=len)

    def find_first_value(text):
        for i in range(len(text)):
            if text[i].isdigit():
                return text[i]

            if not part1:
                for word in WORDS:
                    if text[i:].startswith(word):
                        return WORD_TO_DIGIT[word]

    def find_last_value(text):
        for i in range(len(text) - 1, -1, -1):
            if text[i].isdigit():
                return text[i]

            if not part1:
                for word, digit in WORD_TO_DIGIT.items():
                    start = i - len(word) + 1
                    if start >= 0 and text[start:i + 1] == word:
                        return digit

    total = 0

    for line in lines:
        first = find_first_value(line)
        last = find_last_value(line)
        total += int(first + last)

    return total