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

def close_ticket(tickets, ticket_id):
    """Change a ticket's status to Closed by matching its id."""
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "Closed"
        return tickets

close_ticket(tickets, 1)
view_tickets(tickets)