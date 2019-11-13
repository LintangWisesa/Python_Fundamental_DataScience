# function fibonacci
def fibonacci(urut):
    if urut < 3:
        if urut == 0: return 0
        else: return 1
    else:
        return fibonacci(urut-1) + fibonacci(urut-2)

print(fibonacci(3))
print(fibonacci(6))
print(fibonacci(40))

# ==============================================

# class & obj fibonacci 
class Fibo:
    def urutan(self, urut):
        if urut < 3:
            if urut == 0: return 0
            else: return 1
        else:
            return self.urutan(urut-1) + self.urutan(urut-2)

Fibo = Fibo()
print(Fibo.urutan(3))
print(Fibo.urutan(6))
print(Fibo.urutan(40))