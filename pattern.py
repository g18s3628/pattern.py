#Assign the asterisk as a string and name variable 
#Use for loop and have range from 0 to 5 to print starts otherwise break loop once it prints 5 stars 
stars_up = "*"
for i in range(0 ,5):
    if i < 5:
        print(stars_up)
        stars_up += "*"
    else:
        break
    
#Assign four asterisks to a sting and name 
#Have the stars decend until there is one star then break loop
stars_down  = "****"
for i in range(0 ,4):
    if i < 4:
        down = 4 - i
        print(stars_down[0:down])
    else:
        break
