instrucoes = open('teste.txt')
memoria = [0,0,0,0,0,0,0,0,0,0,0]

def clock(comando,i):
  if 'HALT' in comando:
    print('FIM DO PROGRAMA')
    return -666
  else:
    elementos = comando.split(' ')
    instrucao = elementos[0]
    if ',' in elementos[1]:
      destino = int(elementos[1].split(',')[0][1:])
      origem = elementos[1].split(',')[1]
    else:
      destino = elementos[1]
      origem = '0'
    if origem[0]=='R':
      flag=0
    else:
      flag=1
    ###### trata as instrucoes #####
    if instrucao == 'LOAD':
      if flag==0:
        memoria[destino] = memoria[int(origem[1:])]
      else:
        memoria[destino]=int(origem)
    elif instrucao == 'ADD':
      if flag==0:
        memoria[destino]=memoria[destino]+memoria[int(origem[1:])]
      else:
        memoria[destino]=memoria[destino]+int(origem)
    elif instrucao == 'SUB':
      if flag==0:
        memoria[destino]=memoria[destino]-memoria[int(origem[1:])]
      else:
        memoria[destino]=memoria[destino]-int(origem)
    elif instrucao == 'MULT':
      if flag==0:
        memoria[destino]=memoria[destino]*memoria[int(origem[1:])]
      else:
        memoria[destino]=memoria[destino]*int(origem)
    if instrucao == 'DIV':
      if flag==0:
        if(memoria[int(origem[1:])] == 0):
          print('Divisão por 0 não permitida. Linha',i+1)
          print('FIM DO PROGRAMA')
          exit()
        memoria[destino]=int(memoria[destino]/memoria[int(origem[1:])])
      else:
        if(int(origem) == 0):
          print('Divisão por 0 não permitida. Linha',i+1)
          print('FIM DO PROGRAMA')
          exit()
        memoria[destino]=int(memoria[destino]/int(origem))
    elif instrucao == 'MULT':
      if flag==0:
        memoria[destino]=memoria[destino]*memoria[int(origem[1:])]
      else:
        memoria[destino]=memoria[destino]*int(origem)
    elif instrucao == 'CMP':
      if flag==0:
        if memoria[destino] == memoria[int(origem[1:])]:
          return i+1
        else:
          return i+2
      else:
        if memoria[destino] == int(origem):
          print(memoria)
          return i+1
        else:
          print(memoria)
          return i+2
    elif instrucao == 'JMP':
      print(memoria)
      return int(destino)-1
    elif instrucao == 'CME':
      if flag==0:
        if memoria[destino] < memoria[int(origem[1:])]:
          return i+1
        else:
          return i+2
      else:
        if memoria[destino] < int(origem):
          print(memoria)
          return i+1
        else:
          print(memoria)
          return i+2
    elif instrucao == 'CMA':
      if flag==0:
        if memoria[destino] > memoria[int(origem[1:])]:
          return i+1
        else:
          return i+2
      else:
        if memoria[destino] > int(origem):
          print(memoria)
          return i+1
        else:
          print(memoria)
          return i+2
    print(memoria)
    return i+1


linhas = instrucoes.readlines()

i=0
while(i!=-666):
  i = clock(linhas[i],i)