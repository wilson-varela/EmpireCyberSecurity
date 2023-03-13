#!/bin/python3

menuList = {
	1:"Certificacoes",
	2:"Estudantes",
	3:"Mensalidades",
	4:"Sair"
}

options = {
	1:"Adicionar",
	2:"Listar"
}

months = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
 ]

certifications = []
students = []
payments = []

option = 0
menuOption = 0


def mainAction():
	if menuOption == 1 or menuOption == 2 or menuOption == 3  or menuOption == 4:
		match menuOption:
			case 1:
			
				print("\n====== Certificacoes ======\n")
				for key,value in options.copy().items():
					print (key, "-", value)
				option = int(input("Insira o nr da opcao:"))
				if option == 1:
					controller = True
					while controller:
						cert = input("Insira o nome da certificacao ou digite a palavra sair para voltar ao menu:")
						
						if cert != "sair":
							price = input("Insira o preco da certificacao:")
							certifications.append({
								"name":cert,
								"price":price
							})
							print("Certificacoes:",certifications)
						else:
							controller = False
					menu()
				elif option == 2:
					if len(certifications) > 0:
						print("\n Lista de Certificacoes \n")
						for index,item in enumerate(certifications):
							print (index+1, ".", " Nome da certificacao: ", item['name'], " Preco: ", item['price'] )
						menu()
					else:
						print("\n Sem Certificacoes cadastradas \n")
						menu()
				else:
					print("\n Opcao incorreta ...regressando ao menu \n")
					menu()
					
			case 2:
			
				print("====== Estudantes ======\n")
				for key,value in options.copy().items():
					print (key, "-", value)
				option = int(input("Insira o nr da opcao:"))
				if option == 1:
					controller = True
					if len(certifications)>0:
						while controller:
							studentName = input("Insira o nome do estudante ou digite a palavra sair para voltar ao menu:")
							
							if studentName != "sair":
								print("Selecione a certificacao")
								for index,item in enumerate(certifications):
									print (index+1, "-", item['name'])
								studentOption = int(input("Insira o nr da opcao:"))
								if studentOption > 0 and studentOption <= len(certifications):
									
									students.append({
										"name":studentName,
										"certification": certifications[studentOption-1]['name']
									})
									print("Students:",students)
								else:
									print("\nOpcao incorreta, regressando ao menu...\n")
									controller = False
									
							else:
								controller = False
						menu()
						
								
					else:
						print("\nAdicione certificacoes, regressando ao menu...\n")
						menu()
				elif option == 2:
					if len(students) > 0:
						print("\n Lista de Estudantes \n")
						for index,item in enumerate(students):
							print (index+1, ".", " Nome do estudante: ", item['name'], " Certificacao: ", item['certification'] )
						menu()
					else:
						print("\n Sem Estudantes cadastrados \n")
						menu()
						
				else:
					print("\n Opcao incorreta ...regressando ao menu \n")
					menu()
			case 3:
			
				print("====== Mensalidades ======")
				for key,value in options.copy().items():
					print (key, "-", value)
				option = int(input("Insira o nr da opcao:"))
				if option == 1:
					controller = True
					if len(certifications)>0 and len(students)>0:
						while controller:
							print("Selecione o estudante")
							print("0-Sair")
							for index,item in enumerate(students):
								print (index+1, "-", item['name'])
							studentOption = int(input("Insira o nr da opcao:"))
							if studentOption != 0:
								print("Selecione o mes")
								for index,item in enumerate(months):
									print (index+1, "-", item)
								monthOption = int(input("Insira o nr da opcao:"))
								
								if (studentOption > 0 and studentOption <= len(students)) and (monthOption > 0 and monthOption <= len(months)) :
									
									payments.append({
										"name":students[studentOption-1]['name'],
										"month": months[monthOption-1]
									})
									print("PAgamentos:",payments)
								else:
									print("\nOpcao incorreta, regressando ao menu...\n")
									controller = False
							else:
								controller = False
						menu()
					else:
						print("\nAdicione certificacoes, regressando ao menu...\n")
						menu()
				elif option == 2:
					if len(payments) > 0:
						print("\n Lista de Pagamentos de Mensalidades \n")
						for index,item in enumerate(payments):
							print (index+1, ".", " Nome do estudante: ", item['name'], " Mes pago: ", item['month'] )
						menu()
					else:
						print("\n Sem pagamentos cadastrados \n")
						menu()
				else:
					print("\n Opcao incorreta ...regressando ao menu \n")
					menu()
			case 4:
				print("\n Developed by RedDot\n")
				print("I would like to change the world, that's why i'm looking for the source code")
				exit()
				
		
	else:
		print("\nOpcao incorreta, tente novamente")
		menu()
def menu ():
	global option,menuOption
	print("\n========== EMPIRE CYBERSECURITY APP ==========\n")
	for key,value in menuList.copy().items():
		print (key, "-", value)
	menuOption = int(input("Insira o nr da opcao:"))
	mainAction()
	



menu()

	
