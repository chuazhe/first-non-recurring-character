inputString=input("Please enter the string:")

charList=[]
for i,char in enumerate(inputString):
    if char in charList:
        charList.remove(char)
    else:
        charList.append(char)

if not charList:
    print("No non reccuring character!")
else:
    print("The first non recurring character is "+charList[0])





