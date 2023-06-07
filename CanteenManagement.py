class Canteen:
    def __init__(self):
        self.menu = [
            {"id": 1, "name": "Chapati", "price": 4},
            {"id": 2, "name": "Rice", "price": 25},
            {"id": 3, "name": "Dal", "price": 15},
            {"id": 4, "name": "Aloo Matar", "price": 20},
            {"id": 5, "name": "Paneer", "price": 30},
            {"id": 6, "name": "Chicken Curry", "price": 40},
            {"id": 7, "name": "Fish Curry", "price": 35},
            {"id": 8, "name": "Biryani", "price": 110}
        ]
        self.order = []

    def show_menu(self):
        print("------------- MENU -------------")
        print("ID\tNAME\t\t\t\tPRICE")
        for item in self.menu:
            name = item['name'].ljust(20)
            print(f"{item['id']}\t{name}\t{item['price']:>3} Rs.")
        print("--------------------------------")

    def place_order(self):
        self.show_menu()
        while True:
            print("Enter the ID of the item you want to order (or 0 to exit):")
            item_id = int(input())
            if item_id == 0:
                break
            item = self.find_item(item_id)
            if item:
                print(f"How many plates {item['name']} do you want?")
                quantity = int(input())
                self.order.append({"item": item, "quantity": quantity})
                print(f"You added {quantity} {item['name']} to your order.")
            else:
                print("Invalid item ID. Please try again.")

    def find_item(self, item_id):
        for item in self.menu:
            if item['id'] == item_id:
                return item
        return None

    def calculate_bill(self):
        total_price = 0
        for order_item in self.order:
            item = order_item["item"]
            quantity = order_item["quantity"]
            total_price += item["price"] * quantity
        return total_price

    def print_bill(self, total_price, name):
        print("----------- BILL --------------")
        for order_item in self.order:
            item = order_item["item"]
            quantity = order_item["quantity"]
            print(f"{item['name']} (x {quantity}) - {item['price']} Rs. each")
        print("-------------------------------")
        print(f"Total Bill: {total_price} Rs.")
        print(f"Thank you, {name}, for using the canteen system. Have a great day!")


if __name__ == "__main__":
    print("Welcome to the college canteen!")
    print("Please enter your name:")
    name = input()
    print(f"Hello {name}, welcome to the canteen!")
    canteen = Canteen()
    canteen.place_order()
    total_bill = canteen.calculate_bill()
    canteen.print_bill(total_bill, name)

