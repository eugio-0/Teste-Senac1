tem_ingresso = False
aniversariante = False

if tem_ingresso == True or aniversariante == True:
    print('Acesso Liberado!')
else:
    print("Acesso Negado! Compre o ingresso.")

aniversariante = input("Aniversariante? (sim/nao")
tem_ingresso = input("Ingresso? (sim/nao")

if aniversariante == "sim":
    aniversariante = True
else:
    aniversariante = False
if tem_ingresso == "sim":
    tem_ingresso = True
else:
    tem_ingresso= False

    if aniversariante == True or tem_ingresso == True:
        print("Acesso Liberado!")
    else:
        print("Acesso Negado! Compre o ingresso.")



if aniversariante == 'sim' or tem_ingresso == "sim":
    print('Acesso Liberado!')
else:
    print('Acesso Negado! Compre o igresso.')