#Creator: RMW 12/17/22

def find_sum (num1, num2): #Finds sum of num1 & num2
    return num1 + num2

def print_reciept (total): #prints reciept
    return (f'Your total price is ${total}')

def check_out_your_two_products (price1, price2): #combines products which gives the total cost
    return print_reciept (find_sum (price1, price2))
    pt(find_sum(price1, price2))

print(check_out_your_two_products(44, 56) == 'the price of your two products is $100')
print(check_out_your_two_products(21, 33) == 'the price of your two products is $54')
print(check_out_your_two_products(99, 21) == 'the price of your two products is $120')
print(check_out_your_two_products(12, 5) == 'the price of your two products is $17')
print(check_out_your_two_products(4, 9) == 'the price of your two products is $13')