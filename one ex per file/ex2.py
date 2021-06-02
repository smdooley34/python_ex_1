####################################################################################################
# ex2.py
#
# This file contains the solution to Homework One Exercise Two.
#
# Prompt:
#
#   Break an input sentence into sentences (which end in a .), count them, and print them out using a loop:
#
#     Input: Python is an interpreted, high-level, general-purpose programming language. Created by
#            Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code
#            readability with its notable use of significant whitespace. Its language constructs and
#            object-oriented approach aim to help programmers write clear, logical code for small and
#            large-scale projects.
#     Result: There are 3 sentences
#             Python is an interpreted, high-level, ge...
#             Created by Guido...
#             Its language constructs and...
#
####################################################################################################

print("----- Start Of Part 2 -----")
print("\n")

inputParagraph = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van" \
                 "Rossum and first released in 1991, Python's design philosophy emphasizes code readability with" \
                 "its notable use of significant whitespace. Its language constructs and object-oriented approach" \
                 "aim to help programmers write clear, logical code for small and large-scale projects."
print("Input Paragraph:", inputParagraph)

# This Would Certainly Be The Way I Would Do This... Use A Period As The Delimiter In Distinguishing Sentences
sentenceList = inputParagraph.split(".")
# We Will, However, Be Left With An Empty String As The Last Member Of The `sentenceList` Array, So We Remove It
sentenceList.pop()

# We Print The Number of Sentences Detected...
print("Number Of Sentences:", len(sentenceList))

# ... And We Also Print Each Of The Detected Sentences
index = 0
while index < len(sentenceList):
    print("Sentence ", index + 1, sentenceList[index] + ".")
    index += 1

print("\n")
print("----- End Of Part 2 -----")
