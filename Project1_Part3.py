#!/usr/bin/env python
# coding: utf-8

# In[2]:


class shop():
    def __init__(self,name,type): 
        self.name=name
        self.type=type
    def info(self):
        print(f"Name:{self.name},Type:{self.type}")

class clothingstore(shop):
    def __init__(self,name,type,item_name,size,color):
        super().__init__(name,type)
        self.item_name=item_name
        self.size=size
        self.color=color
    def info(self):
        return (
            f"{super().info()}, Item: {self.item_name}, "
            f"Size: {self.size}, Color: {self.color}"
        )

class Fruit(shop): 
    def __init__(self,name,type,fruit_name,price,quantity):
        super().__init__(name,type)
        self.fruit_name=fruit_name
        self.price=price
        self.quantity=quantity
    def info(self):
        return (
            f"{super().info()}, Fruit: {self.fruit_name}, "
            f"Price: ${self.price}, Quantity: {self.quantity}"
        )


# In[ ]:




