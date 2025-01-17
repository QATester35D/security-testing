import random
import string
import time

#################################################################################################
# Following these common password stanards:
#  - Must begin with a character
#  - Must contain:
#    - At least 1 lowercase letter
#    - At least 1 uppercase letter
#    - At least 1 number
#    - At least 1 special character
#################################################################################################
def generate_password(length, punctuation):
    # Define the characters to use in the password; Getting punctuation from what is passed in
    all_characters = string.ascii_letters + string.digits + punctuation
    allASCII_letters=string.ascii_letters
    # Add the minimum required characters from list in comments at top of script
    letterLowerMin=random.sample(string.ascii_lowercase,1)
    letterUpperMin=random.sample(string.ascii_uppercase,1)
    digitMin=random.sample(string.digits,1)
    punctuationMin=random.sample(punctuation, 1)
    result=letterLowerMin + letterUpperMin + digitMin + punctuationMin
    remainingValues=[x for x in all_characters if x not in result]
    remainingLength=length-4
    result.extend(random.sample(remainingValues,remainingLength)) #generate the rest of characters randomly
    #shuffling the result but need to keep the first character as a letter
    random.shuffle(result)
    if result[0] not in allASCII_letters:
        while True:
            random.shuffle(result)
            if result[0] in allASCII_letters:
                break
    pswd=str("".join(result))
    return pswd

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