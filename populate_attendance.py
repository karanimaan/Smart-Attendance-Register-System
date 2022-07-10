import datetime

# input
import time

import b64

name = "Reza"
portrait_base64 = b64.b64

from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = conn.attendance_register_system

# add record to attendance_table
record = {
    "name": name,
    "image_frame": portrait_base64,
    "time_of_arrival": time.time()
}

# Insert Data
if db.attendance_table.find_one({"name": name}):
    db.attendance_table.delete_many({"name": name})
db.attendance_table.insert_one(record)

# Printing the data inserted
cursor = db.attendance_table.find()
for r in cursor:
    print(r)
