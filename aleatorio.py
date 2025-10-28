from random import choice 
from time import sleep 
from datetime import datetime

def parabainx(nome , premio):
	for i in range(len(premio)):
		print(f'{nome[i]} vai ficar com o prêmio: {premio[i]}')
		sleep(1.5)
	
	data = datetime.now()
	data = data.strftime("%d-%m-%Y_%H-%M")
	try:
		with open(f"resultado_sorteio{data}.txt", "w", encoding="utf-8") as bloquinho:
		    for i in range(len(vencedores)):
		        bloquinho.write(f"O {i + 1}º prêmio: {premios[i]} vai para {vencedores[i].upper()}\n")
		print(f"\nArquivo 'resultado_sorteio{data}.txt' criado com sucesso!\n")
		print("\nFINALMENTE ACABO ESSA PORRA\n")
	except Exception as e:
		print("Algo de errado não está certo... Não consegui criar o arquivo .txt")
		print("COPIA E COLA O RESULTADO PRA NÃO PERDER!!!!!!!!!!!!!")
		print("vc tem 5 segundos pra isso antes de aparecer uma mensagem de erro grandona que vai te atrapalhar")
		sleep(5)
		print(e)

def suspense():
	for i in range(3 , 0 , -1):
		sleep(1)
		print(f'	{i}...')
		sleep(1)
		
def linha():
	sleep(0.5)
	print('\n----------------------------------------------------------------------------\n')
	sleep(0.5)
	
def insereDados(tipo):
	tipo = tipo.lower()
	lista = []
	entrada = ' '
	while entrada:
		sleep(0.2)
		entrada = input(f'Bota o {tipo.upper()} ai mano.\nSe não quiser mais por nenhum {tipo} é só dar Enter (:\n> ')
		if entrada:
			lista.append(entrada.capitalize())
			print()
	linha()
	return lista

######################################################################################

print('\nSorteador de sorteios da D.S.T Noise!!!!!!!!!!!!!!!!!!!!!!')
linha()

premios = insereDados('prêmio')
listaNomes = insereDados('nome')

#bloco q so tem logica
quantidadeSorteada = len(premios)
vencedores = []
for i in range(quantidadeSorteada):
	sorteado = choice(listaNomes)
	vencedores.append(sorteado)
	listaNomes.remove(sorteado)

for i in range(quantidadeSorteada):
	print(f'O { i + 1 }º premio: { premios[i] } vai para...')
	suspense()
	print(f'Parabéns pelo prêmio, { vencedores[i].upper() }!')
	if i != quantidadeSorteada - 1:
		input('\n**********Tecle enter para sortear o próximo**********\n')
linha()	

parabainx(vencedores , premios)


