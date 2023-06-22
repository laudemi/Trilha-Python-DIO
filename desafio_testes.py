#Teste 1 -------------------------------------------------------------

# C = int(input()) 
# for i in range (C): 
#     # n = int(input())
#     if n <= 8000:
#         print("inseto!")
#     else:
#         print("Mais de 8000!")


T = int(input())

for i in range(T):
    N, K = map(int,input().split())
    cheia = N // K # faz uma divisão inteira
    vazia = N % K # resto  da divisão
    garrafas = cheia + vazia
    print(garrafas)

#Teste 2 ----------------------------------------------------------
a = input() 
b = input() 
c = input() 

if a == 'vertebrado': 
    if b ==  'mamifero':
        if c == 'onivoro':
            print('homem')
        
        if c == 'herbivoro' :
            print('vaca')
    
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        
        if c == 'onivoro':
            print('pomba')
    
 
# Teste 3 --------------------------------------------
elif a == 'invertebrado':
    if b ==  'inseto':
        if c == 'hematofago':
            print('pulga')
        
        if c == 'herbivoro' :
            print('lagarta')
    
    if b == 'anelideo':
        if c == 'hematofago':
            print('sanguessuga')
        
        if c == 'onivoro':
            print('minhoca')