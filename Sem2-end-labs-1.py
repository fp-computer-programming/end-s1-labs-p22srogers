# Author: SMR (AMDG) 01/25/21
# Dividends without using the % command

# Defining Function
def remainder(dividend,divisor):
 # While the divisor is less than or equal to the dividend   
    while divisor <= dividend:
 # the dividend is equal to the divident - the divisor    
      dividend = dividend - divisor
 # Return the final dividend   
    return dividend
# Testing the function
fin_remainder=remainder(20,4)
# Displaying the final answer
print(fin_remainder)


