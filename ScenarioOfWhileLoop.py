#Program that asks user to enter a number until it matches the secret number
#Module3 line 616
#variable to store secret number chosen by the magician

#here the magician has chosen the secret number as 13

secret_number = 2020

#variable to store the number chosen by the user

guess = -1

#while loop that iterates until secret number is guessed

while secret_number != guess:

    #prompt the user to enter an integer

    guess = int(input("Enter an integer number: "))

    #if user chooses a wrong number

    if guess != secret_number:

      #print the message

      print("Ha ha! You're stuck in my loop!. Try again!")

#correct guess

if secret_number == guess:

    #print the message

    print ("Well done, muggle! You are free now")      

#end program