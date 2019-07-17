v=['a','i','e','o','u']
c=input("enter a character ")
if(c.isalpha()):
    if(c in v):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
