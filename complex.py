class complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def __str__(self):
        if self.image>=0:
            return f"{self.real}+{self.image}i"
        else:
            return f"{self.real}{self.image}i"
    def add (complex1,complex2):
        return complex(complex1.real+complex2.real,complex1.image+complex2.image)
    def add_complex_objects(*complex1):
        total=complex(0,0)
        for complex in complex1:
            total=add(total,complex)
        return total
c1=complex(3,4)
c2=complex(5,-6)
print(c1)
print(c2)