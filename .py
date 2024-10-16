class parent:
    def __init__(self,eye,hair):
        self.eye = eye
        self.hair = hair


class child(parent):
    def __init__(self,parent):
        super().__init__(parent.eye,parent.hair)



father = parent('Black','brown')
son = child(father)

#print(son.eye)

class a:
    a = 4
    b = 5
    c = 7
    def hello(self):
        print('hello')

class b(a):
    pass

obj = b()

print(obj.a)
