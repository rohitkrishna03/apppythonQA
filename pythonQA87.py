class Flower:
    
    def __init__(self, name: str, petals: int, price: float):
        self._name = name
        self._petals= petals
        self._price= price
    def get_name(self) -> str:
        return self._name
    def set_name(self,name:str):
        self._name= name 
    def get_petals(self) ->int:
        return self._petals
    def set_petals(self,petals:int):
        self._petals=petals
    def get_price(self) -> float:
        return self._price
    def set_price(self, price:float):
        self._price=price
        
flower =Flower("rose", 5 ,3.5)
print("flower name:", flower.get_name())
print("flower petals:", flower.get_petals())
print("flower price:", flower.get_price())

# we can alos set new values by
flower.set_name("lily")
flower.set_petals(6)
flower.set_price(2.5)

print("updated flower name: " ,flower.get_name())
print("updated flower petals:", flower.get_petals())
print("updated flower price: ",flower.get_price())

 
        
        