import random
import string 

length=int(input("Enter the length of the password: ")) 
def password_generator(length):
    characters=string.asscii_letters+string.digits+string.punctuation 
    password = ''.join([random.choice(characters) for i in range(length)])
        return password

password=password_generator(length)
print("Generated Password: ",password)