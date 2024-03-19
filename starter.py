import sqlite3

conn = sqlite3.connect('calendar.db')
cursor = conn.cursor()

# Create the assignments table
cursor.execute('''CREATE TABLE IF NOT EXISTS assignments (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    deadline DATE,
                    days_before_deadline INTEGER
                )''')

# Create the assignment_parts table
cursor.execute('''CREATE TABLE IF NOT EXISTS assignment_parts (
                    id INTEGER PRIMARY KEY,
                    assignment_id INTEGER,
                    part_name TEXT,
                    duration_hours INTEGER,
                    FOREIGN KEY (assignment_id) REFERENCES assignments(id)
                )''')

# Insert data into the assignment_parts table
cursor.executemany('''INSERT INTO assignment_parts (assignment_id, part_name, duration_hours) VALUES (?, ?, ?)''',
                   [(1, 'Part A', 2), (1, 'Part B', 3), (1, 'Part C', 1)])

# Create the user_input table
cursor.execute('''CREATE TABLE IF NOT EXISTS user_input (
                    id INTEGER PRIMARY KEY,
                    hours_available_week INTEGER
                )''')

# Create the assignment_part_relationship table
cursor.execute('''CREATE TABLE IF NOT EXISTS assignment_part_relationship (
                    id INTEGER PRIMARY KEY,
                    assignment_id INTEGER,
                    part_id INTEGER,
                    part_name TEXT,
                    FOREIGN KEY (assignment_id) REFERENCES assignments(id),
                    FOREIGN KEY (part_id) REFERENCES assignment_parts(id)
                )''')

# Commit the transaction and close the connection
conn.commit()
conn.close()
