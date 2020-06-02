# Shoe-Shop


# Milestone Project 4
## Description
---
This is my fourth Milestone project of the Full Stack Software Development course from Code Institute.
This project is designed to pull together everything we have learned over the duration of the course. 
The main focus of this project is using python and Django with a SQL database, whilst also harnessing the 
Javascript, HTML and CSS skills we have previously learnt.

## Development
---
One of the huge benefits of 
Django is that it takes care of a lot of things under the hood which lends itself to fast deployment. Another benefit is 
that you create different sections of your site in individual 'apps' with he premise that you can re-use the 
functionality on future sites.

Throughout development I used Git and GitHub for version control. Firstly, I made sure my site was deployed correctly 
based on the master branch in GitHub. Once setup was successful, I started to develop on different branches. 

Gitpod was my choice of IDE this time around. I like its similarities and features as of that and its predecessor Visual Studio Code.
Additionally, I chose to use Postgres as my database as this is more scalable as your app grows.

The app is deployed on Heroku, and all environment variables are stored locally in an env.py file. This was added to 
a .gitignore file so all of the values were kept a secret.

### Note
When testing this project, to make a payment via the store, the below details should be used:
* Card Number: 4242424242424242
* CVC: Any 3 digit number
* Expiry Date: Any future date.

Anything not matching the above will receive an error.

## UX/UI
---
### User Stories
#### Site Users
* I want the ability to browse the website on any device.
* I want to be able to register an account on the website in order to gain further access.
* I want the ability to buy Products. I want to be able to add them to my cart and the view my cart at any stage.
* I want to be able to adjust the quantity of items in my cart or completely remove them.
* I want to be able to logout of my account.
* I want the ability to be able to search for a desired product from the search bar

### Site Owner
* I want the ability to add and remove products to the store from the admin panel.
* I want the ability to add new products to the store and remove also via the admin panel.
* I want all users (regardless of device) to have a positive user experience.
* I want to be able to be contacted by a user should they deem it necessary.

#### Current Features
* Products Page - A page where thats displays the products in a list view.
* Reviews - A section I created so that users can share htere experiences with the site.
* User Accounts - Users are able to register and account on the site and login.

#### Defensive Design
Throughout the build of this site various defensive features were added to protect against malicious activity, and 
also to stop things breaking.

* A `{% csrf_token %}` was added on every form to prevent Cross Site Request Forgeries.

* Included in a lot of the views and a lot of the templates are checks to ensure that te user has been 
authenticated. This helps avoid somebody trying to login who is already logged in etc. But it also helps ensure 
only registered users are accessing certain functions, such as commenting and purchasing.

* Several checks were put in place within the forms and the models to ensure all requests were receiving all 
the expected data. Adding 'required' to certain field helped ensure this was achieved and fields were not left blank.


* 404 and 500 error pages were created so that the user received a custom error rather than receiving the 
django standards.

## Database
I chose to make use of the Postgres DB as i saw that it had huge advantages compared to other databases.

- Postgres needs to be added as an add-on in Heroku.
