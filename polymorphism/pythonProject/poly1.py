class Party:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def __gt__(self, other):
        if self.money>other.money:
            return True
        else:
            return False

p1=Party("vaishu",10000)
p2=Party("sneha",20000)

if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")