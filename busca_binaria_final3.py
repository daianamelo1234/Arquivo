import struct
import sys

if len(sys.argv) != 2:
    print "USO %s [CEP]" % sys.argv[0]
    quit()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print "Tamanho da Estrutura: %d" % registroCEP.size
f = open("cep_ordenado.dat", "r")
line = f.read(registroCEP.size)

inicio = 0
f.seek(0, 2)
fim = f.tell() // registroCEP.size
meio = (inicio + fim) // 2
f.seek(meio * registroCEP.size)

while inicio <= fim:
    meio = (inicio + fim) // 2

    if  meio == sys.argv[1]:
        sys.exit()

    elif sys.argv[1] > meio:

        fim = meio - 1

    else:
        inicio = meio + 1

print "Busca Binaria: %d" % inicio
f.close()

