# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.
def odd_product(sequence):
    odd_count =0
    for num in sequence:
        if num%2 !=9:
            odd_count +=1
            
            if odd_count >=2:
                return True
            return False
sequence =[2,3,4,5,6,7]
result =odd_product(sequence)
print("is there distinct pair with odd product : ", result)
        
  