AutoTrader

AutoTrader is a popular app for buying and selling vehicles, providing a comprehensive solution for car buyers and sellers, with a wide range of features and services.

<a href="https://autotrader.herokuapp.com/" target="_blank">Visit the live project here</a>

![alt text](docs/multi_platform1.png "Responsive Image") 

## Requirements

1. if you want to login as admin please enter the following username and password to login
    * Username: allah
    * Password: allah
2. if you want to login as normal user you can click on register button in login page.

## User Experience & user stories
### Admin
* As an admin I can access admin panel so that I can create, read, update and delete vehicles.
* As an admin I can access admin panel so that I can approve or reject reviews from users.

### LoggedIn User
* As a loggedin user i can add my review for a specific vehicle.
* As a loggedin user i can edit, delete, and read my review in vehicle details page.

### Normal User
* As a normal user i can see the list of vehicles so that i could buy one.
* As a normal user i can access to pagination so that see list of vehicles very fast.
* As a normal user i can see the details of each vehicle so that i could know all details about that.
* As a normal user i can call to the owner of the vehicle so that i could make a deal with him/her.

### Implemented Agile Project in GitHub
![alt text](docs/agile.PNG "User Stories") 

## Features
According to the mentined point at the top the users can use the website with these features:
1. Users can create user account.
2. Users can see the vehicle details and mail for seller.
3. Users can comment and review on vehicles.
4. Admins can approve or reject vehicle to be published.
5. Admins can approve or reject reviews.
6. This a full responsive webapp

## Structure
Simplicity, clarity and ease of navigation between pages were the main aspects for design of this website's structure.

At the top of the page there is a recognisable type of navigation bar with website name on the left side and the navigation links.
### Files & Directories
1. autotrader - project directory.
2. utils.py - Contains all Django helper functions used in views.py.
3. urls.py - This file handles all the URLs of the project.
4. shop - main application directory.
5. static - contains all static content.
6. css - Contains all css files for styling the webpages.
7. js - Contains all javascript files used in the application.
8. img - Contains all image files used in the application.
9. templates Contains all application templates.
10. index.html - Template for showing all vehicles.
11. vehicle_details.html - Template for showing details for each vehicle.
12. login.html - Login user page.
13. register.html - Register user page.
14. admin.py - Contains some models for access to the Django administrator.
15. models.py - All models used in the application are created here.
16. views.py - This file contains all the application views.
17. requirements.txt - This file contains all contains all the python packages that needs to be installed to run this web application.
18. manage.py - This file is used basically as a command-line utility and for deploying, debugging, or running our web application.

### Database
The backend consists of Python built with the Django framework with a database of a ElephantSQL for the deployed version.

The following models were created to represent the database model structure for the website:
1. VehicleModel
2. ReviewModel

### Technologies Used
This website is developed and designed using these stack:
1. HTML
2. CSS
3. Bootstrap
4. Javascript
5. Python
6. Django

### Libraries & Tools
1. Bootstrap
2. Cloudinary
3. Chrome dev tools
4. Git
5. GitHub
6. Heroku Platform
7. Postgres

## Testing
### Testing Strategy
I utilised manual and validator testing strategies for the development of the site. In addition to the functionality testing of the site and the testing of the code, User Story tests were implemented to ensure that the criteria of the user stories listed above were met.

### Validator Testing
The site's HTML, CSS and Python codes are validated by the W3C Markup Validation Service, W3C CSS Validation Service and PEP8 ONLINE service.

* HTML HTML docs were run through the W3C Markup validation and passed the validation.

  * Html error report:
  ![alt text](docs/html.PNG "HTML Error") 

  * Css All CSS files ran through CSS jigsaw validator with some bootstrap errors that can be ignored.
  
### Manual Testing
1. **Site testing:** I manually tested the site's navigation menu links and all buttons accross the site's all pages that all work fine in terms of loading and redirecting URLs to the relavant pages.

2. **Register form testing:** I manually tested the register form's password fields. The password needs to meet certain requirements when user regsiter an account.

3. **User exists:** I manually tested that it's not possible to register an account with the same username or the same email address.

4. **Login form testing:** I manually tested the login form. The username and the password needs to be the same as user specified when registering an account.

5. **New Vehicle form testing:** I manaually tested vehicle form and the vehicle will be inserted when form filled correctly.

6. **Add Review Testing:** I manaually tested adding review form and it works fine after the adding review for specific vehicle.

## Deployment:
This project was deployed to Heroku. "Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps."- Heroku.

I used Code Institute GitPod full template to set up an environment to created the project. Installed Django and required packages / libraries using commands in GitPod terminal.

* pip3 install Django==3.2 gunicorn
* pip3 install dj3-cloudinary-storage
* pip3 freeze --local > requirements.txt

### Deployment of This Project

This site was deployed by completing the following steps:

1. Log in to Heroku or create an account
2. On the main page click the New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
Next select your region
4. Click on the Create App button
5. Click in resources and select Heroku Postgres database
6. Click Reveal Config Vars and add a new record with SECRET_KEY
7. Click Reveal Config Vars and add a new record with the CLOUDINARY_URL
8. Click Reveal Config Vars and add a new record with the DISABLE_COLLECTSTATIC = 1
9. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
10. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

### Final Deployment
1. Create a Procfile web: gunicorn your_project_name.wsgi
2. When development is complete change the debug setting to: DEBUG = False in settings.py
3. In Heroku settings, delete the config vars for DISABLE_COLLECTSTATIC = 1

### Cloning This Project
Clone this project by following the steps:

1. Open GitHub 
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order to - copy the URL
3. Once you click the button the fork will be in your repository
4. Open a new terminal
5. Change the current working directory to the location that you want the cloned directory
6. Type 'git clone' and paste the URL copied in step 3
7. Press 'Enter' and the project is cloned

## Installation
1. Install project dependencies by running py -m pip install -r requirements.txt.
2. Run the commands py manage.py makemigrations and py manage.py migrate in the project directory to make and apply migrations.
3. Create superuser with py manage.py createsuperuser.
4. Run the command py manage.py runserver to run the web server.
5. Open web browser and goto 127.0.0.1:8000 url to start using the web application.

## Credits
During the process of project development, there have been various sources that gave me idea how to do a particular feature or fix a bug. The following are the sources that I got knowledge from:

* Django Allauth
* Code Instiute course materials and Django Blog Walkthrough Project.
* Bootstrap
* The website has been created following YouTube tutorials and stack overflow.
* All images were taken from free websites

---
*Speacial Thanks from Luke Buchanan for helping me on this project!*