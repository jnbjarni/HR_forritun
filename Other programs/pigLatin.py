original = input("Enter a word: ")
while original != ".":
    word = original.lower()
    first = word[0]
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        output = word + "yay"
        print(output)
        original = input("Enter a word: ")
    elif "a" in word or "e" in word or "i" in word or "o" in word or "u" in word:
        for i, c in enumerate(word):
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                output_start = word[0:i]
                output = word[i:] + output_start + "ay"
                print(output)
                original = input("Enter a word: ")
                break
    else:
        output = word + "ay"
        print(output)
        original = input("Enter a word: ")
