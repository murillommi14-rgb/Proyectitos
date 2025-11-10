import sqlite3
import os

# Ruta a la base de datos
db_path = os.path.join(os.getcwd(), 'db.sqlite3')

# Conéctese a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insertar el registro de migración
cursor.execute("INSERT INTO django_migrations (app, name, applied) VALUES (?, ?, ?)", ('core', '0001_initial', '2023-01-01 00:00:00'))

# Comprométete y cierra
conn.commit()
conn.close()

print("Migration record inserted successfully.")
