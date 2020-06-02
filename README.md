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

## Technologies Used
---
Below is a list of technologies I used to build my site.
* HTML - HTML5 provided the structure of my website. I tried to use semantic elements where possible to ensure the best structure.
* CSS - Used to style my page.
* [Bootstrap](https://getbootstrap.com/) - Used primarily for the grid system. I find this a really good way to position my elements where I want them.
* [GitHub](https://github.com/) - This is where my repository is held externally. I will also use GitHub pages to deploy my website.
* [Google Fonts](https://fonts.google.com/) - Used to import specific fonts I wanted to use on my website.
* [Python](https://www.python.org/) - Python was the language used to build the backend of the website.
* [Django](https://www.djangoproject.com/) - Python framework used in order to build out the routes/views of my website.
* [Heroku](https://id.heroku.com/login) - I used Heroku to deploy my website.
* [Postgres](https://www.postgresql.org/) - I used Postgres as my database for development and production.
* [Stripe](https://stripe.com/gb) - I used Stripe to process payments on the site.
* [WhiteNoise](http://whitenoise.evans.io/en/stable/django.html) - I used WhiteNoise to serve my static files.
* [GoogleFonts](https://fonts.google.com/) - I used Google Fonts to help choose the type of font family i was to be using for my site.

## Testing
---
Most of my testing was done manualy for this project, I did however make use of pep8 and w3 validator to help make sure that my code was semantic and viable.

My choice of browser for this project was Google Chrome. This is my go to browser due to the really good dev tools.
The dev tools play a huge part in how I developed my website. When working on bug fixes or new styles I always use the dev tools 
first to see what they look like or if I can find whats causing the bug before implementing into my own code. The dev tools 
also play a major part in me using the mobile-first approach to designing and developing my website.

I made use of Dev Tools to ensure that all devices were able to render my site within different devices.

I also sent out a link to family and friends to have a look at the site on there own devices to help me spot any areas that needed improvement. This was the final stage of testing.

## Deployment
---
My Website was created using Gitpod, and then linked up to an external github repository. I chose to use a text editor other than c9 so that i was able to gain valuable experiemce from working with other editors rather than just one alone.
Gitpod has an internal cli buit in which makes it easy to link up projects with external sources.

* I created a new project in Gitpod.
* I then created a local git repo.
* I then linked my local git repository to a GitHub repository.
* I then followed the below steps to deploy the site to Heroku.

To deploy the website to Heroku, I followed the below steps:
* Created a new project.
* From the deployment method section of the Deploy tab, I selected GitHub, and then entered my github repo link in the 
field provided.
* Every time I push to GitHub master branch it will automatically send the updates across to Heroku.
* I then also had to create some Config Vars in the settings tab, to reflect the environment variables created 
in the env.py file. This file was added to a .gitignore file to ensure the security of sensitive information.
* [Website Link](https://final-ms-project-shoeshop.herokuapp.com/)

### To run this project locally

* Follow this link to the [GitHub Repository](https://github.com/mattyturn95/Shoe-Shop)
* Click on the 'Clone or Download' button.
* Copy the URL provided.
* Open a bash terminal, move to your desired directory.
* Type 'git clone' and paste in the URL.
* Create an env.py file and store three environment variables. The environment variables required are (SECRET_KEY, DATABASE_URL, 
STRIPE_PUBLISHABLE, STRIPE_SECRET).

## Credits
---
* 
* The Slack community.
* [HTML Color Code](https://htmlcolorcodes.com/) .
* [W3C Validator](https://validator.w3.org/#validate_by_input) * 
* [PEP8](http://pep8online.com/) - Python validator to ensure my code adhered to PEP8 standards.



