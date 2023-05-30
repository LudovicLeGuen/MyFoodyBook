# My-foody-book - Testing 

[Main README.md file](/README.md)

[View live project](https://the-wheel-of-fortune.herokuapp.com/)

***
## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual Testing](#Manual-Testing)
3. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
4. [User Testing](#User-Testing)


***

## Testing User Stories
#### Frequent User Goals:
* As a frequent user want to see the recipes they have created and collected
     * The foody book page allows users to see their own published, secret and collected recipes
     * the user can see all tehir published recipes in the All recipe page

* As a frequent user want to log in with their usual credentials
     * The credentials are stored if necessary.
     * The the credentials are always the same to log in
     
* As a frequent user want to see other users recipes
     * All recipes are visible in the All Recipe page. 
     * The user can also watch other users foodybook to see their published recvipes and collection

* As a frequent users want to manage their FoodyBook
     * All recipes can be updated, deleted or created everywhere on the site
     * Any recipe can be managed according to the users status (author or reader)

#### New User Goals:
* As a New Users want to be able to see some of the content before registering
     * A message explain sthe purpose of the site
     * The foody bookers page is visible

* As a New users want to understand what the site is about within seconds
     * A clear message explains the purpose of the site. 

* As a new users want to understand the functionalities quickly..
     * The functions are pretty clear and pretty simple. 
     * Only very pages and very vew functionalities help keep things simple
     * the buttons on the recipes are also clear to understand

[Back to top ⇧](#My-foody-book---Testing)
## Manual Testing
### Login, Logout, Register
* LogIn

     ![Inserting Names](assets/testing-files/user-name.png) 

* Logout

     ![Inserting Names](assets/testing-files/round-input.png)

* Register

     ![Rules](assets/testing-files/rules-negative.png)
     ![Rules](assets/testing-files/rules.png)

### Create, Delete, Update, See a recipe
* Creating recipe

     ![Mystery Sentence](assets/testing-files/mystery-sentence.png)

* Turning the wheel

     ![Turnning the wheel](assets/testing-files/wheel.png)

* Cash value

     ![Cash Value](assets/testing-files/value.png)

* Pass your turn

     ![Cash Value](assets/testing-files/pass.png)

* Bankrupt

     ![Bankrupt](assets/testing-files/bankrupt.png) 

* Inserting a consonant

     ![Consonant](assets/testing-files/consonant-test.png) 

### Update Profile

* Verify the consonant

     ![Consonant](assets/testing-files/verification.png) 

### Update FoodyBook

* Consonant already guessed

     ![Consonant](assets/testing-files/guessed.png) 

* No more consonant to chose

     ![No more consonant](assets/testing-files/no-consonant.png)

* Print consonant

### Update FoodyBook

* Consonant already guessed

     ![Consonant](assets/testing-files/guessed.png) 

* No more consonant to chose

     ![No more consonant](assets/testing-files/no-consonant.png)


[Back to top ⇧](#My-foody-book---Testing)

## Automated Testing
### Code Validation
* PEP8 CI Python Linter 

| Page              |  Result                                                                    | Comment|
| :---              |      :---:                                                                 | :---:  |
| publish app url   | ![publish app url](assets/readme-files/images/tests/publish_urls.PNG)      | pass   |
| publish app admin | ![publish app admin](assets/readme-files/images/tests/publish_admin.PNG)   | pass   |
| publish app forms | ![publish app forms](assets/readme-files/images/tests/publish_forms.PNG)   | pass   |
| publish app views | ![publish app views](assets/readme-files/images/tests/publish_vews.PNG)    | pass   |
| user app url      | ![user app url](assets/readme-files/images/tests/users_urls.PNG)           | pass   |
| user app signals  | ![user app signals](assets/readme-files/images/tests/users_signals.PNG)    | pass   |
| user app models   | ![user app models](assets/readme-files/images/tests/users_model.PNG)       | pass   |
| user app views    | ![user app views](assets/readme-files/images/tests/users_view.PNG)         | pass   |

* CSS validator
![CSS validation](assets/readme-files/images/tests/css_validator.PNG)

* Javascript
My javascript is a few lines long.
I tested it on [esprima](https://esprima.org/image.png)

![CSS validation](assets/readme-files/images/tests/javascript.png)

* HTML

| Page                |  Result                                                                    | Comment|
| :---                |      :---:                                                                 | :---:  |
| Profile.html        | ![publish app url](assets/readme-files/images/tests/publish_urls.PNG)      | pass   |
| register.html       | ![publish app admin](assets/readme-files/images/tests/publish_admin.PNG)   | pass   |
| user_profile.html   | ![publish app forms](assets/readme-files/images/tests/publish_forms.PNG)   | pass   |
| userlist.html       | ![publish app views](assets/readme-files/images/tests/publish_vews.PNG)    | pass   |
| 404.html            | ![user app url](assets/readme-files/images/tests/users_urls.PNG)           | pass   |
| base.html           | ![user app signals](assets/readme-files/images/tests/users_signals.PNG)    | pass   |
| delete_recipe.html  | ![user app models](assets/readme-files/images/tests/users_model.PNG)       | pass   |
| index.html          | ![user app views](assets/readme-files/images/tests/users_view.PNG)         | pass   |
| my_foodyBook.html   | ![user app views](assets/readme-files/images/tests/users_view.PNG)         | pass   |
| publish_recipe.html | ![user app views](assets/readme-files/images/tests/users_view.PNG)         | pass   |
| recipe_details.html | ![user app views](assets/readme-files/images/tests/users_view.PNG)         | pass   |
| update_recipe.html  | ![user app views](assets/readme-files/images/tests/users_view.PNG)         | pass   |


* Lighthouse


* Javascript


[Back to top ⇧](#My-foody-book---Testing)

## User testing 
Special thanks to the following who tested and gave me their feedback and ideas to improve the game:
* My wife Domnika 
* Ed bradley, as usual
* My Mentor Koko The champion of the wheel of fortune. Really lads she is unbeatable.....

***