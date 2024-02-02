sentence = input("Enter a sentence: ")
sentence = sentence.split()  
x = len(sentence)
vowels = ["a","e", "i", "o", "u" ]

i = 0
while i < x:
  word = sentence[i]
  word = word.lower()
  letters = len(word)
  firstPart = ""
  secondPart = ""
  newWord = ""

  for char in word:
    if char in vowels:
      break
    else:
      firstPart += char

  secondPart = word[len(firstPart):]
  newWord = secondPart + firstPart + "ay"

  if word[0] in vowels:
    newWord = word + "hay"
  i+=1
  print(newWord, end = " ")
