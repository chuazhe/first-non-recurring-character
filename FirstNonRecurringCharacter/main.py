inputString=input("Please enter the string:")
resultASCIICode=-1

# initialise the count of the array of size 256 to 0
# because the character is 0-255 only
count=[0]*256

#Start and calculate the count of character of the string
for char in inputString:
    # ord: Cnvert the character to its ascii code, for example a->97
    count[ord(char)]+=1

# Start finding the first non recurring character
for char in inputString:
    if count[ord(char)] == 1:
        resultASCIICode=ord(char)
        break

if resultASCIICode == -1:
    print("No non reccuring character!")
else:
    # chr: Convert the ascii code to character
    print("The first non recurring character is "+chr(resultASCIICode))



