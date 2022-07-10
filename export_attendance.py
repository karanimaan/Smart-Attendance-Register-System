import csv

from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = conn.attendance_register_system

attendees = list(db.attendance_table.find())

with open('attendance.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(attendees[0].keys())
    for attendee in attendees:
        employee = db.employees_table.find({'name': attendee['name']})
        csv_writer.writerow(attendee.values()[:-1] + employee.values())
