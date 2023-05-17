def notification():
    # Import necessary libraries
    import pandas as pd
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    from tkinter import Tk, Button, Label

    # Read the CSV file into a DataFrame
    df = pd.read_csv("final_table.csv", index_col="file_name")
    df["Upcoming Date"] = pd.to_datetime(df["Upcoming Date"], dayfirst=True)
    # The dates in "Upcaoming Date" column are in European format so we can ignore the warning.

    '''First, we will update the years in the dataframe for any dates that are not current.'''
    
    # Read the CSV file into a DataFrame
    today = datetime.today()
    today = pd.to_datetime(today, dayfirst=True)

    not_current = df[df["Upcoming Date"] <= today].index

    for file in not_current:
        df.loc[file, "Upcoming Date"]+=relativedelta(years=1)
        
    df.to_csv("final_table.csv", index=True)
    
    # Determine the files scheduled for the upcoming month, week, and day
    a_month = today + relativedelta(months=1)
    files_month = list(df[df["Upcoming Date"].between(today, a_month, inclusive="both")].index)
    files_str_month = ", ".join(files_month)

    a_week = today + relativedelta(days=7)
    files_week = list(df[df["Upcoming Date"].between(today, a_week, inclusive="both")].index)
    files_str_week = ", ".join(files_week)

    a_day = today + relativedelta(days=1)
    files_day = list(df[df["Upcoming Date"].between(today, a_day, inclusive="both")].index)
    files_str_day = ", ".join(files_day)
    
    # Define button click event handlers
    def button_clicked_one():
        if files_month == []:
            label_report.config(text="There don't appear to be \nany tasks scheduled for the upcoming MONTH!")
        else:
            output = f"There's \"ONE\" month remaining for maintanence or for filling. \nCheck the file/s of {files_str_month} \nfor more information please."
            label_report.config(text=output)

    def button_clicked_two():
        if files_week == []:
            label_report.config(text="There don't appear to be \nany tasks scheduled for the upcoming WEEK!")
        else:
            output = f"There's \"ONE\" week remaining for maintanence or for filling. \nCheck the file/s of {files_str_week} \nfor more information."
            label_report.config(text=output)

    def button_clicked_three():
        if files_day == []:
            label_report.config(text="There don't appear to be \nany tasks scheduled for TOMORROW!")
        else:
            output = f"Maintenance or refilling of fire extinguishers scheduled for TOMORROW! Check the file/s of {files_str_day} for more information."
            label_report.config(text=output)

    # Create the tkinter window
    window = Tk()
    window.title("Due Date Reminder Program")
    window.minsize(800, 500)
    window.config(padx=15, pady=15)
    window.grid()
    font = ("Arial", 15, "bold", "italic")
    
    # Create a label for spacing
    label_space = Label(text=" "*20, font=font)
    label_space.grid(column=1, row=0)
    
    # Create the first button for upcoming tasks with one month or less remaining
    button_one = Button(text="Upcoming Tasks with \nOne Month or Less Remaining", command=button_clicked_one)
    button_one.grid(column=2, row=0)
    
    # Create a label for spacing
    label_space = Label(text=" "*20, font=font)
    label_space.grid(column=3, row=0)
    
    # Create the second button for upcoming tasks with one week remaining
    button_two = Button(text="Upcoming Tasks with\nOne Week Remaining", command=button_clicked_two)
    button_two.grid(column=4, row=0)

    label_space = Label(text=" "*20, font=font)
    label_space.grid(column=5, row=0)
    
    # Create the third button for tasks scheduled for tomorrow
    button_three = Button(text="Tasks Scheduled \nfor Tomorrow", command=button_clicked_three)
    button_three.grid(column=6, row=0)

    label_space = Label(text=" "*20, font=font)
    label_space.grid(column=1, row=1)

    label_space = Label(text=" "*20, font=font)
    label_space.grid(column=1, row=2)
    
    # Create label for displaying output
    label_report = Label(text="", font=font)
    label_report.grid(columnspan=7, rowspan=3)

    # Start the tkinter event loop
    window.mainloop()