import hashlib
import os

file_name = input("Enter the file name to hash: ")

def hash_file(file_name):
    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist! :(")
        exit(1)


    # Hashing a file using SHA-256
    with open(file_name, 'rb') as f:
        file_content = f.read()

        if not file_content:
            print(f"File '{file_name}' is empty.")
            exit(1)

        hash_object = hashlib.sha256(file_content) 

        return (hash_object.hexdigest())


if __name__ == "__main__":
    file_hash = hash_file(file_name)
    print(f"The SHA-256 hash of the file '{file_name}' is: {file_hash}")
    print("Hashing completed successfully!")