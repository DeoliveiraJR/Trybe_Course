# Exercício 8 ========================================== :
# Envie pacotes para o servidor UDP utilizando o Netcat (nc). Em seguida pare o servidor e perceba que, como não há conexão, nada é sentido pelo client.

# Solução proposta :
# nc -u 127.0.0.1 8084
# Após executar o comando, digite a mensagem e tecle enter para enviá-las.

# Exercício 9 ========================================== :
# Faça uma chamada ao server utilizando o cURL. Lembre que, além do HTTP, o comando utiliza o protocolo TCP e não o UDP. Repare o que acontece.

# Solução proposta :
# curl localhost:8084

# Exercício 10 ========================================== :
# Agora, vamos utilizar um tipo de proxy que pode ser bastante útil no nosso cotidiano como pessoas desenvolvedoras: o NGROK. Com ele conseguimos criar um túnel para o nosso localhost.

# Crie um servidor HTTP em sua máquina executando na porta 80 (pode ser um front-end ou um back-end criado em aulas anteriores).

# Baixe o ngrok e extraia o arquivo baixado em uma pasta de sua preferência, conforme instruções do site oficial.

# Conforme instruções do site, crie um túnel para a porta 80 de sua máquina.

# Acesse o link disponibilizado em seu navegador. Utilize-o para acessar de outros dispositivos, como seu smartphone ou outro computador 😎.

# hackerman
# Crie um servidor HTTP em sua máquina executando na porta 80 (pode ser um front-end ou um back-end criado em aulas anteriores).

# Solução proposta :
# Python é um brinquedo que vem com todos os acessórios, lembra? Claro que ele vem com um servidor http pronto pra usar! Vamos criar um diretório novo e rodar o servidor lá dentro:

#  mkdir diretorio && cd diretorio
#  python3 -m http.server 80
# Baixe o ngrok e extraia o arquivo baixado em uma pasta de sua preferência, conforme instruções do site oficial.

#  unzip /path/to/ngrok.zip
# Conforme instruções do site, crie um túnel para a porta 80 de sua máquina.

#  ./ngrok http 80
# Acesse o link disponibilizado em seu navegador. Utilize-o para acessar de outros dispositivos, como seu smartphone ou outro computador 😎.

# ./ngrok http 80
