def sell_tickets():

    total_tickets = 20

    max_tickets = 4

    total_tickets_sold = 0

    total_buyers = 0

    while total_tickets_sold < total_tickets:
        try:
            num_tickets = int(input("enter the number of tickets you want to buy (1-4): "))
            if 1 <= num_tickets <= max_tickets:
                if total_tickets_sold + num_tickets <= total_tickets:
                    total_tickets_sold += num_tickets
                    total_buyers += 1
                    remaining_tickets = total_tickets - total_tickets_sold
                    print(f"{num_tickets} tickets purchased.")
                    print(f"remaining tickets: {remaining_tickets}")
                else:
                    print("not enough tickets available.")
            else:
                print("you can only buy 1-4 tickets.")
        except ValueError:
            print("please enter 1-4.")

    print(f"All tickets sold out! Total buyers: {total_buyers}")

sell_tickets()