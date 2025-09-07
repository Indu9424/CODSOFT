import tkinter as tk
from tkinter import messagebox
import json

contacts = []
current_index = None  
FILE_NAME = "contacts.json"

# ---------------- Data Persistence ----------------
def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f)

def load_contacts():
    global contacts
    try:
        with open(FILE_NAME, "r") as f:
            contacts[:] = json.load(f)   # load into list
    except FileNotFoundError:
        contacts = []   # if file doesn't exist, start empty

# ---------------- Core Functions ----------------
def add_contact():
    global current_index
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name and phone:
        # Duplicate check (only when adding new)
        if current_index is None and any(c["phone"] == phone for c in contacts):
            messagebox.showwarning("Duplicate", "This phone number already exists!")
            return

        if current_index is None:  # Add new
            contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
        else:  # Update existing
            contacts[current_index] = {"name": name, "phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", f"Contact {name} updated successfully!")
            current_index = None
            add_btn.config(text="Add Contact")

        clear_entries()
        show_all_contacts()
        save_contacts()  # Save every time
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

def toggle_contacts():
    if contact_frame.winfo_viewable():
        contact_frame.grid_remove()
        view_btn.config(text="View Contacts")
    else:
        show_all_contacts()
        contact_frame.grid(row=12, column=0, columnspan=2, padx=5, pady=10)
        view_btn.config(text="Hide Contacts")

def show_all_contacts():
    contact_list.delete(0, tk.END)
    for c in contacts:
        contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")

def search_contact():
    query = search_entry.get().strip().lower()
    if not query:
        messagebox.showwarning("Input Error", "Enter name or phone to search.")
        return

    if not contact_frame.winfo_viewable():
        contact_frame.grid(row=12, column=0, columnspan=2, padx=5, pady=10)
        view_btn.config(text="Hide Contacts")

    contact_list.delete(0, tk.END)
    found = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]

    if found:
        for c in found:
            contact_list.insert(tk.END, f"{c['name']} - {c['phone']}")
    else:
        messagebox.showinfo("Search Result", "No contacts found.")

def reset_search():
    search_entry.delete(0, tk.END)
    show_all_contacts()

def delete_by_name():
    query = delete_entry.get().strip().lower()
    if not query:
        messagebox.showwarning("Input Error", "Enter a name or phone to delete.")
        return

    deleted = False
    for c in contacts[:]:  # safe copy
        if query == c["name"].lower() or query == c["phone"]:
            contacts.remove(c)
            deleted = True
            messagebox.showinfo("Deleted", f"Contact {c['name']} deleted.")
            break

    if not deleted:
        messagebox.showwarning("Not Found", "No contact matched your input.")

    delete_entry.delete(0, tk.END)
    show_all_contacts()
    save_contacts()

def edit_contact():
    global current_index
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact["address"])

        current_index = index
        add_btn.config(text="Save Update")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to edit.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def show_details(event):
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        c = contacts[index]
        messagebox.showinfo("Contact Details", f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Contact Management System")
root.geometry("470x700")

# Entry Fields
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
name_entry = tk.Entry(root, width=35)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
phone_entry = tk.Entry(root, width=35)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
email_entry = tk.Entry(root, width=35)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
address_entry = tk.Entry(root, width=35)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
add_btn = tk.Button(root, text="Add Contact", width=20, command=add_contact)
add_btn.grid(row=4, column=0, columnspan=2, pady=10)

view_btn = tk.Button(root, text="View Contacts", width=20, command=toggle_contacts)
view_btn.grid(row=5, column=0, columnspan=2, pady=5)

# Search
tk.Label(root, text="Search (Name/Phone):").grid(row=6, column=0, sticky="w", padx=5, pady=5)
search_entry = tk.Entry(root, width=25)
search_entry.grid(row=6, column=1, padx=5, pady=5)

search_btn = tk.Button(root, text="Search", width=20, command=search_contact)
search_btn.grid(row=7, column=0, columnspan=2, pady=5)

reset_btn = tk.Button(root, text="Reset Search", width=20, command=reset_search)
reset_btn.grid(row=8, column=0, columnspan=2, pady=5)

# Delete by Name/Phone
tk.Label(root, text="Delete (Name/Phone):").grid(row=9, column=0, sticky="w", padx=5, pady=5)
delete_entry = tk.Entry(root, width=25)
delete_entry.grid(row=9, column=1, padx=5, pady=5)

delete_btn = tk.Button(root, text="Delete Contact", width=20, command=delete_by_name)
delete_btn.grid(row=10, column=0, columnspan=2, pady=5)

# Contacts Frame
contact_frame = tk.Frame(root)

tk.Label(contact_frame, text="Contacts:").pack(anchor="w")
contact_list = tk.Listbox(contact_frame, width=50, height=12)
contact_list.pack(pady=5)

edit_btn = tk.Button(contact_frame, text="Edit Selected Contact", width=25, command=edit_contact)
edit_btn.pack(pady=5)

# Double-click to see full details
contact_list.bind("<Double-1>", show_details)

# Hide initially
contact_frame.grid(row=12, column=0, columnspan=2, padx=5, pady=10)
contact_frame.grid_remove()

# Load saved contacts at startup
load_contacts()

# Save contacts on close
root.protocol("WM_DELETE_WINDOW", lambda: (save_contacts(), root.destroy()))

root.mainloop()
