tickets = []

def add_ticket(tickets):
    """Create a new ticket and add to the tickets list."""
    title = input("Ticket Title: ")
    priority  = input("Priority (Low/Medium/High): ")

    ticket = {
        "id": len(tickets) + 1,
        "title": title,
        "priority": priority, 
        "status": "Open"
        }

    tickets.append(ticket)
    return tickets

def view_tickets(tickets):
    """Print all tickets in readable format."""
    for ticket in tickets:
        print(ticket["id"])
        print(ticket["title"])
        print(ticket["priority"])
        print(ticket["status"])

def close_ticket(tickets, ticket_id):
    """Change a ticket's status to Closed by matching its id."""
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "Closed"
        return tickets

while True:
    print("\n1. Add tickets")
    print("2. View tickets")
    print("3. Closes tickets")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        tickets = add_ticket(tickets)
    elif choice == "2":
        view_tickets(tickets)
    elif choice == "3":
        ticket_id = int(input("Enter ticket ID to close: "))
    elif choice == "4":
        break



