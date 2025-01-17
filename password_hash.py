import hashlib
import time

def hash_password(password):
    # A dictionary to store the hexadecimal representation for each hash and update the dictionary
    hashlibDict={"sha1":"","sha224":"","sha256":"","sha384":"","sha512":"","sha3_224":"","sha3_256":"","sha3_384":"","sha3_512":""}
    password_bytes = password.encode('utf-8') # Encode the password as bytes
    
    for key in hashlibDict:
        statement="hashlib.{hashFunc}(password_bytes)"
        alg=key
        modStmt=statement.format(hashFunc=alg) # will look like: "hashlib.sha256(password_bytes)"
        hash_object=eval(modStmt)
        # Get the hexadecimal representation of the hash
        password_hash = hash_object.hexdigest()
        hashlibDict[key]=password_hash
    
    return hashlibDict

password = input("Input your password: ")
hashed_passwords_dict = hash_password(password)
time.sleep(1)