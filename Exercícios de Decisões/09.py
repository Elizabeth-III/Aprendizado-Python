# Faça um Programa que leia três números e mostre-os em ordem decrescente.


def maior(um, outro):
    return um if um > outro else outro



def menor(um, outro):
    return um if um < outro else outro


v1 = int(input("Informe o primeiro valor"))
v2 = int(input("Informe o segundo valor"))
v3 = int(input("Informe o terceiro valor"))
print("Variáveis v1,v2,v3 valem respectivamente", v1, v2, v3)
w1, w2, w3 = v1, v2, v3
v1 = maior(w1, maior(w2, w3))
v2 = menor(menor(maior(w2, w3), maior(w2, w1)), menor(maior(w1, w3), maior(w1, w2)));
v3 = menor(w1, menor(w2, w3))
print("Após a ordenação")
print("Variáveis v1,v2,v3 valem respectivamente", v1, v2, v3)
print("Em ordem decrescente ficam", v3, v2, v1)