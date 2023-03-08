# Email_Tracker_Python
Simple project as Proof of Concept


## project details:
- I have been asked to create a backend architecture for designing an email tracker.
- On opening an email a Get request will hit which will store the email, the time at which request is done.
- It should also record the number of times the request has been made. 

## pre-requisits for project:
- A database will be needed for this project in order to store the information that will be gathered from email inquiries.
- One server is needed to install the programme and connect to the database.

## Following steps are followed for creating this application:
### step1: Creating Database
- I set up a "email-tracker"-named MySQL database on Amazon.
- When creating a database, a username and password are needed to access the database.

![creating mysql database](https://user-images.githubusercontent.com/114205101/223707628-3042cb89-4975-4595-ab01-b7ff3fd9ab17.PNG)

### step2: creating instance:
- A new t2.micro instance is built from AWS as this project is only being developed for demonstration purposes and larger instances would need to be deployed for actual applications.

![creating instance](https://user-images.githubusercontent.com/114205101/223708337-32b2d416-98bf-4ffc-ad11-b529e4dfc25c.PNG)

### step3: writing code:
- To write code, I used Jupyter Notebook.
- In order to accomplish the project goal, I will use the flask framework.

![creating app in jupyter 1](https://user-images.githubusercontent.com/114205101/223709451-43ac1dcf-8825-4333-a3f7-31d67d00842d.PNG)

- at first we will install mysql connector using command "pip install mysql-connector-python"
- then we will import mysql-connector and Flask
- all the data which is required to connect our database is stored in multiple variables. Ideally it should be stored in another file (config) but as our application is small i have included this in same code.
- one variable is defined named as "conn" which will connect to our database using all the data which we have given in above step.
- The if statement checks if the connection to the MySQL database is successful, and prints a message indicating the same.

![creating app in jupyter 2](https://user-images.githubusercontent.com/114205101/223711547-c274afb6-88c9-44df-9935-76300939ee66.PNG)

- The Flask route that accepts GET requests at the /track endpoint is created
- When request is made to this endpoint it will call the "track_email" function.
- The email_id parameter is extracted from the GET request using request.args.get('email_id').
- A cursor object is created to execute SQL queries on the database.
- The cursor.execute will qury tha database to check wheather the email ID is exist in database or not. if it exist in database it will increae the count by "1, else it will create new row in table and record emailID time and count.
- Finally we will commit it and close the object.
### step4: Running app on server
- At first we will install all the dependancies required for this project on server like python, mysql-connector, flask and gunicorn.
command used are as follw - "sudo apt install python3",
"sudo apt install pip",
"pip install mysql-connector-python",
"pip install Flask",
"sudo apt install gunicorn"
- we will connect to our mysql database using command "mysql <endpoint> -u <username of our database> -P <port no> -p".
- we have create new table within this database which will record all the data.

![database table created](https://user-images.githubusercontent.com/114205101/223716308-1b4a557c-7aea-4ed8-bc52-e6f2a265ce5d.PNG)

- we have already copied our application in this server which can be run using command "python3 <app file name>"

![running app and binding it to ip](https://user-images.githubusercontent.com/114205101/223717079-1dbdc553-c6df-4a55-92bf-15aac2d3d095.PNG)

- we can use gunicorn to bind this application with our server ip and command used is "gunicorn --bind 0.0.0.0:5000 email_tracker:app". this command will run our application on port 5000 which we can access.

![email tracked successfully](https://user-images.githubusercontent.com/114205101/223717264-2834ae1e-5a47-4d0c-8a3c-81f72f29fc42.PNG)

- By again connecting to our mysql database and listing tables we can verify that our data is being stored.

![data is being stored in tables in mysql](https://user-images.githubusercontent.com/114205101/223717482-35e6883a-d8ef-43d4-9cf9-23a1d2b5a011.PNG)

