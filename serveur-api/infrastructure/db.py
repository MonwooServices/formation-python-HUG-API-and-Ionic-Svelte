# Copyright Monwoo pour Elvexdomotique

# https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial
import sqlite3

con = sqlite3.connect("buddy-api.db.sqlite")

cur = con.cursor()

# MODE SQL
cur.execute("CREATE TABLE message(date, haveBeenSaid, msg)")

# MODE NO SQL
# cur.execute("CREATE TABLE message(id, jsonData, indexDeRechercheCalcule)")

# TODO : Trouver un ORM type Doctrine Symfony pour Python (Ex : GraphQl Python)
