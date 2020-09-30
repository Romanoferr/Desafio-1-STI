
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
