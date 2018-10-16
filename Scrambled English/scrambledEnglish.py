import string
# build_wordlist() function goes here


def build_wordlist(filepath):
    a_list = []
    for line in filepath:
        for word in line.split():
            a_list.append(word)
    return a_list


# find_unique() function goes here
def find_unique(wordlist):
    unique_words = [
        x for x in wordlist if x not in string.punctuation and x != " "]
    uniq = sorted(set(unique_words))
    return uniq


def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)
    infile.close()
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)


main()
