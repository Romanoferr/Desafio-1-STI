import csv


class Arquivo:
	def __init__(self):
		self.lista_arquivo = []

	def gera_lista_arquivo(self):  # metodo que le o arquivo e coloca em memoria
		with open('Desafio-1-STI/alunostemp.csv', 'r') as arquivo_base:
			info_arquivo = csv.reader(arquivo_base)
			for line in info_arquivo:
				self.lista_arquivo.append(line)


class Aluno:
	def __init__(self, nome, matricula, telefone, email, uffmail, ativo):
		self.nome = nome
		self.matricula = matricula
		self.telefone = telefone
		self.email = email
		self.uffmail = uffmail
		self.ativo = ativo
		self.uffmail_list = []

	def gera_uffmail(self):  # metodo que preenche a lista uffmail_list com opcoes de email baseado no nomde do aluno
		if (self.ativo == "Ativo") and (self.uffmail == ""):  # o Aluno deve estar Ativo e nao possuir uffmail
			nomes = self.nome.split(" ")
			self.uffmail_list.append((nomes[0] + nomes[2] + "@id.uff.br").lower())
			self.uffmail_list.append((nomes[0] + nomes[1] + "@id.uff.br").lower())
			self.uffmail_list.append((nomes[0][0] + nomes[1][0] + nomes[2] + "@id.uff.br").lower())
			self.uffmail_list.append((nomes[0] + nomes[1][0] + nomes[2] + "@id.uff.br").lower())
			self.uffmail_list.append((nomes[0] + "_" + nomes[2] + "@id.uff.br").lower())
			self.uffmail_list.append((nomes[0] + nomes[1][0:2] + nomes[2][0:2] + "@id.uff.br").lower())
			self.uffmail_list.append((nomes[0] + nomes[1][0] + nomes[2][0] + "@id.uff.br").lower())

	def set_uffmail(self, uffmail):
		self.uffmail = uffmail


arquivo = Arquivo()
arquivo.gera_lista_arquivo()

nova = "S"

while nova != "N":
	num_matricula = input("Digite seu numero de matricula: \n")

	for each in arquivo.lista_arquivo:  # percorre a lista ate encontrar o numero de matricula informado
		if each[1] == num_matricula:
			aluno = Aluno(each[0], each[1], each[2], each[3], each[4], each[5])  # instacia o aluno achado
			nova = "N"

	if nova == "S":  # pergunta se o usuario deseja fazer nova busca ou fechar o programa
		print("Aluno nao encontrado, deseja fazer nova pesquisa? S/N \n")
		nova = input().upper()
		if nova == "N":
			quit()


if aluno.uffmail:   # checo se o aluno possui uffmail e se possui matricula ativa
	print("Email idUFF ja existente: " + aluno.uffmail)

elif aluno.ativo == "Inativo":
	print("Matricula encontra-se inativa")

else:   # o algoritmo de escolha do uffmail so acontece se o aluno nao possuir uffmail e estiver Ativo
	aluno.gera_uffmail()
	print("Por favor, escolha uma das opcoes abaixo: ")

	escolhido = False
	while not escolhido:
		for i in range(len(aluno.uffmail_list)):
			print(str(i + 1) + "..... " + aluno.uffmail_list[i])  # imprime a lista de possiveis uffmail para escolha do usuario

		try:
			escolha = int(input())
			# checa se o numero que o usurio oferece tem equivalencia a algum email
			if escolha < 1 or escolha > len(aluno.uffmail_list):  # caso nao tenha equivalencia pede uma nova entrada valida
				print("Escolha invalida, escolha um numero entre 1 e " + str(len(aluno.uffmail_list)))
			else:  # caso tenha equivalencia guarda na variavel email_escolhido
				email_escolhido = aluno.uffmail_list[escolha - 1]
				escolhido = True

		except ValueError:
			print("Tipo de entrada incorreto, por favor digite um numero entre 1 e " + str(len(aluno.uffmail_list)))


aluno.set_uffmail(email_escolhido)
print(aluno.uffmail)

# TODO quando escolhido o email, gravar no arquivo
