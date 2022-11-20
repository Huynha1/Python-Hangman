# 3 hours of my life gone :(

import random

def stages(count):
    '''
    print("------------")
    print("|       |")
    print("|       |")
    print("|       O")
    print("|      /|\ ")
    print("|       |")
    print("|      / \ ")
    print("|___________") '''

    stage1 = "\n\n\n\n\n\n\n___________"

    stage2 = """
    |
    |
    |
    |
    |
    |
    |___________"""

    stage3 = """
    ------------
    |
    |
    |
    |
    |
    |
    |___________"""

    stage4 = """
    ------------
    |       |
    |       |
    |
    |
    |
    |
    |___________"""

    stage5 = """
    ------------
    |       |
    |       |
    |       O
    |
    |
    |
    |___________"""

    stage6 = """
    ------------
    |       |
    |       |
    |       O
    |      /|\ 
    |
    |
    |___________"""

    stage7 = """
    ------------
    |       |
    |       |
    |       O
    |      /|\ 
    |       |
    |      / \ 
    |___________"""

    if count == 0:
        return "\n\n\n\n\n\n\n\n"
    elif count == 1:
        return stage1
    elif count == 2:
        return stage2
    elif count == 3:
        return stage3
    elif count == 4:
        return stage4
    elif count == 5:
        return stage5
    elif count == 6:
        return stage6
    elif count == 7:
        return stage7 # this feels kinda messed up

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def guess(Word, Input, Letters, Hidden, Count):

    if len(Input) == 1: # This is completely unecessary but i cbs removing it
        if Input in Word.lower(): 

            if Word.lower().count(Input) == 1: # If the letter only appears once in the word
                if Word.lower().index(Input) == 0 or Word.lower()[Word.lower().index(Input) - 1] == " ": # If the letter is at the start of a word then its an upper case
                    Hidden[Word.lower().index(Input)] = Input.upper() # Replace the "-" in the list with a letter
                else:
                    Hidden[Word.lower().index(Input)] = Input

            elif Word.lower().count(Input) > 1: # If the letter appears more than once in the word
                for i in find(Word.lower(), Input): # this find() function finds the indexes that the letter appears in the word
                    if i == 0 or Word[i - 1] == " ":
                        Hidden[i] = Input.upper()
                    elif i != 0:
                        Hidden[i] = Input
            
            Letters.remove(Input.upper())
        
        else: 
            Letters.remove(Input.upper())
            print("\nIncorrect")
            Count += 1
                        
    return Word, Input, Letters, Hidden, Count

words = [
    ["Lamborghini", "Ferrari", "Mercedes", "Toyota", "Honda", "Bugatti", "Lexus", "Acura", "Nissan", "Ford", "Mazda", "Mitsubishi", "BMW", "Porsche", "Volvo", "Holden", "Jaguar", "Kia", "Fiat", "McLaren", "Renault"],
    ["Apple", "Microsoft", "Dell", "Asus", "Intel", "Amd", "Nvidia", "Logitech", "Razer", "Steel Series", "Google", "Adobe", "Python", "Java", "Chrome", "Corsair", "Ducky", "Facebook", "Netflix", "Samsung", "BenQ"],
    ["Australia", "United States of America", "China", "Vietnam", "Japan", "India", "Italy", "Egypt", "Canada", "New Zealand", "South Africa", "Brazil", "Argentina", "France", "Germany", "Russia", "Spain", "Cambodia", "Finland", "Sweden", "Netherlands", "United Kingdom"]
]
# The above list is a list of words duh

count = 0
# This counts how many times you get an incorrect letter, if it hits 7 he dead

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# The alphabet duh. Once you guess a word it gets removed form this list

SelectedWord = random.choice(random.choice(words)) # Selects a random word from the words list

Category = ""

if SelectedWord in words[0]:
    Category = "Cars"
elif SelectedWord in words[1]:
    Category = "Tech Brands/Companies"
elif SelectedWord in words[2]:
    Category = "Countries"
HiddenWord = [] # This list is going to be a string where the characters in the selected word are replaced with "-", I might change it idk

for i in SelectedWord:
    if i != " ":
        HiddenWord.append("-") # letters are "-"
    else:
        HiddenWord.append(" ") # white space is white space

while 1 > 0: # INFINITE LOOOOOOOOOOP
    
    print("\nThe category is {}".format(Category))

    if count != 7:
        print("the word is: {}".format("".join(HiddenWord))) # Print the blank word
    else:
        print("\nthe word is: {}".format(SelectedWord))
        
    print() # Resurrects Nelson Mandela

    print(stages(count)) # Print the different stanges of hang depending on what count is

    print("\nLetters left: {}".format(" ".join(Letters))) # Print the numbers of letters left
 
    if count == 7:
        print("F... he died")
        break
    elif "-" not in "".join(HiddenWord): 
        print("\n**** NICE ONE MATE YOU SAVED HIM **** \n")
        
        break

    print("Guess Letter or Word\nType \"End\" to end")
    
    Input = input()

    if Input.lower() == "end":
        break

    if len(Input) == 1:
        if Input.upper() in Letters:
            SelectedWord, Input, Letters, HiddenWord, count = guess(SelectedWord, Input.lower(), Letters, HiddenWord, count)
        else:
            print("\nYou already guessed this letter, try again")
            continue

    elif len(Input) > 1:
        if Input.lower() == SelectedWord.lower():
            print("\n**** NICE ONE MATE YOU SAVED HIM **** \n")
            break
        else:
            print("\nBRO YOU JUST KILLED HIM, THE WORD WAS {}".format(SelectedWord))
            
            break

#there's so much shit i can clean up but cbs