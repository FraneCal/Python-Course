
products = {
    "001": {
        "Name": "Laptop",
        "Short Description": "High-performance laptop with SSD storage",
        "Price": 1200,
        "State": 1500
    },
    "002": {
        "Name": "Smartphone",
        "Short Description": "Flagship smartphone with a powerful camera",
        "Price": 900,
        "State": 500
    },
    "003": {
        "Name": "Headphones",
        "Short Description": "Wireless noise-canceling headphones",
        "Price": 250,
        "State": 100
    },
    "004": {
        "Name": "Smart TV",
        "Short Description": "Ultra HD Smart TV with built-in streaming apps",
        "Price": 1500,
        "State": 5
    },
    "005": {
        "Name": "Fitness Tracker",
        "Short Description": "Waterproof fitness tracker with heart rate monitor",
        "Price": 100,
        "State": 2
    },
    "006": {
        "Name": "Digital Camera",
        "Short Description": "DSLR camera with interchangeable lenses",
        "Price": 800,
        "State": 2000
    },
    "007": {
        "Name": "Wireless Speaker",
        "Short Description": "Portable wireless speaker with long battery life",
        "Price": 150,
        "State": 443
    },
    "008": {
        "Name": "Gaming Console",
        "Short Description": "Next-generation gaming console with 4K graphics",
        "Price": 500,
        "State": 421
    },
    "009": {
        "Name": "Coffee Maker",
        "Short Description": "Programmable coffee maker with built-in grinder",
        "Price": 80,
        "State": 123
    },
    "010": {
        "Name": "Vacuum Cleaner",
        "Short Description": "Robot vacuum cleaner with smart navigation",
        "Price": 300,
        "State": 872
    }
}


def all_products():
    header = ["Product ID", "Name", "Short Description", "Price", "State"]
    # Reminder for myself
    # The "<" ensures left alignment, and the number next to it defines the width of each column
    print("{:<15} {:<20} {:<50} {:<10} {:<10}".format(*header))
    print("-" * 108)

    for product_id, product_info in products.items():
        print("{:<15} {:<20} {:<50} {:<10} {:<10}".format(
            product_id,
            product_info["Name"],
            product_info["Short Description"],
            product_info["Price"],
            product_info["State"]
        ))
    print()
    print()


def single_product():
    user_input = input('Enter the ID (e.g. 001): ')
    header = ["Product ID", "Name", "Short Description", "Price", "State"]
    print("{:<15} {:<20} {:<50} {:<10} {:<10}".format(*header))
    print("-" * 108)
    print("{:<15} {:<20} {:<50} {:<10} {:<10}".format(
        user_input,
        products[user_input]["Name"],
        products[user_input]["Short Description"],
        products[user_input]["Price"],
        products[user_input]["State"]
    ))
    print()
    print()


def add_a_product():
    next_ID = str(f'0{len(products) + 1}')
    product_name = input('Enter the product name: ')
    product_description = input('Enter a short description: ')
    product_price = input('Enter the price: ')
    product_state = input('Enter the state: ')
    products.update({
        next_ID: {
            "Name": f'{product_name}',
            "Short Description": f'{product_description}',
            "Price": f'{product_price}',
            "State": f'{product_state}',
        }
    })
    print('Product added successfully.')

    all_products()


def change_the_state():
    while True:
        try:
            product_id = input('Enter the ID of the product: ')
            new_state = input('Enter the new state of the product: ')

            if product_id in products:
                products[product_id]['State'] = new_state
                print('Product state updated successfully.')
                break
            else:
                print('Invalid product ID.')
        except ValueError:
            print('Invalid product ID.')

    print()
    all_products()

