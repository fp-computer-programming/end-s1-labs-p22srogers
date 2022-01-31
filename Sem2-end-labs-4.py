# Author: SMR (AMDG) 01/25/21
'''The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.'''

# First defining the function
def open_senior(data):
# Creating a blank list    
    rest = []
# For loop.   
    for index in data:
# If the Index of 0 is greater or equal to 55 and index of 1 is greater than 7 than appened Senior    
      if index[0] >= 55 and index[1] > 7:
        rest.append("Senior")
# If not then append Open     
      else:
        rest.append("Open")
    return rest
# Final Test Case
new=open_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])

print(new)
