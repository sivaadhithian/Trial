x=str(input("enter the word"))
y=['a','e','i','o','u','A','E','I','O','U']
count1=0
count2=0
for i in x:
    if i in y:
        count1+=1
    else:
        count2+=1
print("number of vowels",count1)
print("number of consonants",count2)
