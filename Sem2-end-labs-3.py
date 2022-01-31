# Author: SMR (AMDG) 01/25/21
# Kata forgets how to add two numbers together
# Defining the function taking up two different arguments which is the two numbers being added up with one another 
def add(a,b):
 # Creating whitespace  
    s = ""
  # Creating a while loop while addition is taking place  
    while a+b:
        
        a,c = divmod(a,10)
        
        b,d = divmod(b,10)
    # setting s equal to the string of c and d + s    
        s = str(c+d)+s
  # Returns the integer of s or 0  
    return int(s or'0')

# Testing with 16 and 18
test=add(16,18)

# Should print out 214
print(test)