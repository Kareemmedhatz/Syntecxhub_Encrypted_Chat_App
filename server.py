import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

KEY = b'12345678901234567890123456789012'
IV = b'1234567890123456'

def decrypt_message(enc_msg):
    encrypted_data = base64.b64decode(enc_msg)
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted.decode()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)

print("Server listening on port 5000...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
print(f"Encrypted: {data.decode()}")

decrypted_text = decrypt_message(data.decode())
print(f"Decrypted: {decrypted_text}")

conn.close()
server_socket.close()
