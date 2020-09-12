print("ugly language")

def giraffe_lang():
    word = list(input("Enter a word: ").lower())
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in range(len(word)):
        if word[i] in vowels:
            word[i] = 'G'
    print("your word is "+"".join(word).capitalize())

giraffe_lang()