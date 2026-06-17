# Movie Hall Ticket Booking System
# Concepts Used:
# OOP, Linked List, BST, Queue, Searching, Recursion


# -------------------------------
# Booking Class
# -------------------------------
class Booking:
    def __init__(self, ticket_id, name, movie, seat_no):
        self.ticket_id = ticket_id
        self.name = name
        self.movie = movie
        self.seat_no = seat_no


# -------------------------------
# Linked List for Booking History
# -------------------------------
class BookingNode:
    def __init__(self, booking):
        self.booking = booking
        self.next = None


class BookingLinkedList:
    def __init__(self):
        self.head = None

    def add_booking(self, booking):
        new_node = BookingNode(booking)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display_bookings(self):
        if self.head is None:
            print("No booking history found.")
            return

        temp = self.head
        print("\n--- Booking History ---")
        while temp:
            b = temp.booking
            print(f"Ticket ID: {b.ticket_id}, Name: {b.name}, Movie: {b.movie}, Seat: {b.seat_no}")
            temp = temp.next


# -------------------------------
# BST for Fast Ticket Search
# -------------------------------
class BSTNode:
    def __init__(self, booking):
        self.booking = booking
        self.left = None
        self.right = None


class TicketBST:
    def __init__(self):
        self.root = None

    def insert(self, booking):
        self.root = self._insert_recursive(self.root, booking)

    def _insert_recursive(self, root, booking):
        if root is None:
            return BSTNode(booking)

        if booking.ticket_id < root.booking.ticket_id:
            root.left = self._insert_recursive(root.left, booking)
        else:
            root.right = self._insert_recursive(root.right, booking)

        return root

    def search(self, ticket_id):
        return self._search_recursive(self.root, ticket_id)

    def _search_recursive(self, root, ticket_id):
        if root is None:
            return None

        if root.booking.ticket_id == ticket_id:
            return root.booking

        if ticket_id < root.booking.ticket_id:
            return self._search_recursive(root.left, ticket_id)

        return self._search_recursive(root.right, ticket_id)

    def inorder_display(self):
        print("\n--- Tickets in Sorted Order ---")
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            b = root.booking
            print(f"Ticket ID: {b.ticket_id}, Name: {b.name}, Seat: {b.seat_no}")
            self._inorder_recursive(root.right)


# -------------------------------
# Queue for Waiting List
# -------------------------------
class WaitingQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, name):
        self.queue.append(name)
        print(f"{name} added to waiting list.")

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def display_queue(self):
        if self.is_empty():
            print("Waiting list is empty.")
            return

        print("\n--- Waiting List ---")
        for i, name in enumerate(self.queue, start=1):
            print(f"{i}. {name}")


# -------------------------------
# Main Movie Hall System
# -------------------------------
class MovieHall:
    def __init__(self, movie_name, total_seats):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.available_seats = list(range(1, total_seats + 1))
        self.booked_seats = []
        self.ticket_counter = 1000

        self.booking_history = BookingLinkedList()
        self.ticket_tree = TicketBST()
        self.waiting_list = WaitingQueue()

    def book_ticket(self, name):
        if len(self.available_seats) == 0:
            print("Seats full!")
            self.waiting_list.enqueue(name)
            return

        seat_no = self.available_seats.pop(0)
        self.booked_seats.append(seat_no)
        self.ticket_counter += 1

        booking = Booking(
            ticket_id=self.ticket_counter,
            name=name,
            movie=self.movie_name,
            seat_no=seat_no
        )

        self.booking_history.add_booking(booking)
        self.ticket_tree.insert(booking)

        print("\nTicket booked successfully!")
        print(f"Ticket ID: {booking.ticket_id}")
        print(f"Name: {booking.name}")
        print(f"Movie: {booking.movie}")
        print(f"Seat No: {booking.seat_no}")

    def search_ticket(self, ticket_id):
        booking = self.ticket_tree.search(ticket_id)

        if booking is None:
            print("Ticket not found.")
        else:
            print("\n--- Ticket Found ---")
            print(f"Ticket ID: {booking.ticket_id}")
            print(f"Name: {booking.name}")
            print(f"Movie: {booking.movie}")
            print(f"Seat No: {booking.seat_no}")

    def show_available_seats(self):
        print("\nAvailable Seats:")
        print(self.available_seats)

    def show_booked_seats(self):
        print("\nBooked Seats:")
        print(self.booked_seats)

    def show_booking_history(self):
        self.booking_history.display_bookings()

    def show_sorted_tickets(self):
        self.ticket_tree.inorder_display()

    def show_waiting_list(self):
        self.waiting_list.display_queue()


# -------------------------------
# Menu Program
# -------------------------------
def main():
    hall = MovieHall("Pushpa 2", 5)

    while True:
        print("\n========== Movie Hall Ticket Booking ==========")
        print("1. Book Ticket")
        print("2. Search Ticket")
        print("3. Show Available Seats")
        print("4. Show Booked Seats")
        print("5. Show Booking History")
        print("6. Show Tickets Sorted by Ticket ID")
        print("7. Show Waiting List")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            hall.book_ticket(name)

        elif choice == "2":
            ticket_id = int(input("Enter ticket ID: "))
            hall.search_ticket(ticket_id)

        elif choice == "3":
            hall.show_available_seats()

        elif choice == "4":
            hall.show_booked_seats()

        elif choice == "5":
            hall.show_booking_history()

        elif choice == "6":
            hall.show_sorted_tickets()

        elif choice == "7":
            hall.show_waiting_list()

        elif choice == "8":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


main()