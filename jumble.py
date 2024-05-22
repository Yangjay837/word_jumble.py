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
guess=input("\n Enter Your Guess:")
while guess != correct and guess !="":
        print('sorry,that is not correct.')
        guess=input("\n Enter your guess again:")
        if guess==correct:
            print("That is it! You guessed it !/n")
            print ("Thanks for playing")
            
