"""
Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

Order Number	Book Title and Author	Quantity	Price per Item
34587	Learning Python, Mark Lutz	4	40.95
98762	Programming Python, Mark Lutz	5	56.80
77226	Head First Python, Paul Barry	3	32.95
88112	Einführung in Python3, Bernd Klein	3	24.99


Write a Python program, which returns a list with 2-tuples.
Each tuple consists of a the order number and the product of the price per items and the quantity.
The product should be increased by 10,- € if the value of the order is smaller than 100,00 €.
Write a Python program using lambda and map.
"""
def find_cost(orders):
    order = lambda x: x[0]
    quantity = lambda x: x[2]
    price = lambda x: x[3]
    cost = lambda x, y: x * y if x * y >= 100 else x * y + 10

    order_map = map(order, orders)
    quantity_list = list(map(quantity, orders))
    price_list = list(map(price, orders))
    cost_map = map(cost, quantity_list, price_list)

    result = []
    for _ in range(len(orders)):
        single_result = next(order_map), next(cost_map)
        result.append(single_result)

    return result


def find_costs(orders):
    result = list(map(lambda x: (x[0], x[2]*x[3] if x[2]*x[3] > 100 else x[2]*x[3]+10), orders))
    return result


orders = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
          [98762, 'Programming Python, Mark Lutz', 5, 56.80],
          [77226, 'Head First Python, Paul Barry', 3, 32.95],
          [88112, 'Einführung in Python3, Bernd Klein', 3, 24.99]]


print(find_cost(orders))

print('for compact one')

print(find_costs(orders))



