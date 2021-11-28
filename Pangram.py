alphabets="abcdefghijklmnopqrstuvwxyz"
#x="The quick brown fox jumps over the lazy dog"
x='i love you vivek'
for letter in alphabets:
    if letter not in x.lower():
        print("the string is not a pangram")
        break
else:
    print("The string is pangram")
