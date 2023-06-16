import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

current_directory = os.getcwd()
root = Tk()
root.withdraw()  # Hide the root window

memoria = [0,0,0,0,0,0,0,0,0,0,0]

def clock(comando,i):
  if 'HALT' in comando:
    print('FIM DO PROGRAMA')
    return -666
  else:
    print('COMANDO: ',comando)
    elementos = comando.split(' ')
    instrucao = elementos[0]
    if ',' in elementos[1]:
      destino = int(elementos[1].split(',')[0][1:])
      #destino = destino[1:]
      origem = elementos[1].split(',')[1]
    else:
      destino = elementos[1]
      origem = '0'
    #print('**',origem,destino)
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
    if instrucao == 'ADD':
      if flag==0:
        memoria[destino]=memoria[destino]+memoria[int(origem[1:])]
      else:
        memoria[destino]=memoria[destino]+int(origem)
    if instrucao == 'SUB':
      if flag==0:
        memoria[destino]=memoria[destino]-memoria[int(origem[1:])]
      else:
        memoria[destino]=memoria[destino]-int(origem)
    if instrucao == 'MULT':
      if flag==0:
        memoria[destino]=memoria[destino]*memoria[int(origem[1:])]
      else:
        memoria[destino]=memoria[destino]*int(origem)
    #if instrucao == 'DIV':
    if instrucao == 'CMP':
      #Compara origem e destino. Se forem iguais executa a linha i+1,
      #se forem difeentes executa a linha i+2
      if flag==0:
        if memoria[destino]==memoria[int(origem[1:])]:
          return i+1
        else:
          return i+2
      else:
        if memoria[destino] == int(origem):
          #print('Instrucao:',instrucao,' destino',destino,'origem',origem)
          print(memoria)
          #print('i=',i,'retorna:',i+1,'na lista:',i)
          return i+1
        else:
          #print('Instrucao:',instrucao,' destino',destino,'origem',origem)
          print(memoria)
          #print('i=',i,'retorna:',i+1,'na lista:',i)
          return i+2
    
    if instrucao == 'JMP':
      #IMPLEMENTAR
      #print('Instrucao:',instrucao,' destino',destino,'origem',origem)
      print(memoria)
      #print('i=',i,'retorna:',i+1,'na lista:',i)
      return int(destino)-1

    #print('Instrucao:',instrucao,' destino',destino,'origem',origem)
    print(memoria)
    #print('i=',i,'retorna:',i+1,'na lista:',i)
    return i+1

if __name__ == "__main__":

    # Open the file explorer dialog
    filename = askopenfilename(initialdir=current_directory)
    if filename:
        print("Selected file:", filename)
    else:
        print("No file selected.")

    with open(filename, 'r') as file:
        ListaLida = [line.strip('#') for line in file.readlines()]

    i=0
    while(i!=-666):
        i = clock(ListaLida[i],i)
