class DLLNode:
    def __init__(self, item: str, price: float):
        self.item = item
        self.price = price
        self.next = None
        self.prev = None


class ShoppingCart:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_item(self, item: str, price: float):
        new_node = DLLNode(item, price)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Added {item} to cart")

    def delete_item(self, item: str):
        current = self.head
        while current:
            if current.item == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                print(f"Removed {item} from cart")
                return
            current = current.next
        print(f"{item} not found in cart")

    def sort_cart(self, by_price=False):
        if self.size <= 1:
            return

        items = []
        current = self.head
        while current:
            items.append((current.item, current.price))
            current = current.next

        items.sort(key=lambda x: x[1] if by_price else x[0])

        self.head = None
        self.tail = None
        for item, price in items:
            self.add_item(item, price)

    def print_cart(self):
        if not self.head:
            print("Cart is empty")
            return

        total = 0
        print("\nShopping Cart:")
        current = self.head
        while current:
            print(f"{current.item}: ${current.price:.2f}")
            total += current.price
            current = current.next
        print(f"Total: ${total:.2f}")


def cart_menu():
    cart = ShoppingCart()
    while True:
        print("\n=== SHOPPING CART MENU ===")
        print("1. Add item")
        print("2. Delete item")
        print("3. Sort cart")
        print("4. View cart")
        print("5. Back to main menu")

        cart_choice = input("Enter your choice (1-5): ")

        if cart_choice == "1":
            item = input("Enter item name: ")
            price = float(input("Enter price: "))
            cart.add_item(item, price)
        elif cart_choice == "2":
            item = input("Enter item to delete: ")
            cart.delete_item(item)
        elif cart_choice == "3":
            sort_by = input("Sort by price? (y/n): ").lower()
            cart.sort_cart(sort_by == 'y')
        elif cart_choice == "4":
            cart.print_cart()
        elif cart_choice == "5":
            break

cart_menu()