# Encrypted Chat App

This is a simple client-server chat application using Python sockets.

Messages are encrypted using AES before being sent from the client to the server, and then decrypted on the server side.

---

## How it works

* The client takes a message from the user
* Encrypts it using AES (CBC mode)
* Sends it to the server using TCP
* The server receives the encrypted message
* Decrypts it and prints the original message

---

## Technologies used

* Python
* Socket Programming
* AES (PyCryptodome)

---

## How to run

1. Install required library:
   pip install pycryptodome

2. Run the server:
   python server.py

3. Run the client:
   python client.py

---

## Notes

* This project uses a fixed key and IV (for simplicity)
* It is for learning purposes only and not secure for real-world use

---

## Author

Kareem Medhat
