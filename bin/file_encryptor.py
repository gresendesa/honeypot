from .encryptor import Honey
import base64

class Source:
	def get_fake():
		with open('targets/fake.txt','r') as file:
			return file.read()

	def get_key():
		with open('targets/key_in.txt','r') as file:
			return file.read()

	def get_message_to_encrypt():
		with open('targets/message_to_encrypt.txt','r') as file:
			return file.read()

	def set_decripted_message(message):
		with open('targets/decripted_message.txt','w') as file:
			return file.write(message)

	def set_key(key):
		with open('targets/key_out.txt','wb') as file:
			return file.write(key)


"""
=========================



=========================
"""

class File:

	decryptor = Honey()

	def message_to_base64(str):
		return base64.b64encode(str.encode(str))

	def base64_to_message(str):
		return  base64.b64decode(str).decode()

	def encrypt(message=Source.get_message_to_encrypt(), fake_message=Source.get_fake()):
		Source.set_key(base64.b64encode(str.encode(Honey().transform(message, fake_message))))

	def decrypt(fake_message=Source.get_fake(), key=Source.get_key()):
		Source.set_decripted_message(Honey().reconstruct(fake_message,File.base64_to_message(key)))