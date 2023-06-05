# Excel Data Consolidation and GUI Systems for Fire Suppression Products Company Overview

This project aims to streamline data management and improve task tracking for a Fire Suppression Products company. The company handles multiple customers, with each customer's information stored in a separate Excel file. These files contain crucial dates related to filling and maintenance of fire extinguishers.

The primary objectives of this project are as follows:

1.	Extract the relevant dates from the Excel files and consolidate them into a single data frame.
2.	Develop a Graphical User Interface (GUI) notification program using Python to remind employees of upcoming tasks, such as fire extinguisher filling or maintenance.
3.	Implement GUI systems for adding new customers and deleting existing customers.
4.	Ensure privacy and data confidentiality by not sharing any customer names or specific Excel file details, except for the necessary dates.
    
## Data Consolidation

The company maintains approximately 150-200 Excel files, each representing a different customer. The first step involves extracting the relevant dates from these files and consolidating them into a unified data frame. This consolidation will facilitate efficient monitoring and management of the fire extinguisher maintenance schedule.

## GUI Notification Program

To address the issue of missed filling or maintenance dates, a GUI notification program will be developed. This program will serve as a reminder system for employees, ensuring timely actions and preventing any financial losses for the company. The GUI will display notifications based on predefined time intervals (e.g., one month, one week, or one day) before the scheduled task.
The GUI notification program will seamlessly integrate with the command-line interface (CMD). Whenever employees launch the program, the GUI will automatically open, providing a user-friendly interface for managing and tracking fire extinguisher maintenance tasks.
![image](https://github.com/Romchico/fire-suppression-products-data-management/assets/101732278/451fe239-7078-4482-ae46-ff48756f3326)

## GUI Systems for Adding and Deleting Customers

To enhance customer management capabilities, GUI systems will be implemented for adding new customers and deleting existing customers.

### Adding New Customers

The GUI system provides employees with the ability to add new customers to the company's database. Using an intuitive interface, employees can fill out the necessary fields and enter the relevant information, including customer name and dates for fire extinguisher filling and maintenance. Once the required details are entered, employees can submit the information, which will be securely stored in the company's database.
![image](https://github.com/Romchico/fire-suppression-products-data-management/assets/101732278/39c83199-b9cc-4c0a-a937-da8560c330d8)

### Deleting Customers

The GUI system will also allow employees to remove customers from the company's database. By selecting the customer to be deleted from a list or inputting specific details, employees can initiate the deletion process. This feature ensures an efficient and organized customer management system.
![image](https://github.com/Romchico/fire-suppression-products-data-management/assets/101732278/45f4c9c2-886d-4869-82ef-c4bc96e7b868)

## Privacy and Confidentiality

The company maintains a strict privacy policy to safeguard customer information. As per this policy, the names of customers and specific details from Excel files will not be shared. Only the relevant dates related to fire extinguisher filling and maintenance will be accessed and processed.

## Development Tools

The following tools were utilized in the development of this project:
- Jupyter Notebook: Used for data analysis, processing, and initial code development.
- Visual Studio Code (VSCode): Served as the primary Integrated Development Environment (IDE) for writing and testing code.
- Excel: Utilized for storing customer information in separate Excel files.
- CMD: Integrated with the GUI program to provide command-line interaction and launch the notification system.
- 
## License

This project is licensed under the [MIT License](LICENSE).
