# Count words, characters, lowercase, uppercase and replace spaces

sentence = input("Enter a sentence: ")

print("Number of Words:", len(sentence.split()))
print("Number of Characters:", len(sentence))
print("Lowercase:", sentence.lower())
print("Uppercase:", sentence.upper())
print("With Underscores:", sentence.replace(" ", "_"))
