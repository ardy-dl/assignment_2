# pseudocode
# ask for string input to decrypt, save it
encrypt_text = input("Enter a string to decrypt: ")
decrypt_text = ""
# loop through entire character
for char in encrypt_text:
#   if * change to a
    if char == "*":
        decrypt_text += "a"
#   if & change to e
    elif char == "&":
        decrypt_text += "e"
#   if # change to i
    elif char == "#":
        decrypt_text += "i"
#   if + change to o
    elif char == "+":
        decrypt_text += "o"
#   if ! change to u
    elif char == "!":
        decrypt_text += "u"
    else:
        decrypt_text += char
# print the output
print("The Plain Text:", decrypt_text)
