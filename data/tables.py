TABLES = {}
TABLES['ticket'] = (
    "create table if not exists ticket (" + 
    "ticket_id INT PRIMARY KEY," + 
    "trans_date DATE," + 
    "event_id INT," + 
	"event_name VARCHAR(50)," + 
	"event_date DATE," + 
	"event_type VARCHAR(50)," + 
	"event_city VARCHAR(50)," +  
	"customer_id INT, " + 
	"price DECIMAL, " + 
	"num_tickets INT" + 
     ") ENGINE=InnoDB"
)
