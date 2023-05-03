print("Digite dois valores")
x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))

while x != y:
    if x > y:
        print("DECRESCENTE")
    else:
        print("CRESCENTE")

    print("Digite outros dois valores")
    x = int(input("Primeiro valor: "))
    y = int(input("Segundo valor: "))
