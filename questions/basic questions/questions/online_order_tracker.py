
class Order:
    def __init__(self, order_id, item_name, price, status="Pending"):
        self.order_id = order_id
        self.item_name = item_name
        self.price = price
        self.status = status

    def __str__(self):
        return f"Order ID: {self.order_id}, Item: {self.item_name}, Price: ₹{self.price}, Status: {self.status}"

class OrderManager:
    def __init__(self):
        self.orders = []

   
    def add_order(self, order):
        self.orders.append(order)
        print(f"Order {order.order_id} added successfully!")

    def update_status(self, order_id, new_status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = new_status
                print(f"Order {order_id} status updated to {new_status}")
                return
        print("Order not found!")

    def display_delivered_orders(self):
        print("\nDelivered Orders:")
        for order in self.orders:
            if order.status == "Delivered":
                print(order)


manager = OrderManager()

manager.add_order(Order(101, "Laptop", 55000))
manager.add_order(Order(102, "Headphones", 2000))
manager.add_order(Order(103, "Mobile Phone", 30000))

manager.update_status(101, "Shipped")
manager.update_status(101, "Delivered")
manager.update_status(103, "Delivered")

manager.display_delivered_orders()
