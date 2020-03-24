#Guessing game using while loops


secret_number = 9
#i is the number of guesses users has made
i = 0
i_limit = 3
while i < i_limit:
   guess =  int(input('Guess: '))
   i +=1
   if guess == secret_number:
       print("You Won!")
       break
else:
    print("Sorry, you failed!")



