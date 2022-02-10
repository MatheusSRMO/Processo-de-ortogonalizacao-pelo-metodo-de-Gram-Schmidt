#Faça um programa que leia n vetores (bae) e ache uma base ortogonal pelo
#processo de ortogonalização de Gram-Schmidt 

#achando uma base ortogonal
# w1 = matriz[0]
# w2 = matriz[1] - projeção de matriz[1] sobre matriz[0]
# w3 = matriz[2] - projeção de matriz[2] sobre matriz[0] - projeção de matriz[2] sobre matriz[1]
# w4 = matriz[3] - projeção de matriz[3] sobre matriz[0] - projeção de matriz[3] sobre matriz[1] - projeção de matriz[3] sobre matriz[2]
# Definindo projeção de V sobre W = ((V*W)/||W||**2)W
# É necessário definir produto interno
# É necessário definir norma de um vetor
def produto_interno(a,b):
    c = 0
    for i in range(len(a)):
        c += a[i]*b[i]
    return c
def norma(b):
    d = 0
    for i in range(len(b)):
        d += b[i]**2
    d = d**(1/2)
    return d
def arredondamento(a):
    matriz = []
    for i in range(len(a)):
        matrizlinha = []
        for j in range(len(a[0])):
            e = round(a[i][j],2)
            matrizlinha.append(e)
        matriz.append(matrizlinha)
    return matriz
def projeção(a,b):
    #Definindo projeção de a sobre b = ((a*b)/||b||**2)b  
    c = 0
    for i in range(len(a)):
        c += a[i]*b[i] #c é produto interno
    d = 0
    for i in range(len(a)):
        d += b[i]**2
    d = d**(1/2) #d é norma
    escalar = (c/(d)**2)
    vetor = []
    for i in range(len(a)):
        vetor.append(escalar*b[i])
    return vetor
#projeção de a sobre b => projeção(a,b)
# base[0] = matriz[0]
# base[1] = matriz[1] - projeção de matriz[1] sobre matriz[0]
# base[2] = matriz[2] - projeção de matriz[2] sobre matriz[0] - projeção de matriz[2] sobre matriz[1]
# base[3] = matriz[3] - projeção de matriz[3] sobre matriz[0] - projeção de matriz[3] sobre matriz[1] - projeção de matriz[3] sobre matriz[2]
while True:
    print("1 - Calcular a norma\n2 - Calcular o produto interno\n3 - Calcular a base ortogonal\n4 - Sair")
    opção = int(input("Digite a opção: "))
    matriz = []
    linhas = int(input("Digite o número de vetores: "))
    while linhas <= 0:
        linhas = int(input("Número invalido, digite novamente: "))
    for i in range(linhas):
        x = input(f"Digite o {i+1}º vetor: ").split()
        if len(matriz) > 0 :
            while len(x) != len(matriz[0]):
                x = input("Vetor invalido! Digite novamente: ").split()
        valores = [int(val) for val in x]
        matriz.append(valores)
    if opção == 4:
        break
    elif opção == 3: 
        base = []
        w = []
        for i in range(len(matriz)):
            w = []
            var = []
            for j in range(len(base)):
                if len(var) > 0:
                    for k in range(len(var)):
                        a = projeção(matriz[i],base[j])
                        var[k] += a[k] 
                else:
                        var += projeção(matriz[i],base[j])
            if len(var) > 0:
                for k in range(len(matriz[1])):
                    e = matriz[i][k] - var[k] 
                    w.append(e)
            else:
                w = matriz[i]
            base.append(w)

        print(f"A base ortogonal é: {arredondamento(base)}")
    elif opção == 1:
        print(f"A norma de {matriz[0]} é: {norma(matriz[0])}")
    elif opção == 2:
        print(f"O produto interno de {matriz[0]} entre {matriz[1]} é {round(produto_interno(matriz[0],matriz[1]), 2)}")
    else:
        print("Opção invalida!")