# Schedule Viewer

## System Requirements
> Python 3 </br>
> Pip, which is included by default in Python 3.4 and later </br>
> Visual Studio Code with the Live Server extension or similar server setup </br>

## Installation
The following instructions are created for Windows devices. Follow the same steps with the respective MacOS commands.
1. Clone or download the code found within the GitHub repository </br>
2. Using the command prompt, change directories to .//Schedule_Viewer-main/REST_API
3. Once here, use `python -m venv environment` to create an environment
4. Next, `cd environment/Scripts` and activate by running `activate.bat`
5. Change directories back to REST_API (`cd ../..`), and `pip install -r requirements.txt` to install dependencies 
6. Change to the REST directory via `cd REST`, then `pip install windows-curses` and `python manage.py migrate`
7. Finally, run the server with `python manage.py runserver` (Port should automatically be 8000 if not it should be changed to port 8000)
8. Use the Live Server extension within VS Code, or similar software, to 'Go Live'
9. It is now possible to use the application on localhost (127.0.0.1), using index.html

## Usage
The following steps can be used to experience the full functionality of the application. </br>
These can also be found within the final report (with accompanying pictures). </br>

\[All\] </br>
1.  Logging In: enter the credentials to a valid account stored within the database </br>
1b. If an account does not exist, press the “Create Account” button and enter the information required


\[Employee\] </br>
1. View Schedule: Once logged in as an employee, the “Schedule View” page will greet the worker. This page displays all of the hours of this employee for the week. Their estimated earnings are also displayed.
2. Making a Request: By selecting the chat bubble icon in the bottom-right corner, an employee is able to make a request. Use the “Submit” button to finalise this request. “Close” will minimise the popup without sending a request.
3. Updating Personal Information: In order to update personal information, the employee must enter their username and password. This page is accessed by selecting the “Update Info” section of the header. Once the employee has validated their identity, it is possible to change all information (barring user ID and username, as these are unique and essential to the system).
4. Time Log: A key part of the system, any employee is able to use this functionality to track the hours that they have worked. A project must be selected, followed by the start and end time of the employee’s work day. 

\[Manager\] </br>
1. Building a Schedule: Once logged into a manager account, the user is welcomed by the “Builder” page. Here, a manager is able to select an employee, select a day, and choose the employee’s hours for that day. 
2. Managing Requests: Requests can be viewed by managers on the “Requests” page. Requests can be denied with the “Request Denied” button, or accepted with the “Schedule Changed” button.
3. Adding Departments: It is possible to create new departments by selecting the “Add New Department” button. It is possible to choose a name and select a manager for the newly created department.
4. Editing and Deleting Departments: Editing a department will allow a manager to add employees. To do this, simply select employees from the dropdown.
Deleting a department is as simple as selecting the “Delete” button displayed next to any department. All users within that department will have it removed from their profile.


## Version History
*v1.0* <br/>
A basic website with minimal functionality. Front-end setup. No API implementation at this point, purely a visual representation.</br>
</br>
*v1.1* </br>
Improved CSS styling and polishing of the front-end. Initial setup of the API, but no integration yet.</br>
</br>
*v2.0* </br>
Full integration of the API and database.</br>
</br>


## Contributors and Credit
Richard Gingrich </br>
Ty Irving </br>
Roberto Zaghini </br>
