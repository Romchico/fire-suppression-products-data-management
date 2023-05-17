def add_new_customer():
    
    import pandas as pd
    import re
    from time import sleep
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    from tkinter import Tk, Button, Label, Entry

    # Create a global variable for customer date input field
    global input_customer_date

    # Define a regular expression pattern for validating date format
    pattern = re.compile(r"\d{1,2}/\d{1,2}/\d{4}")

    # Get the current date
    today = datetime.today()
    today = pd.to_datetime(today, dayfirst=True)

    # Read the CSV file into a DataFrame
    df = pd.read_csv("final_table.csv", index_col="file_name")
    df["Upcoming Date"] = pd.to_datetime(df["Upcoming Date"], dayfirst=True)

    # Define the function for button one click event
    def button_one_clicked():
        global cust_name
        label_output.grid(column=1, row=2)

        # Get the customer name from the input field
        cust_name = input_customer_name.get()

        if cust_name == "":
            label_output.config(text="Please type the customer name!")
            input_customer_name.delete(0, 'end')
            return
        if cust_name + ".xlsx" in df.index:
            label_output.config(text=f"{cust_name} is already exist!, Try Again")
            input_customer_name.delete(0, 'end')
        else:
            file_name = cust_name + ".xlsx"
            label_output.config(text=f"{cust_name} is successfully added! \nNow add a date on the left!")
            input_customer_name.delete(0, 'end')

    # Define the function for button two click event
    def button_two_clicked():
        new_date = input_customer_date.get()
        check_date = re.findall(pattern, new_date)
        label_output.grid(column=3, row=2)

        if check_date == []:
            label_output.config(text="Unvalid Date, Try Again!")
            input_customer_date.delete(0, 'end')
            return

        try:
            new_date_mod = pd.to_datetime(new_date, dayfirst=True)
        except:
            label_output.config(text="Unvalid Date, Try Again!")
            input_customer_date.delete(0, 'end')
            return

        if today >= new_date_mod:
            label_output.config(text="Please Write the Current Date!")
            input_customer_date.delete(0, 'end')
            return

        elif "cust_name" in globals():
            cust_name_modified = cust_name + ".xlsx"
            df.loc[cust_name_modified] = new_date_mod
            df.to_csv("final_table.csv", index=True)
            label_output.config(text=f"{new_date} is successfully added!\nAll the information has been added to the database")
            input_customer_date.delete(0, 'end')

        elif "cust_name" not in globals():
            text="Customer name should have been first!\nPlease, firstly add the customer name.\nThen add the date again."
            label_output.config(text=text)

    # Create the tkinter window
    window = Tk()
    window.title("Adding New Customer Program")
    window.minsize(600, 500)
    window.config(padx=15, pady=15)
    window.grid()
    font = ("Arial", 15, "bold", "italic")

    # Create customer name input field
    input_customer_name = Entry()
    input_customer_name.grid(column=1, row=0)

    # Create button one for adding customer name
    button_one = Button(text="Add a new customer\n(First fill here!)", 
                        command=button_one_clicked)
    button_one.grid(column=1,row=1)
    
    # Create label for displaying output
    label_output = Label(text="", font=font)

    # Create spacing label
    label_space = Label(text=" "*20, font=font)
    label_space.grid(column=2, row=0)

    # Create customer date input field
    input_customer_date = Entry()
    input_customer_date.grid(column=3, row=0)

    # Create button two for adding customer date
    button_two = Button(text="Add a date in the format of dd/mm/yyyy", command=button_two_clicked)
    button_two.grid(column=3, row=1)

    # Start the tkinter event loop
    window.mainloop()