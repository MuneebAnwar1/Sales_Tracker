# Function to gather product and sales information from the user
def taking_input():
    # Prompt user for the number of products with input validation
    while True:
        try:
            num_of_products = int(input("How many products do you have: "))
            break  # Exit loop if valid input is provided
        except ValueError:
            print("Please enter a valid number.")  # Error message for invalid input

    products = []  # List to store product names and prices as tuples
    sales = {}  # Dictionary to store quantities sold for each product

    # Loop to collect details for each product
    for i in range(num_of_products):
        # Prompt for product name with validation (only alphabetic characters allowed)
        while True:
            name = input(f"Enter the product name {i+1}: ")
            if name.isalpha():  # Check if the name consists of alphabetic characters
                break  # Exit loop if valid name is entered
            else:
                print("Please enter a valid product name (alphabetic characters only):")
        
        # Prompt for product price with validation (only integers allowed)
        while True:
            try:
                price = int(input(f"Enter your price for {name}: "))
                break  # Exit loop if valid price is entered
            except ValueError:
                print("Please enter a valid number.")  # Error message for invalid price

        # Store product name and price as a tuple in the products list
        products.append((name, price))

        # Prompt for quantity sold with validation (only integers allowed)
        while True:
            try:
                quantity_sold = int(input(f"How many {name}s have you sold: "))
                break  # Exit loop if valid quantity is entered
            except ValueError:
                print("Please enter a valid number.")  # Error message for invalid quantity
        
        # Record the quantity sold in the sales dictionary with the product name as the key
        sales[name] = quantity_sold

    # Return the list of products and the sales dictionary
    return products, sales

# Function to display sales information and calculate total revenue
def shope():
    # Call the taking_input function to collect product and sales data
    products, sales = taking_input()
    content = []  # List to store formatted sales information for file writing

    # Iterate through each product in the products list
    for i in products:
        name = i[0]  # Extract product name from the tuple
        price = i[1]  # Extract product price from the tuple
        
        # Retrieve the quantity sold from the sales dictionary using the product name
        sold = sales.get(name, None)  # Returns None if the product is not found
        
        # If no sales data is found, display a message indicating no sales
        if sold is None:
            print(f"Product name: {name}, Price: {price}, Quantity sold: No sales available")
        
        # If sales data is found, calculate and display total sales revenue
        else:
            revenue = price * sold  # Calculate total sales revenue
            print(f"Product name: {name}, Price: {price}, Total sales: {revenue}")
            # Append formatted sales information to the content list for file writing
            content.append(f"Product name: {name}, Price: {price}, Total sales: {revenue}")

    # Write the sales information to a file
    with open('file2.txt', 'a', encoding='utf-8') as file:
        for y in content:
            file.write(y + "\n")  # Write each entry to the file
            file.flush()  # Ensure data is written to the file immediately

# Call the shope function to execute the program
shope()