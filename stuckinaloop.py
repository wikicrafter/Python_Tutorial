secret_word = ""
while True:
    secret_word = input("You're stuck in an infinite loop!\nEnter a secret word to leave the loop.")
    if secret_word == "chupacabra":
        print("You've successfully left the loop.")
        break