def minion_game(string):
    # your code goes here
    vowel = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowel:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print('Kevin {0}'.format(kevin))
    elif kevin < stuart:
        print('Stuart {0}'.format(stuart))
    else:
        print('Draw')


s = input()
minion_game(s)