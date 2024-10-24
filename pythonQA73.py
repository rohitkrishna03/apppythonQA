# Write a  Python program to get all strobogrammatic numbers that are of length n.

# A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears the same when rotated 180 degrees. In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).

# For example,
# Given n = 2, return ["11", "69", "88", "96"].
# Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']

def sobo_gram(n):
    result = helper(n,n)
    return result
def helper(n, length):
     if n == 0:
         return [""]
     if n ==1:
         return ["1","0","8"]
     middles = helper(n-2,length)
     result =[]
     for middle in middles:
        # If 'n' is not equal to the original length, add "0" on both sides.
        if n != length:
            result.append("0" + middle + "0")
            # Add strobogrammatic numbers with "8" in the middle.
            result.append("8" + middle + "8")
            # Add strobogrammatic numbers with "1" in the middle.
            result.append("1" + middle + "1")
            # Add strobogrammatic numbers with "9" in the first half and "6" in the second half.
            result.append("9" + middle + "6")
            # Add strobogrammatic numbers with "6" in the first half and "9" in the second half.
            result.append("6" + middle + "9")
     return result
print("n =1: \n", sobo_gram(1))
print("n =2: \n", sobo_gram(2))
print("n =3: \n", sobo_gram(3))

    