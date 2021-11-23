""" usar uma estrutura de repetição for /while
um contador com contagem normal e outro com contagem regressiva
"""

for p, r in enumerate(range(10,1,-1)):
# o range serve para sequencias
# start - início da sequência
# stop - último elemento da sequência
# step - intervalo entre os elementos
# range (start, stop,step)
# O enumerate serve para contar os elementos do laço e serve como a lista progresiva
    print(p,r)
