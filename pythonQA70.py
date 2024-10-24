# # Write a  Python program to get all possible two-digit letter combinations from a 1-9 digit string.

# string_maps = {
# "1": "abc",
# "2": "def",
# "3": "ghi",
# "4": "jkl",
# "5": "mno",
# "6": "pqrs",
# "7": "tuv",
# "8": "wxy",
# "9": "z"
# }


def let_comb(nums):
    if nums  == "":
        return []
    string_maps = {
            "1": "abc",
            "2": "def",
            "3": "ghi",
            "4": "jkl",
            "5": "mno",
            "6": "pqrs",
            "7": "tuv",
            "8": "wxy",
            "9": "z"
 
            }
    result =[""]
    for num in nums:
        temp =[]
        
        for letter in result:
            for char in string_maps[num]:
                temp.append(letter +char)
                result = temp
    return result
    
given_digit ='67'
print(let_comb(given_digit))
              
                
















#     result =[""]
#     for num in nums:
#             temp=[]
            
#             for bn in result:
#                 for char in string_maps[num]:
#                     temp.append(bn +char)
#                     result = temp
#     return result
# digit_str ='25'
# print(let_comb(digit_str))
        
                