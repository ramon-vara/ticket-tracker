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

tickets = add_ticket(tickets)
print(tickets)

def view_tickets(tickets):
    """Print all tickets in readable format."""
    for ticket in tickets:
        print(ticket["id"])
        print(ticket["title"])
        print(ticket["priority"])
        print(ticket["status"])

view_tickets(tickets)