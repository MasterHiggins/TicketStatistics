#Program written to correct words to contain ones with only valid characters
#Written by Chris H.

#Invalid Characters
InvalidCharacters = [
    ",",
    "<",
    ">",
    ".",
    "/",
    "?",
    ";",
    ":",
    "[",
    "{",
    "}",
    "]",
    " ",
    "|",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "'",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"
]

#Emptying the file
Modifying = open("Libraries\\Dictionary.txt", "w")
Modifying.close()

#Readying the append and file reading
Modifying = open("Libraries\\Dictionary.txt", "a")
Source = open("Libraries\\WordsBackup.txt", "r")

#Writing and modifying appropriate words to all caps in the modified file
for Word in Source:
    Word = Word.strip()
    Word = Word.upper()
    if any(Letter in Word for Letter in InvalidCharacters) == False and len(Word) < 11:  #Length of words cannot exceed 11 characters
        Modifying.write(Word + "\n")
    
#Closing it all
Modifying.close()
Source.close()
