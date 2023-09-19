sequences = [
    [2, 3, 4], [2, 3, 5], [2, 3, 10], [2, 3, 11], [2, 3, 12], [2, 3, 13],
    [2, 4, 5], [2, 4, 10], [2, 4, 11], [2, 4, 12], [2, 4, 13],
    [2, 5, 10], [2, 5, 11], [2, 5, 12], [2, 5, 13],
    [2, 10, 11], [2, 10, 12], [2, 10, 13],
    [3, 4, 5], [3, 4, 10], [3, 4, 11], [3, 4, 12], [3, 4, 13],
    [3, 5, 10], [3, 5, 11], [3, 5, 12], [3, 5, 13],
    [3, 10, 11], [3, 10, 12], [3, 10, 13],
    [4, 5, 10], [4, 5, 11], [4, 5, 12], [4, 5, 13],
    [4, 10, 11], [4, 10, 12]
]

characters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

combinations = {character: sequence for character, sequence in zip(characters, sequences)}


def get_charcter(pressedKeys):
    matched_character = None

    for char, seq in combinations.items():
        if pressedKeys == seq:
            matched_character = char
            break

    if matched_character:
        print("Matched Character:", matched_character)
    else:
        print("No match found.")
pressedKeys = list(map(int, input().strip().split()))
print(pressedKeys)
get_charcter(pressedKeys)

