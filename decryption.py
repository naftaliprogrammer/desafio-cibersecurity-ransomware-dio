import os
import pyaes

# Ler o arquivo.
file_name = 'teste.txt.hackeado1'
with open(file_name, 'rb') as file:
    file_data = file.read()

# remover o arquivo atual.
os.remove(file_name)

# gerando a chave.
key = b"testeransomware1"  # Está chave é de 16 bites.
# Lembrando que apenas pode se gerar chaves de 16, 24, e 32 bites
# Cada letra é um 1 bite.
aes = pyaes.AESModeOfOperationCTR(key)

# descriptografando.
crypt_data = aes.decrypt(file_data)

# Criando um novo arquivo.
new_file_name = "teste.txt."
with open(new_file_name, 'wb') as new_file:
    new_file.write(crypt_data)
