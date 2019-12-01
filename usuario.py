arquivo = open('usuarios.txt','r')
original= arquivo.readlines()
num = 1
soma = 0
i = 0
ordem = []
def convertMB (a):
    MB = (int (a)/1024)/1024
    MB = '{:.2f}'.format(MB)
    return MB
def calcpercent (mb, soma):
    percent = (mb/soma)*100
    percent = '{:.2f}'.format(percent)
    return percent
##ordena e soma
for l in original:
    conteudo = l.split()
    conteudo[1] = convertMB(conteudo[1])
    mb = conteudo[1]
    soma += float (mb)
    ordem.append(float (conteudo[1]) )
    ordem.sort(reverse=True)
while i < len (ordem):
   for l in original:
      conteudo = l.split()
      conteudo[1] = convertMB(conteudo[1])
      if i == 0:
         if conteudo [1] == str (ordem [i]):
            arquivo = open ('ordenacao.txt', 'w')
            arquivo.writelines(str (ordem [i]) + ' ' + conteudo [0] + '\n')
            arquivo.close()
         else:
            continue
      else:
         if conteudo [1] == str (ordem [i]):
            arquivo = open ('ordenacao.txt', 'a')
            arquivo.writelines(str (ordem [i]) + ' ' + conteudo [0] + '\n')
            arquivo.close()
         else:
            continue
   i += 1
arquivo = open ('relatorio.txt', 'w')
arquivo.write('ACME Inc.' + ' '* 17 +'uso do espaço em disco pelos usuários \n' + '-'*80 + '\n')
arquivo.write('Nr.'+' '*6+'Usuário'+' '*10+'Espaço utilizado'+' '*10+ ' % do uso \n')
arquivo.close()
arquivo = open ('ordenacao.txt', 'r')
ordena = arquivo.readlines()
##arquivo principal
for linha in ordena:
    cont = linha.split()
    mb = cont[0]
    percentual = calcpercent(float (mb), float(soma))
    espacoM = 15 + (9 - (len(cont[1]))) - (len(str (mb)))
    espacoP = 19 + (5 - (len(str (percentual))))
    arquivo = open ('relatorio.txt','a')
    arquivo.writelines (str (num) + ' '*8 + cont [1] + ' '*espacoM + mb +' MB'+ ' '*espacoP + str (percentual) + '%\n')
    arquivo.close()
    num += 1
media = soma/6
media = '{:.2f}'.format(media)
arquivo = open ('relatorio.txt','a')
arquivo.writelines ('\nEspaço total ocupado: '+ str (soma) + ' MB')
arquivo.writelines ('\nEspaço médio ocupado: '+ str (media) + ' MB')
arquivo.close()
arquivo = open ('relatorio.txt', 'r')
saida = int (input ("quantas posições você deseja ver?\n"))
for i in range (saida + 3):
        relatorio = arquivo.readline()
        if i > 8:
            break
        elif i >1:
            print (relatorio)
        else:
            continue
        
