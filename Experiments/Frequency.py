#Count Word and character frequency

text = input("Enter a string: ")

#Word Count
words = text.lower().split()
word_frequency = {}
total_words = 0
for word in words:
    word_frequency[word] = word_frequency.get(word,0)+1
    total_words += 1
print("\nWord Frequency:",total_words)
for word,count in word_frequency.items():
    print(word,":",count)

#Character Frequency
character_frequency = {}
total_characters = 0
for character in text:
    total_characters += 1
    if character!=" ":
        character_frequency[character] = character_frequency.get(character,0)+1
print("\nCharacter Frequency:",total_characters)
for character,count in character_frequency.items():
    print(character,":",count)