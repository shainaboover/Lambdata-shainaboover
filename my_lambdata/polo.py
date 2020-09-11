# attributes / properties

# behaviors /methods

# define new class
class Polo():
    def __init__(self, color, size, price, style='Normal'):
        self.color = color
        self.size = size
        self.price = price
        self.style = style
    
    def fold(self):
        print(f'Folding the {self.size.upper()} {self.color.upper()} Polo')





if __name__ == '__main__':

    # new object that invokes polo class
    # pass in some attributes, positional arguments
    polo = Polo('Blue', 'Lg', 49.99)
    print(polo.color, polo.size, polo.price)
    polo.fold()

    # alternatively pass in parameters, named arguments
    polo2 = Polo(color='Red', size='Sm', price=39.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()

    polo3 = Polo(color='Green', size='Md', price=45.99, style='Slim Fit')
    print(polo3.color, polo3.size, polo3.price)
    polo3.fold()

    breakpoint()