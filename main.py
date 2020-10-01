from aluno import Aluno
from arquivo import Arquivo

arquivo = Arquivo()
arquivo.gera_lista_arquivo()

nova = "S"


def escolha_uffmail():
	if aluno.ativo == "Ativo" and aluno.uffmail == "":  # o algoritmo de escolha do uffmail so acontece se o aluno nao
		# possuir uffmail e estiver Ativo
		aluno.gera_uffmail()
		print("Por favor, escolha uma das opções abaixo: ")

		escolhido = False
		while not escolhido:
			for i in range(len(aluno.uffmail_list)):
				print(str(i + 1) + "..... " + aluno.uffmail_list[
					i])  # imprime a lista de possiveis uffmail para escolha do usuario

			try:
				escolha = int(input())
				# checa se o numero que o usurio oferece tem equivalencia a algum email
				if escolha < 1 or escolha > len(
						aluno.uffmail_list):  # caso nao tenha equivalencia pede uma nova entrada valida
					print("Escolha inválida, escolha um número entre 1 e " + str(len(aluno.uffmail_list)))
				else:  # caso tenha equivalencia guarda na propriedade uffmail de aluno
					aluno.set_uffmail(aluno.uffmail_list[escolha - 1])
					escolhido = True

			except ValueError:  # trata entradas que nao sao numeros inteiros
				print("Tipo de entrada incorreta, por favor digite um número entre 1 e " + str(len(aluno.uffmail_list)))


def inativo_existente():  # imprimo mensagem caso o aluno ja possua uffmail ou matricula Inativa
	if aluno.uffmail:
		print("Email idUFF já existente: " + aluno.uffmail)
	if aluno.ativo == "Inativo":
		print("Matrácula encontra-se inativa")


while nova != "N":
	num_matricula = input("Digite seu número de matrícula: \n")
	salva_linha = -1
	for each in arquivo.lista_arquivo:  # percorre a lista ate encontrar o numero de matricula informado
		salva_linha += 1
		if each[1] == num_matricula:
			aluno = Aluno(each[0], each[1], each[2], each[3], each[4], each[5])  # instacia o aluno achado
			nova = "N"
			if aluno.uffmail or aluno.ativo == "Inativo":
				inativo_existente()
			else:
				escolha_uffmail()  # chama funcao com algoritmo de criacao e escolha do uffmail
				print("A criação de seu e-mail (" + aluno.uffmail + ") será feita nos próximos minutos.")
				print("Um SMS foi enviado para " + aluno.telefone + " com sua senha de acesso")
				arquivo.update_lista_arquivo(aluno.uffmail, salva_linha)
				arquivo.grava_uffmail()

	if nova != "N":  # pergunta se o usuario deseja fazer nova busca ou fechar o programa
		print("Aluno não encontrado, deseja fazer nova pesquisa? S/N ")
		nova = input().upper()
	else:
		quit()

