def solve(s):
    str = s.split(' ')
    new = ' '.join(word.capitalize() for word in str)
    print(new)
solve(input())
