import os
import hmac
import hashlib
import time
import base64
import struct
import sys
from cryptography.fernet import Fernet





def encrypt_key(key, filename):
    encryption_key = Fernet.generate_key()
    cipher = Fernet(encryption_key)
    encrypted_key = cipher.encrypt(key)

    with open(filename, "wb") as f:
        f.write(encryption_key + b"\n" + encrypted_key)

    print("Key was successfully saved in ft_otp.key.")



def decrypt_key(filename):
    try:
        with open(filename, "rb") as f:
            data = f.readlines()
            encryption_key = data[0].strip()
            encrypted_key = data[1].strip()

        cipher = Fernet(encryption_key)
        return cipher.decrypt(encrypted_key)
    except Exception as e:
        print("Error: Unable to read or decrypt the key.")
        print(e)
        sys.exit(1)



def generate_hotp(secret, counter):
    key = base64.b16decode(secret, casefold=True)
    counter_bytes = struct.pack("!Q", counter)
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()

    offset = hmac_hash[-1] & 0x0F
    code = struct.unpack_from("!I", hmac_hash, offset)[0] & 0x7FFFFFFF

    otp = code % 1000000
    return f"{otp:06d}"



def main():
    if len(sys.argv) < 3:
        print("Usage: python3 ft_otp.py -g <hex_key_file>")
        print("Usage: python3 ft_otp.py -k <key_file>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "-g":
        if not os.path.exists(sys.argv[2]):
            print("Error: Key file does not exist.")
            sys.exit(1)

        with open(sys.argv[2], "r") as f:
            key = f.read().strip()


        if len(key) != 64 or not (all(c in "0123456789abcdef" for c in key) or all(c in "0123456789ABCDEF" for c in key)):
            print("Error: Key must be 64 hexadecimal characters.")
            sys.exit(1)

        encrypt_key(key.encode(), "ft_otp.key")

    elif command == "-k":
        key = decrypt_key(sys.argv[2])
        counter = int(time.time() // 30)
        otp = generate_hotp(key.decode(), counter)
        print(otp)
    else:
        print("Error: Invalid command.")
        sys.exit(1)



if __name__ == "__main__":
    main()
