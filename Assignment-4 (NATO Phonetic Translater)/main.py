


# Translater function 
def main(s):
    f = ""
    for ec in s: #traverse the string
        if ec == "a":
            c = "Alpha"
        elif ec == "b":
            c = "Bravo"
        elif ec == "c":
            c = "Charlie"
        elif ec == "d":
            c = "Delta"
        elif ec == "e":
            c = "Echo"
        elif ec == "f":
            c = "Foxtrot"
        elif ec == "g":
            c = "Golf"
        elif ec == "h":
            c = "Hotel"
        elif ec == "i":
            c = "India"
        elif ec == "j":
            c = "Juliett"
        elif ec == "k":
            c = "Kilo"
        elif ec == "l":
            c = "Lima"
        elif ec == "m":
            c = "Mike"
        elif ec == "n":
            c = "November"
        elif ec == "o":
            c = "Oscar"
        elif ec == "p":
            c = "Papa"
        elif ec == "q":
            c = "Quebec"
        elif ec == "r":
            c = "Romeo"
        elif ec == "s":
            c = "Sierra"
        elif ec == "t":
            c = "Tango"
        elif c == "u":
            c = "Uniform"
        elif ec == "v":
            c = "Victor"
        elif ec == "w":
            c = "Whiskey"
        elif ec == "x":
            c = "X-ray"
        elif ec == "y":
            c = "Yankee"
        elif ec == "z":
            c = "Zulu"
        elif ec ==" ":
            c = "  ---  " 
        else:
            c = ec

        if c == "  ---  " :
            c = "  --'SPACE'--  " 
        else:
            c = c
        
        ec = ec.upper()
        if c =="  --'SPACE'--  " :
            print()
            f = print(c)
            print()
        else:
            f = print(ec  ,"-",  c)
    



            #BIGINS PROGRAM
#welcome screen
print()
print("HELLO!")
print("Welcome to  NATO Phonetic Translator")
print()
print("Here you will be able to translate any word or sentence you want into NATO")
input("Click ENTER to Begin.")
print()

#Word/sentence input
print("👇 Enter the text you would like to translate 👇")
x = input("") 
x = x.lower()

# Gives the user the index for the output
print()
print()
print("----------------------------------------------------------------------------------")
print("               Index")
print(" '--'SPACE'--'   =     seperates words ")
print("----------------------------------------------------------------------------------")


print()
print()
print("👇 Here is the translated version 👇")
print()
# Calls the translater function 
main(x) 



print()
print()
#Thank you message
print("Thank you for using NATO Phonetic Translator!")
print()