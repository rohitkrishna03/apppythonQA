def decimal_to_hex(decimal_nums):
    digits ="0123456789ABCDEF"
    x=(decimal_nums % 16)
    rest_part =decimal_nums //16
    if(rest_part == 0):
        return digits[x]
    return decimal_to_hex(rest_part)+digits[x]
decimal_nums = [0,15,30,55,355,656,896,1125]
print("decimal numbers: ")
print(decimal_nums)

print("hexadecimal numbers of the said decimal numbers : ")
print([decimal_to_hex(x) for x in decimal_nums])
