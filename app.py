import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, data TEXT)''')

# Function to insert data

def insert_data(data):
    cursor.execute('''INSERT INTO records (data) VALUES (?)''', (data,))
    conn.commit()

# Example usage
insert_data('Sample data record')

# Close connection
conn.close()