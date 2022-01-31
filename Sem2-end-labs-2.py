# Author: SMR (AMDG) 01/25/21
# Build a function that returns an array of integers from n to 1 where n>0.

# Definiing the function as reverse sequnce
def reverse_sequence(n):
# Returning a list of 5 range down     
    return list(range(n, 0, -1))
# Test Case of 5
sequence=reverse_sequence(5)
# Final print statement
print(sequence)