import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

KEY = b'12345678901234567890123456789012'
IV = b'1234567890123456'

def encrypt_message(msg):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(pad(msg.encode(), AES.block_size))
    return base64.b64encode(encrypted).decode()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

message = input("Enter Message: ")
encrypted_msg = encrypt_message(message)

print(f"Encrypted Message: {encrypted_msg}")
client_socket.sendall(encrypted_msg.encode())

client_socket.close()
