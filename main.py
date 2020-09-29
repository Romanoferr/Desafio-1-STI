import csv


class Arquivo:
	def __init__(self):
		self.lista_arquivo = []

	def gera_lista_arquivo(self):
		with open("alunos.csv", "r") as arquivo_base:
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
arquivo.gera_lista_arquivo()    # carrega o arquivo em memoria na variavel arquivo.lista_arquivo

for lini in arquivo.lista_arquivo:
	print(arquivo.lista_arquivo[lini])  # teste


