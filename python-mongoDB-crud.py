import tkinter as tk
from pymongo import MongoClient

# # Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['ADS_Assignment_9']
collection = db['CRUD _Application']


# cloud_connection_string = "mongodb+srv://hakkevaibhavi:r4rFzk1sWjgaAdZT@adsassignment9.zaumkik.mongodb.net/?retryWrites=true&w=majority&appName=adsassignment9"

# # Initialize MongoDB client
# client = MongoClient(cloud_connection_string)
# db = client['ADS_Assignment_9']
# collection = db['CRUD _Application']

# Define functions for CRUD operations
def create_record(name, age, email, phone):
    data = {
        "name": name,
        "age": age,
        "email": email,
        "phone": phone
    }
    collection.insert_one(data)

def read_records():
    records = collection.find()
    return list(records)

def update_record(record_id, name, age, email, phone):
    collection.update_one({"_id": record_id}, {"$set": {"name": name, "age": age, "email": email, "phone": phone}})

def delete_record(record_id):
    collection.delete_one({"_id": record_id})

# GUI
class CRUDApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("CRUD Application")
        self.master.configure(bg='#f0f0f0')  # Set background color

        # Labels and Entries
        self.name_label = tk.Label(master, text="Name:", bg='#f0f0f0')
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.age_label = tk.Label(master, text="Age:", bg='#f0f0f0')
        self.age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.age_entry = tk.Entry(master, width=30)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(master, text="Email:", bg='#f0f0f0')
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(master, text="Phone:", bg='#f0f0f0')
        self.phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.create_button = tk.Button(master, text="Create", command=self.create, bg='#4CAF50', fg='white')  # Green color
        self.create_button.grid(row=4, column=0, padx=10, pady=5, sticky="we")

        self.read_button = tk.Button(master, text="Read", command=self.read, bg='#008CBA', fg='white')  # Blue color
        self.read_button.grid(row=4, column=1, padx=10, pady=5, sticky="we")

        self.update_button = tk.Button(master, text="Update", command=self.update, bg='#f44336', fg='white')  # Red color
        self.update_button.grid(row=5, column=0, padx=10, pady=5, sticky="we")

        self.delete_button = tk.Button(master, text="Delete", command=self.delete, bg='#FFC107', fg='black')  # Yellow color
        self.delete_button.grid(row=5, column=1, padx=10, pady=5, sticky="we")

        # Output Text
        self.output_text = tk.Text(master, height=10, width=40)
        self.output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        self.output_text.configure(bg='#ffffff')  

    def create(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        create_record(name, age, email, phone)
        self.output_text.insert(tk.END, "Record created successfully.\n")

    def read(self):
        records = read_records()
        self.output_text.delete(1.0, tk.END)
        for record in records:
            self.output_text.insert(tk.END, f"Name: {record['name']}, Age: {record['age']}, Email: {record['email']}, Phone: {record['phone']}\n")

    def update(self):
        records = read_records()
        if records:
            record_id = records[0]['_id']
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            email = self.email_entry.get()
            phone = self.phone_entry.get()
            update_record(record_id, name, age, email, phone)
            self.output_text.insert(tk.END, "Record updated successfully.\n")
        else:
            self.output_text.insert(tk.END, "No records found to update.\n")

    def delete(self):
        records = read_records()
        if records:
            record_id = records[0]['_id']
            delete_record(record_id)
            self.output_text.insert(tk.END, "Record deleted successfully.\n")
        else:
            self.output_text.insert(tk.END, "No records found to delete.\n")

# Initialize Tkinter
root = tk.Tk()
app = CRUDApplication(root)
root.mainloop()
