class Tab:

    menu = {
        'wine': 500,
        'beer': 300,
        'soft_drink':150,
        'chicken':250,
        'desert':100,
        'veg_rolls':50,
        'nuggets':60
    }

    def __init__(self):
        self.total = 0
        self.items = [ ]

    def add(self,item):
        self.items.append(item) 
        self.total += self.menu[item]

    def print_bill(self,tax,service_charge):
        tax = (tax/100)*self.total
        service_charge = (service_charge/100)*self.total
        total = self.total + tax + service_charge 

        for item in self.items:
            print(f'{item:20} Rs.{self.menu[item]}')

        print(f'{"Total":20} Rs{total:.2f}')
