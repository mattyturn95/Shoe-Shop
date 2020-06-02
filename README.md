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
