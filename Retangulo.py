import math

b: float = float(input("Digite a base do retangulo "))
a = float(input("Digite a altura do retangulo "))

area = b*a
perimetro = 2 * (b + a)
diagonal = math.sqrt(b*b + a*a)

print(f"area = {area:.4f}")
print(f"perimetro = {perimetro:.4f}")
print(f"diagonal = {diagonal:.4f}")