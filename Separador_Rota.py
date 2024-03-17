lista_pct = []
rota_davi = []
rota_samuel = []
rota_carlos = []
rota_gabriel = []
qtd_davi = 0
qtd_samuel = 0
qtd_carlos = 0
qtd_gabriel = 0
qtd_recebida = 0

def add_saca():
    qtd_pcts = int(input("qtd de pacotes : "))
    for i in range(qtd_pcts + 1):
        if i != 0:
            lista_pct.append(i)
    global qtd_recebida 
    qtd_recebida += qtd_pcts
    print(qtd_recebida)

def remover_parada():
    parada = int(input("remover parada:"))
    qtd_pct = lista_pct.count(parada)
    for _ in range(qtd_pct):
        lista_pct.remove(parada)

def add_pct_parada():
    parada_e_qtd = str(input("digite a parada e a quantidade de pacotes: "))
    parada_e_qtd = parada_e_qtd.split(',')
    print(parada_e_qtd)
    parada = int(parada_e_qtd[0])
    qtd = int(parada_e_qtd[1])
    lista_pct.remove(parada)
    for _ in range(qtd):
        lista_pct.append(parada)
        lista_pct.sort()
        print(f"--------------------------------- \n Pacotes: {lista_pct}")
        
def verificar_qtd():
    print(f"QTD RECEBIDO: {qtd_recebida}\nQTD ATUAL: {len(lista_pct)}")

def dist_rota():
    entregador = str(input("entregador: "))
    rota = str(input("pacotes: "))
    match entregador:
        case "carlos":
            n_rota = rota.split('-')
            ini_rota = int(n_rota[0])
            final_rota = int(n_rota[1])
            print(lista_pct)
            print(ini_rota)
            ini_rota = lista_pct.index(ini_rota)
            final_rota = lista_pct.index(final_rota) 
            final_rota += 1 
            for i in range(ini_rota,final_rota):
                rota_carlos.append(lista_pct[i])
                lista_pct[i] = 0
            print("------------------------")
            print(rota_carlos)
            global qtd_carlos
            qtd_carlos += len(rota_carlos)

        case "samuel":
                n_rota = rota.split('-')
                ini_rota = int(n_rota[0])
                final_rota = int(n_rota[1])
                print(lista_pct)
                print(ini_rota)
                ini_rota = lista_pct.index(ini_rota)
                final_rota = lista_pct.index(final_rota)   
                final_rota += 1 
                for i in range(ini_rota,final_rota):
                    rota_samuel.append(lista_pct[i])
                    lista_pct[i] = 0
                print("------------------------")
                print(rota_samuel)
                global qtd_samuel
                qtd_samuel+= len(rota_samuel)

        case "gabriel":
            n_rota = rota.split('-')
            ini_rota = int(n_rota[0])
            final_rota = int(n_rota[1])
            print(lista_pct)
            print(ini_rota)
            ini_rota = lista_pct.index(ini_rota)
            final_rota = lista_pct.index(final_rota)
            final_rota += 1 
            for i in range(ini_rota,final_rota):
                rota_gabriel.append(lista_pct[i])
                lista_pct[i] = 0
            print("------------------------")
            print(rota_gabriel)
            print(f"PACOTES GABRIEL: {rota_gabriel.__len__()}")
            global qtd_gabriel
            qtd_gabriel += len(rota_gabriel)

        case "davi":
            n_rota = rota.split('-')
            ini_rota = int(n_rota[0])
            final_rota = int(n_rota[1])
            print(lista_pct)
            print(ini_rota)
            ini_rota = lista_pct.index(ini_rota)
            final_rota = lista_pct.index(final_rota)
            final_rota += 1 
            for i in range(ini_rota,final_rota):
                rota_davi.append(lista_pct[i])
                lista_pct[i] = 0
            print("------------------------") 
            print(rota_davi)
            global qtd_davi
            qtd_davi += len(rota_davi)

def visualizar_rota():
    print("-----------------------------------------------------------")
    print(rota_samuel)
    print("-----------------------------------------------------------")
    print(rota_davi)
    print("-----------------------------------------------------------")
    print(rota_carlos)
    print("-----------------------------------------------------------")
    print(rota_gabriel)        
def exit():
    bd_saca = open("saca.txt","w")
    bd_saca.write("Samuel:")
    for y in rota_samuel:
        bd_saca.write(f"{y},")
    bd_saca.write("\n")
    bd_saca.write("Davi:")
    for y in rota_davi:
        bd_saca.write(f"{y},")
    bd_saca.write("\n")
    bd_saca.write("Carlos:")
    for y in rota_carlos:
        bd_saca.write(f"{y},")
    bd_saca.write("\n")
    bd_saca.write("Gabriel:")     
    for y in rota_gabriel:
        bd_saca.write(f"{y},")   
          
        
lista_pct = []
lista_pct_copia = []
qtd_recebida = 0
while True:
    print(f"--------------------------------------------------------------------------------------------------------------------------------\n                                                                                      QTD_PCTS: {qtd_recebida}")
    print(f"                                                                                      QTD_SAMUEL: {qtd_samuel}")                                                                                                                                                                                                                                                    # QTD_CARLOS: {rota_samuel}
    print(f"                                                                                      QTD_CARLOS: {qtd_carlos}")                                                                                                                                                                                                                                                    #QTD_GABRIEL: {rota_samuel}
    print(f"                                                                                      QTD_DAVI: {qtd_davi}")
    print(f"                                                                                      QTD_GABRIEL: {qtd_gabriel}")                                                                                                                                                                                                                                                    #QTD_DAVI: {rota_samuel}
                                                                                                                                                                                                                                    
          
          
    print("1 - ADICIONAR SACA")
    print("2 - REMOVER PARADA")
    print("3 - ADICONAR PACOTE NA PARADA")
    print("4 - CONFIRMAR QUANTIDADE")
    print("5 - CRIAR ROTA")
    print("6 - VISUALIZAR ROTAS")
    print("0 - FECHAR")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    menu = int(input("escolha uma opção a cima: "))
    match menu : 
        case 1:
             add_saca()
        case 2:
            remover_parada()
        case 3:
            add_pct_parada()
        case 4:
            verificar_qtd()
        case 5:
            dist_rota()
        case 6:
            visualizar_rota()
        case 0:
            exit()
