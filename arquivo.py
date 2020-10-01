import csv


class Arquivo:
	def __init__(self):
		self.lista_arquivo = []
		self.in_arquivo = 'Desafio-1-STI/input/alunostemp.csv'
		self.out_arquivo = 'Desafio-1-STI/output/alunostempout.csv'

	def gera_lista_arquivo(self):  # metodo que le o arquivo e coloca em memoria
		with open(self.in_arquivo, 'r') as arquivo_base:
			info_arquivo = csv.reader(arquivo_base)
			for line in info_arquivo:
				self.lista_arquivo.append(line)

	def update_lista_arquivo(self, uffmail, linha_salva):  # ataualiza a lista local com uff escolhido pelo usuario
		self.lista_arquivo[linha_salva][4] = uffmail

	def grava_uffmail(self):  # metodo que grava no arquivo o email escolhido
		with open(self.out_arquivo, 'w', newline='') as arquivo_base:
			escrever_uffmail = csv.writer(arquivo_base)
			escrever_uffmail.writerow(self.lista_arquivo)

