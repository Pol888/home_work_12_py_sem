import json

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

    def __enter__(self):
        self.o = open('new_file.json', 'w', encoding='utf-8')


    def __exit__(self, exc_type, exc_val, exc_tb):
        dict_j = [{key:val} for key, val in self.__list_k]
        json.dump(dict_j, self.o, indent=2)
        self.o.close()
        del self.o




f = Factorial(3)
with f:
    f(5)
    f(9)
    f(10)
    f(23)
    f(87)

print(*f.getter_list_k, sep=',\n')
