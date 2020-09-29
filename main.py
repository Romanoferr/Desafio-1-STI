import csv


class Arquivo:
	def __init__(self):
		self.lista_arquivo = []

	def gera_lista_arquivo(self):  # metodo que le o arquivo e coloca em memoria
		with open('Desafio-1-STI/alunos.csv', 'r') as arquivo_base:
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


arquivo = Arquivo()
arquivo.gera_lista_arquivo()  # carrega o arquivo em memoria na variavel arquivo.lista_arquivo

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

