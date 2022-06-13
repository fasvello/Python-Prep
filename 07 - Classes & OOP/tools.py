class Tools:
    def __init__(self) -> None:
        pass

    def is_primo(self, x):
        res = True
        try:
            for i in range(2, x - 1):
                if x % i == 0:
                    res = False
                    break
            return res
        except TypeError:
            print("error: debe ser entero")

    def num_moda2(self, lista, valor):
        numeros = []
        cantidad = []
        maximos = []
        for n in lista:
            if n not in numeros:
                numeros.append(n)
                cantidad.append(0)
        for pos, num in enumerate(numeros):
            for i in lista:
                if i == num:
                    cantidad[pos] += 1
        for pos, num in enumerate(numeros):
            if cantidad[pos] == max(cantidad):
                maximos.append(num)
        print(max(cantidad))
        print(maximos)
        if valor == "max":
            print(max(maximos))
        else:
            print(min(maximos))
