import sqlite3
import os

# Path to the database
db_path = os.path.join(os.getcwd(), 'db.sqlite3')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insert the migration record
cursor.execute("INSERT INTO django_migrations (app, name, applied) VALUES (?, ?, ?)", ('core', '0001_initial', '2023-01-01 00:00:00'))

# Commit and close
conn.commit()
conn.close()

print("Migration record inserted successfully.")
