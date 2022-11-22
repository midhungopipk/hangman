f = open('dict.txt')
no_of_guesses = int(input('Number of guesses?'))
length_ofWord = int(input('Length of the word?'))
dict_updated = []

for e in f:
    if '\n' in e:
        if len(e.strip()) == length_ofWord:
            dict_updated.append(e.strip())
    else:
        if len(e) == length_ofWord:
            dict_updated.append(e)

word = []
words = []


def find_match(ch, i):
    if len(word) == 0:
        word.append(ch)
        for e in dict_updated:
            if ch == e[i] and len(e) == length_ofWord:
                words.append(e)
                print(''.join(word), (length_ofWord-len(word))*'_ ')
    else:
        word.append(ch)
        for l in words:
            a = slice(len(word))
            if ''.join(word) == ''.join(list(l)[a]):
                print(''.join(word), (length_ofWord-len(word))*'_ ')
                break
            else:
                continue
        else:
            word.pop()
            print('NOT LUCKY!')


for k in range(no_of_guesses):
    if len("".join(word)) == length_ofWord:
        print('YOU HAVE WON.')
        break
    elif len(words) != 0:
        l = input("Guess the Letter? ")
        find_match(l, k)
    else:
        print('There is no word in the dictionary with this length!')
        break
