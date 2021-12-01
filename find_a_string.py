def count_substring(string, sub_string):
    length = len(string)
    sub_len = len(sub_string)
    count = 0
    for i in range(0,length):
        if string[i:i + sub_len] == sub_string:
            count = count + 1
    return count
print(count_substring(input(),input()))

