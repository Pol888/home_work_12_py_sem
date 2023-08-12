class Factorial:
    def __init__(self, k):
        self.k = k
        self.__list_k = []


    def __call__(self, f_n):
        result = sum(list(range(1, f_n + 1)))
        self.__list_k.append([f_n, result])
        if len(self.__list_k) > self.k:
            del self.__list_k[0]

    @property
    def getter_list_k(self):
        for i in self.__list_k:
            yield f'factorial- |{i[0]}| = {i[1]}'


f = Factorial(2)
f(5)
f(9)
f(10)

print(*f.getter_list_k, sep=',\n')

''' => 
       factorial- |9| = 45,
       factorial- |10| = 55'''
