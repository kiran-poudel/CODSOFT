import random,string

print("Hello, welcome to password generator")
length = int(input('Enter the length of password:'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

sample = random.sample(all,length)
password = "".join(sample)
print(password)
