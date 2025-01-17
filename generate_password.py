import random
import string
import time

def generate_password(length, punctuation):
    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + punctuation
    allASCII_letters=string.ascii_letters
    allDigits=string.digits
    letterMin=random.sample(allASCII_letters,1)
    digitMin=random.sample(allDigits,1)
    punctuationMin=random.sample(punctuation, 1)
    result=letterMin + digitMin + punctuationMin
    remainingValues=[x for x in all_characters if x not in result]
    remainingLength=length-3
    # result.extend(random.sample(remainingValues,remainingLength))
    # Use the random module to generate the password
    # password = ''.join(random.choice(all_characters) for i in range(length))
    password = result.join(random.choice(all_characters) for i in range(length))
    random.shuffle(password)
    return password

password_length = int(input("Input the desired length of your password:"))
typicalPunctuation="!\";#$%&'()*+,-./:;<=>?@[]^_`{|}~"
print("These are the typical punctuation used:", typicalPunctuation)
resp=input("Are these punctuation characters ok to use? Enter Yes or No: ")
resp=resp.lower()
if resp == "no":
    typicalPunctuation=input("Enter the punctuation characters you want to use.")

password = generate_password(password_length, typicalPunctuation)
print(f"Generated password is: {password}")
time.sleep(1)