class GerPrimo:
    def __init__(self):
        self.primo = 0

    def proximo(self):
        if self.primo == 0:
            self.primo = 2
            return self.primo
        else:
            i = self.primo
            while True:
                i += 1
                divisores = 0
                for j in range(1, i+1):
                    if i % j == 0:
                        divisores += 1
                if divisores == 2:
                    self.primo = i
                    return self.primo

primo = GerPrimo()
print(primo.proximo())
print(primo.proximo())
print(primo.proximo())
print(primo.proximo())
print(primo.proximo())
print(primo.proximo())
print(primo.proximo())
print(primo.proximo())
print(primo.proximo())