import random
 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "<>,.?/:;{}[]+=_-()*&^%$#@!"
length = 12 
all = lower + upper + numbers + symbols
password = "".join(random.sample(all,length))

print("Here you go!" + password)
 