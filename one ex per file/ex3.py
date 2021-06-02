####################################################################################################
# ex3.py
#
# This file contains the solution to Homework One Exercise Three.
#
# Prompt:
#
#   Break an input sentence into words (separated by a space). Print them out so that every second
#   word is in full uppercase. Optionally remove all periods and commas.
#
#     Input: Python is an interpreted, high-level, general-purpose programming language.
#     Result: Python
#             IS
#             an
#             INTERPRETED
#             high-level
#             GENERAL-PURPOSE
#             programming
#             LANGUAGE
#
####################################################################################################

print("----- Start Of Part 3 -----")
print("\n")

inputSentence = "Python is an interpreted, high-level, general-purpose programming language."
print("Input Sentence:", inputSentence)

# Use A Space As The Delimiter In Distinguishing Words
wordList = inputSentence.split()

index = 0
upperCaseWord = False
while index < len(wordList):
    # First, We Remove Any Periods Or Commas From The Word
    wordList[index] = wordList[index].replace(".", "")
    wordList[index] = wordList[index].replace(",", "")

    # Then, We Print The Word As Uppercase If Needed And As Normal Otherwise
    print("Word ", index + 1, wordList[index].upper()) if upperCaseWord else print("Word ", index + 1, wordList[index])

    index += 1
    upperCaseWord = not upperCaseWord

print("\n")
print("----- End Of Part 3 -----")
