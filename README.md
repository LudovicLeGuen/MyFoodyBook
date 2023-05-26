# My-foody-book

My Foody Book is a full stack web application where users can create and store their recipes and also collect other users one. 

The purpose of the site is to offer a convenient platform to store recipes and also be inspired by others. 

The audience is simple: Food lovers of all ages who love sharing and showing what they can do in a kitchen. 

The Website is based on CRUD fucntionnality and allow users to create, read, update and delete their own recipes (except for admins). User can also collect and discard others users recipes. Finally, users can create and update their profiles.

My Foody Book also provides an administration exclusively accessible by admins that can manage comments and moderate the platform.

![Abyss diving club on devices](assets/readme-files/wheel-of-fortune.PNG)

[Click here to access live project](https://the-wheel-of-fortune.herokuapp.com/)
## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
    4. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
     1. [Deploying on GitHub Pages](#Deploying-on-GitHub-Pages)
8. [Credits](#Credits)
     1. [Media](#Media)
     2. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***

## Introduction
My Foody Book is the 4th project for Code Institute's full stack development degree.
The minimum requirements of this project are:
* Use an Agile methodology to plan and design a Full-Stack Web application using an MVC framework and related contemporary technologies.
* Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
* Identify and apply authorisation, authentication and permission features in a Full-Stack web application solution.
* Create manual and/or automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies
* Use a distributed version control system and a repository hosting service to document, develop and maintain a Full-Stack Web application using an MVC framework and related contemporary technologies.
* Deploy a Full-Stack Web application using an MVC framework and related contemporary technologies to a cloud-based platform
* Understand and use object-based software concepts


[Back to top ⇧](#My-foody-book)

## UX
### Ideal User Demographic

### User-Stories
#### Frequent User Goals
* Frequent users want to see the recipes they have created and collected
* Frequent users want to log in with their usual credentials
* Frequent users want to wee ne recipes

#### New User Goals
* New Users want to be able to see some of the content before registering
* New users want to understand what the site is about with seconds
* New users want to understand the funxtionalities quickly.

#### Site Administrators
* The admnistrators needs to control all aspects of the site
* The admins can remove users
* The admins need to moderate comments

#### Development Methodology
* The development followed an Agile methodology on the [Foody Book github Project](https://github.com/users/LudovicLeGuen/projects/4 "Link to the Foody Book github Project")
![Github project](assets/readme-files/project.png)
* All project database was base on the following Database Shema.
![Github project](assets/readme-files/database.png)

[Back to top ⇧](#My-foody-book)

### Dvelopment-Planes


#### Strategy

    
#### Scope

#### Scope

<details>
<summary>Pre game flowchart</summary>
    
![Pre Game](assets/readme-files/pre-game.png)

</details> 


[Back to top ⇧](#My-foody-book)

### Design

[Back to top ⇧](#My-foody-book)

### Skeleton

<details>
<summary>Home Page</summary>
    
![Homepage](assets/readme-files/home-my-foody-book.png)

</details> 

<details>
<summary>All recipe page</summary>
    
![Homepage](assets/readme-files/all-recipe.png)

</details> 

<details>
<summary>Landing page</summary>
    
![Landing-Page](assets/readme-files/landing-page.png)

</details> 

<details>
<summary>Profile page</summary>
    
![Profile](assets/readme-files/profile-page.png)

</details> 

<details>
<summary>Login</summary>
    
![Login](assets/readme-files/login.png)

</details> 
<details>
<summary>Register page</summary>
    
![Register](assets/readme-files/register-page.png)

</details> 

<details>
<summary>My Foody Book page</summary>
    
![Foody-book](assets/readme-files/my-foody-book-page.png)

</details> 

<details>
<summary>My Foody Book page no recipe</summary>
    
![Foody-book](assets/readme-files/Home-My-Foody-book-no-recipe.png)

</details> 

[Back to top ⇧](#My-foody-book)

## Features
### Existing Features


[Back to top ⇧](#My-foody-book)

### Features to Implement in the future

[Back to top ⇧](#My-foody-book)

## Issues and Bugs 
Several issues were encountered during developpement but the most troublesome are listed below.

**Bankrupt would reset the player overall gains instead of the player round earnings** 

### Unfixed Bugs 

[Back to top ⇧](#My-foody-book)

## Technologies Used
### Main Languages Used
* Python3
### Frameworks, Libraries & Programs Used
- [Heroku](https://heroku.com/ "Link to Heroku") was used to deploy the game.
- [GitPod](https://gitpod.io/ "Link to GitPod homepage") was used for writing, commiting, and pushing code.
- [GitHub](https://github.com/ "Link to GitHub")
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage") was used to verify responsiveness and to create the top picture of this README.md

[Back to top ⇧](#My-foody-book)

## Testing
Refer to this [page](TESTING.md) please

## Deployment
The site was developped on Gitpod and Codeanywhere, commiting and pushing to github.

### Deploying on Heroku
Deploying on Heroky required the following:

* Type "pip freeze > requirements.txt" in your Github terminal to update the requirements.txt file with the list of dependencies used in the project . Save, commit and push.

* Create an Heroku account, select Python as the 'Primary development language'.

* Open the email sent to your address and click the link to verify your email address. Follow the instructions to create a password and log in.

* Click the 'create new app' button on the dashboard. Name your app, select your region and click 'Create App'

* In the "Settings" tab, add both the python and node.js build packs.

* Create a "Config VAR" named 'CREDS' KEY and copy/paste the creds.json file in it.

* Create another "Config VAR" called PORT as the KEY with 8000 as VALUE.

* In the "Deploy" tab, choose GitHub as a deployment method.

* Search for the wanted repository.

* Click on "enable automatic deploys" and then deploy branch.

* once the app built (a minute or two needed)click "View" to access the site.
   
[Back to top ⇧](#My-foody-book)

## Credits 
### Code 
The developer has consulted countless times Stack Overflow and W3Schools in ordeer to build the game.
The code inspired by other developpers is commented directly in the code.

[Back to top ⇧](#My-foody-book)

## Acknowledgements
I would like to thank:
* My wife  for her patience and her kind words when I was in doubt.
* my mentor, Seun, for her counseling and her contagious enthusiasm and love for coding.
* my fellow coding students of Code institue who have been invaluable on Slack.

[Back to top ⇧](#My-foody-book)

***