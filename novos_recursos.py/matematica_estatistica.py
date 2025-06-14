import math
import statistics

print('math.prod -> retorna o produto de um container numérico')
nums_v1 = [2,3,6,8]
nums_v2 = (2,3,6,8)
nums_v3 = {2,3,6,8}

print(math.prod(nums_v1))
print(math.prod(nums_v2))
print(math.prod(nums_v3))
print()

print('math.isqrt -> retorna a parte interia da raiz quadrada')
print(math.sqrt(9))
print(math.isqrt(9))
print(math.sqrt(17))
print(math.isqrt(17))
print()

print('math.dist -> retorna a distância euclidiana entre dois pontos 3D ou 2D')
p3d1 = [12,50,40]
p3d2 = (6,7,13)
p2d1 = (12,50)
p2d2 = [6,7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))
print()

print('math.hyport -> retorna a hipotenusa ou nome euclidiana')
print(math.hypot(*p3d1))
print(math.hypot(*p2d1))
print()

print('statistics.fmean -> calcula a média de números reais')
valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1,6,3,89]
print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))
print()

print('statistics.geometric_mean -> calcula a média geometrica de números reais')
print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))
print()

print('statics.multimode -> retorna o valor mais frequente de uma sequência')
seq1 = 'Geek University'
seq2 = [3,5,3,8,7,8,5,3]
seq3 = [1,2,3,1,2,3,4,5,6]
print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
print()
