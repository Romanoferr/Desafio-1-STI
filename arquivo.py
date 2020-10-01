import csv


class Arquivo:
	def __init__(self):
		self.lista_arquivo = []
		self.arquivo_dir = 'Desafio-1-STI/source/alunostemp.csv'

	def gera_lista_arquivo(self):  # metodo que le o arquivo e coloca em memoria
		with open(self.arquivo_dir, 'r') as arquivo_base:
			info_arquivo = csv.reader(arquivo_base)
			for line in info_arquivo:
				self.lista_arquivo.append(line)

	def update_lista_arquivo(self, uffmail, linha_salva):  # ataualiza a lista local com uff escolhido pelo usuario
		self.lista_arquivo[linha_salva][4] = uffmail

	def grava_uffmail(self):  # metodo que grava no arquivo o email escolhido
		with open(self.arquivo_dir, 'w') as arquivo_base:
			escrever_uffmail = csv.writer(arquivo_base, delimiter=',')
			for line in self.lista_arquivo:
				escrever_uffmail.writerow(line)
		print("\narquivo atualizado com sucesso...")
