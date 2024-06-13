from cryptography.fernet import Fernet

# Generar una clave de cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Mensaje a cifrar
message = b"Este es un mensaje secreto"

# Cifrar el mensaje
cipher_text = cipher_suite.encrypt(message)
print(f"Mensaje cifrado: {cipher_text}")

# Descifrar el mensaje
plain_text = cipher_suite.decrypt(cipher_text)
print(f"Mensaje descifrado: {plain_text.decode('utf-8')}")
