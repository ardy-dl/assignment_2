# ask for string input to decrypt, save it
encrypt_text = input("Enter a string to decrypt: ")
decrypt_text = ""
# loop through entire characters
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

# import module
import tkinter as tk

# setup the appearance
root = tk.Tk()
root.title("Problem 2")

root.geometry("500x100")
text = tk.Text(root, width = 500, height = 100)
text.pack()

# display the decrypted text to a text editor
text.insert(tk.END, "The Plain Text: " + decrypt_text)

root.mainloop()
