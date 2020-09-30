import csv


class Arquivo:
	def __init__(self):
		self.lista_arquivo = []
		self.dir_arquivo = 'Desafio-1-STI/alunostemp.csv'

	def gera_lista_arquivo(self):  # metodo que le o arquivo e coloca em memoria
		with open(self.dir_arquivo, 'r') as arquivo_base:
			info_arquivo = csv.reader(arquivo_base)
			for line in info_arquivo:
				self.lista_arquivo.append(line)

	"""def grava_uffmail(self, uffmail):  # metodo que grava no arquivo o email escolhido

		with open(self.dir_arquivo) as arquivo_base:
			escrever_uffmail = csv.writer(arquivo_base)
			escrever_uffmail.writerow()
"""
