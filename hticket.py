def hticketdetecrot():
    happyTickets = 0
    for i in range(100000, 900001):
        ticket = [i]
        ticketString = str(ticket)
        if int(ticketString[1])+int(ticketString[2])+int(ticketString[3]) == int(ticketString[4])+int(ticketString[5])+int(ticketString[6]):
             happyTickets += 1
    return happyTickets


if __name__ == "__main__":
    coutTickets = hticketdetecrot()
    print(coutTickets)