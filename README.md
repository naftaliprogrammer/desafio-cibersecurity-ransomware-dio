# desafio-cibersecurity-ransomware-dio
Esse scrip é um desafio, feito em Python para criptografar arquivos usando AES (Advanced Encryption Standard) e descriptografar o arquivo utilizando a mesma chave.


###  Código de Criptografia

Este script em Python realiza a **criptografia** de um arquivo utilizando o **AES (Advanced Encryption Standard)** no modo **CTR** (Counter Mode). Ele realiza as seguintes etapas:

1. **Leitura do Arquivo Original:** O código abre e lê um arquivo binário (`teste1.txt`).
2. **Remoção do Arquivo Original:** Após ler o conteúdo do arquivo, ele é removido do sistema.
3. **Definição da Chave de Criptografia:** A chave `testeransomware1` é definida, com 16 bytes.
4. **Configuração do AES em Modo CTR:** A biblioteca `pyaes` é usada para inicializar o AES no modo CTR com a chave fornecida.
5. **Criptografia dos Dados:** Os dados do arquivo são criptografados utilizando o método `aes.encrypt()`.
6. **Criação de um Novo Arquivo Criptografado:** O conteúdo criptografado é salvo em um novo arquivo com a extensão `.hackeado1`.

Este código realiza a criptografia de um arquivo com a chave fornecida e o algoritmo AES no modo CTR.

---

### Código de Descriptografia

Este script em Python realiza a **descriptografia** de um arquivo previamente criptografado utilizando o **AES (Advanced Encryption Standard)** no modo **CTR**. Ele segue as etapas abaixo:

1. **Leitura do Arquivo Criptografado:** O código abre e lê um arquivo binário criptografado (`teste1.txt.hackeado1`).
2. **Remoção do Arquivo Original:** Após ler o conteúdo criptografado, o arquivo original é removido do sistema.
3. **Definição da Chave de Descriptografia:** A mesma chave de criptografia, `testeransomware1`, é usada para descriptografar os dados.
4. **Configuração do AES em Modo CTR:** O AES é inicializado novamente no modo CTR usando a mesma chave.
5. **Descriptografia dos Dados:** Os dados criptografados são descriptografados utilizando o método `aes.decrypt()`.
6. **Criação de um Novo Arquivo Descriptografado:** O conteúdo original é restaurado e salvo em um novo arquivo, `teste1.txt`.

Este código realiza a descriptografia de um arquivo criptografado utilizando a mesma chave de criptografia usada originalmente, recuperando os dados ao seu estado original.

---
