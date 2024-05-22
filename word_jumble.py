import random
WORDS=("python","jumble","easy","difficult","answer","xylophone")
word=random.choice(WORDS)
correct=word
jumble=""
while word:
      position=random.randrange(len(word))
      jumble+=word[position]
      word=word[position]+word[(position+1):]

print(""" Welcome to word jumble!!!
          
          Unscramble the letters to make a word.
          (press the enter key to prompt  to quit.)""")
print("The jumble is:",jumble)

