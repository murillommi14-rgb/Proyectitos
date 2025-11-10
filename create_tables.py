import sqlite3
import os

# Path to the database
db_path = os.path.join(os.getcwd(), 'db.sqlite3')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# SQL statements from sqlmigrate
sql_statements = """
CREATE TABLE "core_role" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL UNIQUE);
CREATE TABLE "core_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL);
CREATE TABLE "core_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "core_user_roles" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED, "role_id" bigint NOT NULL REFERENCES "core_role" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "core_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "core_user_groups_user_id_group_id_c82fcad1_uniq" ON "core_user_groups" ("user_id", "group_id");
CREATE INDEX "core_user_groups_user_id_70b4d9b8" ON "core_user_groups" ("user_id");
CREATE INDEX "core_user_groups_group_id_fe8c697f" ON "core_user_groups" ("group_id");
CREATE UNIQUE INDEX "core_user_roles_user_id_role_id_6a202c76_uniq" ON "core_user_roles" ("user_id", "role_id");
CREATE INDEX "core_user_roles_user_id_754bb369" ON "core_user_roles" ("user_id");
CREATE INDEX "core_user_roles_role_id_85eb2a9f" ON "core_user_roles" ("role_id");
CREATE UNIQUE INDEX "core_user_user_permissions_user_id_permission_id_73ea0daa_uniq" ON "core_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "core_user_user_permissions_user_id_085123d3" ON "core_user_user_permissions" ("user_id");
CREATE INDEX "core_user_user_permissions_permission_id_35ccf601" ON "core_user_user_permissions" ("permission_id");
"""

# Execute each statement
for statement in sql_statements.strip().split(';'):
    if statement.strip():
        cursor.execute(statement)

# Commit and close
conn.commit()
conn.close()

print("Core tables created successfully.")
