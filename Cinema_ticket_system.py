tickets = []

def book_ticket():
    name = input("Enter customer name: ")
    movie = input("Enter movie name: ")
    tickets.append({"name": name, "movie": movie})
    print("Ticket booked")

def view_tickets():
    for ticket in tickets:
        print(ticket["name"], "-", ticket["movie"])

def main():
    while True:
        print("1. Book Ticket")
        print("2. View Tickets")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
