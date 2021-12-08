def print_formatted(number):
    l = len(bin(int(number))[2:])
    for i in range(1, int(number)+1):
        print(str(i).rjust(l, ' '), oct(i)[2:].rjust(l, ' '), hex(i)[2:].upper().rjust(l, ' '), bin(i)[2:].rjust(l, ' '))


print_formatted(input())
