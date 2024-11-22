import csv
import tkinter
from tkinter import messagebox

# Define the file path as a global variable
# PLEASE EDIT THIS TO YOUR MACHINE
DATA_FILE_PATH = r"C:\Users\oscar\Documents\Work\CCT211H5_F(coding)\assigment2_part1-3\Data.csv"

# Function to validate date format (dd/mm/yyyy)
def validate_date_format(input):
    if len(input) != 10 or input[2] != '/' or input[5] != '/':
        return False
    day, month, year = input[:2], input[3:5], input[6:]
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    if int(day) < 1 or int(day) > 31 or int(month) < 1 or int(month) > 12 or len(year) != 4:
        return False
    return True

# Function to check if the student number is unique
def is_student_number_unique(student_number):
    try:
        with open(DATA_FILE_PATH, mode='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if len(line) >= 4:  # Ensure there are enough columns
                     if line[3] == student_number:  # Check if the student number exists
                         return False
    except FileNotFoundError:
        return True  # If file is not found, assume the student number is unique
    return True

# Function to validate the entire form
def validate_form():
    if not first_name_value.get():
        messagebox.showwarning("Input Error", "First name is required.")
        return False
    if not last_name_value.get():
        messagebox.showwarning("Input Error", "Last name is required.")
        return False
    if not date_of_birth_value.get() or not validate_date_format(date_of_birth_value.get()):
        messagebox.showwarning("Input Error", "Please enter a valid date of birth (dd/mm/yyyy).")
        return False
    if not student_number_value.get():
        messagebox.showwarning("Input Error", "Student number is required.")
        return False
    if not is_student_number_unique(student_number_value.get()):
        messagebox.showwarning("Input Error", "This student number already exists.")
        return False
    if not passwords.get():
        messagebox.showwarning("Input Error", "Password is required.")
        return False
    if checkboxA.get() == 0:
        messagebox.showwarning("Confirmation Error", "Please confirm the action before proceeding.")
        return False
    return True

# Function to read and display data from CSV
def read_data():
    table = []
    try:
        with open(DATA_FILE_PATH, mode='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                table.append(line)
    except FileNotFoundError:
        messagebox.showwarning("File Error", "File not found.")
        return
    # Initialize the data frame
    for widget in data_frame.winfo_children():
        widget.destroy()
    # Populate the data frame
    for row_num, row in enumerate(table):
        for column_num, cell_value in enumerate(row):
            cell_label = tkinter.Label(data_frame, text=cell_value)
            cell_label.grid(row=row_num, column=column_num)

# Function to write (create or update) data into CSV
def write_data():
    if not validate_form():
        return
    if not messagebox.askyesno("Confirm Submission", "Are you sure you want to submit the data?"):
        return
    
    try:
        table = []
        # Read the file into a list
        with open(DATA_FILE_PATH, mode='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                table.append(line)
        # Update the table and write back in the correct order
        table.append([date_of_birth_value.get(), first_name_value.get(), last_name_value.get(), student_number_value.get(), passwords.get()])
        
        # Write the updated table back to the CSV file
        with open(DATA_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(table)
        
        messagebox.showinfo("Success", "Data submitted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to delete a record by student number
def delete_data():
    student_number = student_number_value.get()
    if not student_number:
        messagebox.showwarning("Input Error", "Student number is required to delete a record.")
        return
    if not messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the record?"):
        return
    
    try:
        table = []
        record_found = False
        with open(DATA_FILE_PATH, mode='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if len(line) >= 4:  # Ensure there are enough columns
                    if line[3] == student_number:  # Check if the student number matches
                        record_found = True  # Found the record to delete
                    else:
                        table.append(line)  # Keep the rows that don't match the student number
        if record_found:
            with open(DATA_FILE_PATH, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(table)  # Write the updated table back to the file
            messagebox.showinfo("Success", "Record deleted successfully.")
        else:
            messagebox.showwarning("Not Found", "Student record not found.")
    except FileNotFoundError:
        messagebox.showerror("File Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the main window
window = tkinter.Tk() 
window.title("User Data Centre") 
window.geometry('700x500') 

# Connected variables for form inputs
first_name_value = tkinter.StringVar(window)
last_name_value = tkinter.StringVar(window)
student_number_value = tkinter.StringVar(window)
date_of_birth_value = tkinter.StringVar(window)
passwords = tkinter.StringVar(window)

# Data display frame
data_frame = tkinter.LabelFrame(window, text="Student Info")
data_frame.grid(row=0, column=0)

# Input frame
input_frame = tkinter.LabelFrame(window, text="Inputs")
input_frame.grid(row=0, column=1)

# First name
first_name_label = tkinter.Label(input_frame, text="First Name ")
first_name_label.grid(row=0, column=0)
first_name_entry = tkinter.Entry(input_frame, textvariable=first_name_value) 
first_name_entry.grid(row=0, column=1)

# Last name
last_name_label = tkinter.Label(input_frame, text="Last Name ")
last_name_label.grid(row=1, column=0)
last_name_entry = tkinter.Entry(input_frame, textvariable=last_name_value) 
last_name_entry.grid(row=1, column=1)

# Date of birth
date_of_birth_label = tkinter.Label(input_frame, text="Date of Birth (dd/mm/yyyy)")
date_of_birth_label.grid(row=0, column=2)
date_of_birth_entry = tkinter.Entry(input_frame, textvariable=date_of_birth_value)
date_of_birth_entry.grid(row=0, column=3)

# Student number
student_number_label = tkinter.Label(input_frame, text="Student Number ")
student_number_label.grid(row=1, column=2)
student_number_entry = tkinter.Entry(input_frame, textvariable=student_number_value) 
student_number_entry.grid(row=1, column=3)

# Password
passwords_label = tkinter.Label(input_frame, text="New password ")
passwords_label.grid(row=2, column=0)
passwords_entry = tkinter.Entry(input_frame, textvariable=passwords)  # Corrected here
passwords_entry.grid(row=2, column=1)

# Checkbox for confirmation
checkboxA = tkinter.IntVar()
checkbox_A_check_button = tkinter.Checkbutton(input_frame, 
    text="Confirm?",
    variable=checkboxA,
    onvalue = 1, offvalue = 0)
checkbox_A_check_button.grid(row=2, column=2)

# Buttons for various actions
submit_button = tkinter.Button(input_frame, text='Submit', command=write_data)
submit_button.grid(row=3, column=0)

show_button = tkinter.Button(input_frame, text='Show Data', command=read_data)
show_button.grid(row=3, column=1)

delete_button = tkinter.Button(input_frame, text='Delete Record', command=delete_data)
delete_button.grid(row=3, column=2)


tkinter.mainloop()
