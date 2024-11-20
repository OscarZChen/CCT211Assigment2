import csv
import tkinter

# Define the file path as a global variable
# PLEASE EDIT THIS TO YOUR MACHINE
DATA_FILE_PATH = r"C:\Users\oscar\Documents\Work\CCT211H5_F(coding)\assigment2_part1-3\Data.csv"

def read_data():
    table = []
    # Open the file using the global path variable
    with open(DATA_FILE_PATH, mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            table.append(line)
    # Initialize the data frame
    for widget in data_frame.winfo_children():
        widget.destroy()
    # Populate the data frame
    for row_num, row in enumerate(table):
        for column_num, cell_value in enumerate(row):
            cell_label = tkinter.Label(data_frame, text=cell_value)
            cell_label.grid(row=row_num, column=column_num)

def write_data():
    table = []
    # Read the file into a list
    with open(DATA_FILE_PATH, mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            table.append(line)
    # Update the table and write back
    table.append([first_name_value.get(), last_name_value.get(), student_number_value.get()])
    with open(DATA_FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)


window = tkinter.Tk() 
window.title("Entry Validation with Dialog") 
window.geometry('700x500') 

#everything below in this block is connected variable
first_name_value = tkinter.StringVar(window)
last_name_value = tkinter.StringVar(window)
student_number_value = tkinter.StringVar(window)

#data_frame is connected variable
data_frame = tkinter.LabelFrame(window, text="Student Info")
data_frame.grid(row=0, column=0)
input_frame = tkinter.LabelFrame(window, text="Inputs")
input_frame.grid(row=0, column=1)

first_name_label = tkinter.Label(input_frame, text="First Name ")
first_name_label.grid(row=0, column=0)
first_name_entry = tkinter.Entry(input_frame, textvariable=first_name_value) 
first_name_entry.grid(row=0, column=1)

last_name_label = tkinter.Label(input_frame, text="Last Name ")
last_name_label.grid(row=1, column=0)
last_name_entry = tkinter.Entry(input_frame, textvariable=last_name_value) 
last_name_entry.grid(row=1, column=1)

student_number_label = tkinter.Label(input_frame, text="Student Number ")
student_number_label.grid(row=2, column=0)
student_number_entry = tkinter.Entry(input_frame, textvariable=student_number_value) 
student_number_entry.grid(row=2, column=1)

submit_button = tkinter.Button(input_frame, text='Submit', command=write_data)
submit_button.grid(row=3, column=1)

show_button = tkinter.Button(input_frame, text='Show Data', command=read_data)
show_button.grid(row=3, column=0)
tkinter.mainloop()
