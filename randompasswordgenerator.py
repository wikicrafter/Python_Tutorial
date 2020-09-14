import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(33,125)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(33,125))
uppercaseLetter3=chr(random.randint(33,125))#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter4=chr(random.randint(33,125)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter5=chr(random.randint(33,125))
uppercaseLetter6=chr(random.randint(33,125))#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter7=chr(random.randint(33,125)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter8=chr(random.randint(33,125))
uppercaseLetter9=chr(random.randint(33,125))#Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + uppercaseLetter7 + uppercaseLetter8 + uppercaseLetter9 # + ....
password = shuffle(password)

#Ouput
#it's basically impossible to generate same pwd and u can use it even etand 
print(password)