import csv


class Arquivo:
	def __init__(self):
		self.lista_arquivo = []
		self.arquivo_dir = 'Desafio-1-STI/source/alunos.csv'

	def gera_lista_arquivo(self):  # metodo que le o arquivo e preenche a lista local
		with open(self.arquivo_dir, 'r') as arquivo_base:
			info_arquivo = csv.reader(arquivo_base)
			for line in info_arquivo:
				self.lista_arquivo.append(line)

	def update_lista_arquivo(self, uffmail, linha_salva):  # ataualiza a lista local dado um uffmail e a linha na lista
		self.lista_arquivo[linha_salva][4] = uffmail

	def escreve_arquivo(self):  # metodo que grava a lista no arquivo
		with open(self.arquivo_dir, 'w') as arquivo_base:
			escrever_uffmail = csv.writer(arquivo_base, delimiter=',')
			for line in self.lista_arquivo:
				escrever_uffmail.writerow(line)
		print("\narquivo atualizado com sucesso...")
