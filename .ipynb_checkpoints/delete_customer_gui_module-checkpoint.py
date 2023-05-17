def delete_customer():
    import pandas as pd
    import re
    from time import sleep
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    from tkinter import Tk, Button, Label, Entry, messagebox
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv("final_table.csv", index_col="file_name")
    df["Upcoming Date"] = pd.to_datetime(df["Upcoming Date"], dayfirst=True)
      
    def button_clicked():
        label_output.grid(column=1, row=2)
        customer = input_customer_name.get() + ".xlsx"
        
        if input_customer_name.get() == "":
            # Check if customer name is provided
            label_output.config(text="Please type the customer name!")
            input_customer_name.delete(0, 'end')
            return
        if customer not in df.index:
            # Check if customer exists in the DataFrame
            label_output.config(text="The name you provided is not in the dataframe!")
            input_customer_name.delete(0, 'end')
        else:
            # Ask for confirmation before deleting the customer
            confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {customer}?")
            if confirmation:
                # Delete the customer from the DataFrame
                df.drop(customer, axis=0 ,inplace=True)
                df.to_csv("final_table.csv", index=True)
                label_output.config(text=f"{customer} is deleted from the dataframe!")
            else:
                # Deletion cancelled by the user
                label_output.config(text="Deletion cancelled.")
            
            input_customer_name.delete(0, 'end')
            
    # Create the tkinter window
    window = Tk()
    window.title("Deleting Customer Program")
    window.minsize(600, 500)
    window.config(padx=15, pady=15)
    window.grid()
    font = ("Arial", 15, "bold", "italic")
    
    # Create customer name input field
    input_customer_name = Entry()
    input_customer_name.grid(column=1, row=0)
    
    # Create button two for deleting customer
    button = Button(text="Delete the Customer", command=button_clicked)
    button.grid(column=1, row=1)
    
    # Create label for displaying output
    label_output = Label(text="", font=font)
    
    # Start the tkinter event loop
    window.mainloop()