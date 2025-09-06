from cryptography.fernet import Fernet

# Step 1: Generate a key (save this for decryption)
key = Fernet.generate_key()
cipher = Fernet(key)
print("Encryption Key (save this to decrypt files later):", key.decode())

# Step 2: Input text to encrypt
text = input("Enter text to encrypt: ").encode()

# Step 3: Encrypt the text
encrypted = cipher.encrypt(text)
print("Encrypted Text:", encrypted.decode())

# Step 4: Decrypt the text
decrypted = cipher.decrypt(encrypted)
print("Decrypted Text:", decrypted.decode())
