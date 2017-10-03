#Reordenacao em blocos de arquivo binario
import sys,os

#Conta quantos comandos de pular linha (/n) tem no arquivo, contando assim quantas linhas existem nele
#maxLines = sum((1 for i in open('cep.dat', 'rb')))
bloco = 600
fileN = '0';

with open('cep.dat', 'rb') as cepFile:
    for line in cepFile:
        linha = []
        for i in range(bloco):
            logradouro = cepFile.read(72).decode('iso8859_1')
            bairro = cepFile.read(72).decode('iso8859_1')
            cidade = cepFile.read(72).decode('iso8859_1')
            estado = cepFile.read(72).decode('iso8859_1')
            sigla = cepFile.read(2).decode('iso8859_1')
            cep = cepFile.read(8).decode('iso8859_1')
            linhaeof = cepFile.read(2).decode('iso8859_1')

            linha.append([logradouro+bairro+cidade+estado+sigla+cep+linhaeof, cep])

        linha = sorted(linha, key=lambda charac: charac[1])   # sort by cep

        resFile = open('resultado/ordenado'+fileN+'.dat', 'w+')
        for item in linha:
            resFile.write(item[0])
        resFile.close()
        fileN = str(float(fileN) + 1)
        
