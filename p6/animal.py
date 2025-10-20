class Animal:
    def __init__(self):
        return
    
    # method
    def bersuara(self):
        print('Ini adalah suara hewan.')


class Cat(Animal):
    def __init__(self):
        return
    
    def bersuara(self):
        super().bersuara() # Memanggil fungsi parent
        print('Suara kucing: Meong')
    

class Dog(Animal):
    def __init__(self):
        return
    
    def bersuara(self):
        super().bersuara()
        print('Guk guk')