def encrypt_letters(message, key):
# convert inputs to uppercase
    message = message.upper()
    key = key.upper()
# convert inputs to corresponding letter values (0-25)
    message_number = [ord(letter) - 65 for letter in message if message.isupper()]
    key_number = [ord(letter) - 65 for letter in key if key.isupper()]
# repeat key to match length of message
    key_number = key_number * (len(message_number) // len(key_number) + 1)
    key_number = key_number [:len(message_number)]
# add both numbers
    encrypted_numbers = [(m + k) % 26 for m, k in zip(message_number, key_number)]
# convert encrypted numbers to corresponding letters (A-Z)
    ciphertext = ''.join([chr(value + 65) for value in encrypted_numbers])
# return/print value
    return ("Your ciphertext is: " + ciphertext)

# ask for input, then save
message = input("Enter a message: ")
key = input("Enter a key: ")

# call the function
ciphertext = encrypt_letters(message, key)

# turtle graphics for output
import turtle as t
import colorsys
wn = t.Screen()
wn.bgcolor("black")
wn.screensize(canvwidth=2000, canvheight=2000)
t.tracer(1000)
h = 0
t.pensize(1)
t.up()
for i in range(500):
  c = colorsys.hsv_to_rgb(h, 1, 1)
  h += 0.008
  t.pencolor(c)
  t.lt(i)
  t.fd(3)
  t.fd(5)               
  t.goto(-310, 100)      
  t.down()
  t.write(ciphertext, font = ("Times New Roman", 20))
  t.done