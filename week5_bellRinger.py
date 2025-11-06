# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
# a. Retrieve the 5th character.
fifth_char = print(magic[4])
# b. Retrieve the second to last character.
second_to_last_char = print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
first_c_index = print(magic.index('c'))
last_a_index = print(magic.rindex('a'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
hij = print(alphabet.index('hij'))
hij2 = print(alphabet[7:10])
# c. Reverse the entire string using slicing.
every_second = print(alphabet[0:13:2])
# Problem Set 2: Extracting Information
reversed_alphabet = print(alphabet [ : : -1])
i_have_a_dream = "And when this happens, and when we allow freedom ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual"

reversed_i_have_a_dream = print(i_have_a_dream [: : -1])
# From Descriptions:
famous_quote = "Ask not what your country can do for you - ask what you can do for your country, - John F Kennedy"

john_f_kennedy =print(famous_quote.find("john f. kennedy"))

extracted_name = print(famous_quote[98:])
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

# Manipulating Words:

# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
phrase1 = "Python is fun. fun is good. good is subject."
# b. Extract every third word.
subjective =print(phrase1.find("subjective"))
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
every_3rd_word = print(phrase1 [::2])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
motto = ["Make", "haste", "slowly."]

# a. Convert the list into a single string.
motto_str = " ".join(motto)
print("Joined string:", motto_str)

# b. Now, split the string at every occurrence of the letter 'a'.
split_motto = motto_str.split('a')
print("String split at 'a':", split_motto)


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
sentence = "Life is what happens when you are busy making other plans."

# a. Replace "busy" with "distracted".
sentence = sentence.replace("busy", "distracted")

# b. Replace "plans" with "mistakes".
sentence = sentence.replace("plans", "mistakes")
print("Modified sentence:", sentence)


# Problem Set 4: String Properties and Advanced Operations

# Repetition:
# Concatenate the word "Iteration" 7 times.
word = "Iteration"
repeated_word = word * 7
print("Repeated word:", repeated_word)


# Word Search:
# Check if the word "moonlight" appears in the quote.
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
contains_moonlight = "moonlight" in quote
print("Contains 'moonlight'?", contains_moonlight)


# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation)
phrase = "Supercalifragilisticexpialidocious"
num_characters = len(phrase)

# b. Count the number of times the letter 'i' appears
i_count = phrase.count('i')

print("Number of characters:", num_characters)
print("Number of 'i's:", i_count)