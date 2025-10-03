import hashlib
import random
import string



# Generate a  random MD5 hash

def generate_random_md5_hash(length=16):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    md5_hash = hashlib.md5(random_string.encode()).hexdigest()
    return md5_hash


# example usage with a if __name__ == "__main__":
if __name__ == "__main__":
    
    num_hashes = 22  #input("Ingresa cantidad de randoms: ")
       # Change this value for more or fewer hashes
    for _ in range(num_hashes):
        print(generate_random_md5_hash())
