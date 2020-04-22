from textwrap import dedent

welcome = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
order_item = """
***********************************
** What would you like to order? **
***********************************
"""

menu = {
    "Appetizers": 
    {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0
    },
    "Entrees": 
    {
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A Literal Garden": 0
    },
    "Desserts": 
    {
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0
    },
    "Drinks": 
    {
        "Coffee": 0,
        "Tea": 0,
        "Soda": 0
    },
}

def display_menu():
    for category in menu:
        print(dedent(f"""\n
        {category}
        -----------"""))
        for item, quantity in menu[category].items():
            print(item) 

def placed_order(user_input):
    for category in menu:
        current_category = menu[category]
        if user_input.lower() in map(str.lower, current_category.keys()):
            quantity = current_category [user_input]
            quantity += 1
            current_category[user_input]= quantity
            print (f"{quantity} order of {user_input} have been added to your meal")
            return
    print(f"{user_input} does not exist in the menu.")

if __name__ == '__main__':
    print(dedent(welcome))
    display_menu()
    order = input(order_item)
    while order != 'quit':
        placed_order(order)
        order = input(order_item)

#order = order.title()

