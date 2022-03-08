# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

import csv


with open("201-lab/03_file-input-output/words.txt", "r") as file:
    # word_list = file.readlines().replace("\n", "")
    
    words = file.read().splitlines()
    # print(words)

    shortest = min(words, key=len)
    print(shortest)

    longeest = max(words, key=len)
    print(longeest)

    print(len(words))




