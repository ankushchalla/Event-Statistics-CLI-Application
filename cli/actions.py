class GetTopSellingTickets:
    def get_view():
        return "Get the top 3 selling tickets"
    
    def run(connection):
        cursor = connection.cursor()
        query = ("""
                with event_ticket_totals as (
                    select event_id, sum(num_tickets) total_tickets_sold, sum(num_tickets * price) total_revenue
                    from ticket
                    group by event_id
                )
                select distinct t.event_name, ett.total_tickets_sold, ett.total_revenue
                from ticket t
                join event_ticket_totals ett on t.event_id = ett.event_id
                order by total_revenue desc
                limit 3
                """)
        cursor.execute(query)
        print("\nTop 3 selling tickets:")
        for (event_id, total_tickets_sold, total_revenue) in cursor:
            print(f"  - event_name={event_id}, total_tickets_sold={total_tickets_sold}, total_revenue=${total_revenue}")

class GetTotalTicketsSoldPerEventType:
    def get_view():
        return "Get the total tickets sold for each event type"
    
    def run(connection):
        cursor = connection.cursor()
        query = (
            """
            with event_ticket_totals as (
                select event_type, sum(num_tickets) total_tickets_sold
                from ticket
                group by event_type 
            )

            select distinct t.event_type, ett.total_tickets_sold
            from ticket t
            join event_ticket_totals ett on t.event_type = ett.event_type
            order by total_tickets_sold desc
            """
        )
        cursor.execute(query)
        print("\nTotal tickets sold for each event type:")
        for (event_type, total_tickets_sold) in cursor:
            print(f"  - event_type={event_type}, total_tickets_sold={total_tickets_sold}")

class GetEventSummary:
    def get_view():
        return "Get summary of all events"
    
    def run(connection):
        cursor = connection.cursor()
        query = (
            """
            with event_ticket_totals as (
                select event_id, sum(num_tickets) total_tickets_sold, sum(num_tickets * price) total_revenue
                from ticket
                group by event_id
            )
            select distinct t.event_name, t.event_date, t.event_city, ett.total_tickets_sold, ett.total_revenue
            from ticket t
            join event_ticket_totals ett on t.event_id = ett.event_id
            order by t.event_name
            """
        )
        cursor.execute(query)
        print("\nEvent summaries:")
        for (event_name, event_date, event_city, total_tickets_sold, total_revenue) in cursor:
            print(f"  - event_name={event_name}, event_date={event_date}, event_city={event_city}, total_tickets_sold={total_tickets_sold}, total_revenue={total_revenue}")


ACTIONS = [GetTopSellingTickets, GetTotalTicketsSoldPerEventType, GetEventSummary]
