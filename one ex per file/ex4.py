####################################################################################################
# ex4.py
#
# This file contains the solution to Homework One Exercise Four.
#
# Prompt:
#
#   Abbreviate a potentially long string to have only the first x and last chars between "...".
#   Print out the abbreviation for values of x ranging from 5 to 15. Note there will be an issue
#   where the abbreviated result would actually be longer than(!) than the un-abbreviated version.
#   For these cases, do not perform your abbreviation. Optionally, write a general function
#   abbr(s, filler="...", total_width=15) which abbreviates the string to total_width chars and uses
#   the string filler in between them.
#
#     Input: abbr("A very long description", filler="...", total_width=5) => "A ver...ption"
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

# A Function To Abbreviate A String To A Specified Number Of Characters With A Specified Filler String
def abbr(sentence, filler, total_width):
    # Checks If The Abbreviation Would Be Longer Than The Original
    if total_width * 2 + len(filler) > len(sentence):
        return sentence
    # Otherwise We Insert A Filler String In The Sentence
    else:
        return sentence[0:total_width] + filler + sentence[-total_width:]


print("----- Start Of Part 4 -----")
print("\n")

customFiller = "..."
inputSentence = "A very long description"

# Tests Input For A Varying Total Specified Width
for width in range(5, 16):
    print("Width (x):", width, "Output:", abbr(inputSentence, customFiller, width))

print("\n")
print("----- End Of Part 4 -----")
