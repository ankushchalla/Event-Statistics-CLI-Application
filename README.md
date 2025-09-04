# Event Statistics CLI Application

## 1. Introduction

This is a basic command-line application that allows users to retrieve and view statistics about events. The application connects to a MySQL database, loads data into it, fetches relevant data based on user input, and displays it in a human-readable format through the console.

---
## 2. How to Run

### Prerequisites

- Python 3.x installed  
- A locally running MySQL database  
- Required Python packages (install with `pip install -r requirements.txt`)

### Running the Application

1. Ensure your MySQL server is up and running.
2. Open your terminal and navigate to the root directory of the project.
3. Run the application using:

```bash
python main.py
```
4. (Optional) Provide database connection parameters as command-line arguments using key=value format:
```bash
python main.py user=user port=3306
```

### Default Database Configuration

If no command-line arguments are provided, the application uses the following default credentials:
* user: `root`
* password: `password`
* host: `localhost`
* port: `3306`
* database: `ticket_system`

### Using the application
Once the application is running:
1. You will see a list of numbered options.
2. Type the number corresponding to the option you'd like to select and press Enter.
3. The application will retrieve the requested data, format it, and display the results in the console.
4. You can continue selecting different options or exit anytime by pressing Ctrl-C.

### Command line execution log for an example job run
```plaintext
$ python main.py port=3306
DEBUG:data.load:DB_CONNECTION_ESTABLISHED host=localhost port=3306 database=ticket_system
***LOADING DATA***
INFO:data.load:TABLE_CREATION_SUCCESS
INFO:data.load:CSV_INGESTION_SUCCESSFUL linesRead=6
INFO:data.load:DB_INSERT_SUCCESSFUL recordsInserted=6


(0) - Get the top 3 selling tickets
(1) - Get the total tickets sold for each event type
(2) - Get summary of all events
Enter number corresponding to desired action above. Ctr-C to exit: 0

Top 3 selling tickets:
  - event_name=Christmas Spectacular, total_tickets_sold=5, total_revenue=$450
  - event_name=Washington Spirits vs Sky Blue FC, total_tickets_sold=5, total_revenue=$295
  - event_name=The North American International Auto Show, total_tickets_sold=4, total_revenue=$140


(0) - Get the top 3 selling tickets
(1) - Get the total tickets sold for each event type
(2) - Get summary of all events
Enter number corresponding to desired action above. Ctr-C to exit: 2

Event summaries:
  - event_name=Carlisle Ford Nationals, event_date=2020-09-30, event_city=Carlisle, total_tickets_sold=1, total_revenue=43  
  - event_name=Christmas Spectacular, event_date=2020-10-05, event_city=New York, total_tickets_sold=5, total_revenue=450   
  - event_name=The North American International Auto Show, event_date=2020-09-01, event_city=Michigan, total_tickets_sold=4, total_revenue=140
  - event_name=Washington Spirits vs Sky Blue FC, event_date=2020-08-30, event_city=Washington DC, total_tickets_sold=5, total_revenue=295


(0) - Get the top 3 selling tickets
(1) - Get the total tickets sold for each event type
(2) - Get summary of all events
Enter number corresponding to desired action above. Ctr-C to exit: Exiting...
```
