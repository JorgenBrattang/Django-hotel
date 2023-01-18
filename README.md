# Django Hotel
Small Hotel with a booking system that is easy to use.

<!-- ![stretch-page](assets/images/amIresponsive.png) -->

Live app: https://django-hotel.herokuapp.com/

# Table of content
- [User Experience](#user-experience)
    - [User stories](#user-stories)
    - [User feedback](#user-feedback)
- [Design](#design)
    - [Login](#login)
    - [Menu](#menu)
    - [Difficulty](#difficulty)
- [Development](#development)
- [Strategy](#strategy)
- [Feature and Testing](#feature-and-testing)
- [Unsolved bugs](#unsolved-bugs)
- [Technologies used](#technologies-used)
    - [Language](#language)
- [Frameworks libraries and programs used](#frameworks-libraries-and-programs-used)
- [Credit](#credit)
    - [Deployment description](#deployment-description)
    - [Credited Code](#credited-code)
- [Deployment](#deployment)
    - [Create Repository](#create-repository)
    - [Github Pages](#github-pages)
    - [Forking](#forking)
    - [Clone](#clone)
    - [Setting up heroku](#setting-up-heroku)
- [Developers part](#Developers-part)
- [What I learned](#what-i-learned)
- [Continued development](#continued-development)
- [Acknowledgements](#acknowledgements)


# User experience
## User stories


[Back to top](#table-of-content)

## User feedback


[Back to top](#table-of-content)

# Development


[Back to top](#table-of-content)

# Strategy

[Back to top](#table-of-content)

## Feature and Testing


[Back to top](#table-of-content)

## Unsolved bugs

[Back to top](#table-of-content)

# Technologies used
## Language
- Python
- Django

[Back to top](#table-of-content)

## Frameworks libraries and programs used

- <a href="https://git-scm.com/" title="Link to git" rel="nofollow">Git</a>
    - For version control
- <a href="https://gitpod.io/" title="Link to gitpod" rel="nofollow">GitPod</a>
    - GitPod was used for writing code, committing, and then pushing to GitHub.
- <a href="https://github.com/" title="Link to github" rel="nofollow">Github</a>
    - GitHub was used to store the project after pushing
- <a href="https://dashboard.heroku.com/" title="Link to Heroku" rel="nofollow">Heroku</a>
    - To deploy project.
- <a href="https://lucid.app/" title="Link to lucid" rel="nofollow">Lucid</a> 
    - To make flowcharts for the project
- <a href="https://docs.python.org/3/library/os.html" title="Link to python os" rel="nofollow">Os libary</a> 
    - To clear the screen
- <a href="https://ui.dev/amiresponsive" title="Link to am i responsive" rel="nofollow">am i responsive</a> 
    - Show the website on different screens

[Back to top](#table-of-content)

# Credit

## Deployment description
Huge thank you to <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> with the excellent description on how the deployment went. 

[Back to top](#table-of-content)

# Credited Code

[Back to top](#table-of-content)

# Deployment
To make this project I used the Code Institute's mock terminal for Heroku.

## Create Repository
For this I used Github.
1. Go to your profile, and press on "Repositories".
2. Press "New" (Big green button).
3. There I chose to use a template from Code Institute to have everything I needed for this project.
4. Named my project "django-hotel".
5. Then clicked on "Create repository".
6. Onces created, I opened the repository and clicked on "Gitpod" to create a new workplace.

[Back to top](#table-of-content)

## Github Pages
1. Went to my repository "django-hotel".
2. Settings tab.
3. Pages.
4. Chose my branch to be main.
5. Hit save and a couple of minutes later it was deployed.

[Back to top](#table-of-content)

## Forking
1. Login to Github and go to my <a href="https://github.com/JorgenBrattang/daily-math">repository</a>
2. Find the Fork button o the top right corner.
3. Press it.
4. The fork is now in your own repository.

[Back to top](#table-of-content)

## Clone
- Credit to <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> for the description!

1. Login to Github and go to my <a href="https://github.com/JorgenBrattang/daily-math">repository</a>
2. Above the list of files click the green ‘code’ button.
3. This will bring up a few options as to how you would like to clone. You can 4. select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
4. Open git bash
5. Type ‘git clone’ and then paste the URL you copied. Press Enter.

[Back to top](#table-of-content)

## Setting up heroku
- Credit to <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> for the description!

To set up heroku you must;

1. If your requirements.txt file has not changed you can skip this step. Otherwise, in your terminal type 'pip3 freeze > requirements.txt' then save and push the changes.
2. Go to Heroku.com and sign in or create a free account.
3. From the heroku dashboard click the 'Create new app' button.
4. Name the app something unique and choose what region you are in then click 'Create app'.
5. Go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.
6. If your project does not use a creds.json file then skip this step. Otherwise, in the field for KEY enter the value CREDS in all capitals. In the field for VALUE copy and paste the entire contents of your creds.json file from your project. Then click 'Add'.
7. In the field for KEY enter PORT in all capitals, then in the field for VALUE enter 8000. Then click 'Add'.
8. Scroll down to the Buildpacks section and click 'Add buildpack'.
9. Click Python then save changes.
10. Add another buildpack by clicking 'Add buildpack' and this time click Nodejs then save changes.
11. Make sure that Python appears above Nodejs in the buildpack section. If it does not you can click and drag them to change the order.
12. Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.
13. From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.
14. Enter the repository name as it is in GitHub and click 'search'.
15. Click the 'connect' button next to the repository to link it to heroku.
16. To deploy, scroll down and click the 'Deploy Branch' button.
17. Heroku will notify you that the app was successfully deployed with a button to view the app.
18. If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.

[Back to top](#table-of-content)

# Developers part

## What I learned

[Back to top](#table-of-content)

## Continued development

[Back to top](#table-of-content)

## Acknowledgements
I would like to acknowledge my mentor <a href="https://github.com/seunkoko" title="Link to GitHub profile" rel="nofollow">Oluwaseun Owonikoko</a> which guided me to make the app more interesting and threw me idea's that I did not think about.

 My family for helping me progress and support me, and not to forget the tutors and community of slack that helped me alot to understand the concepts of programming and hardship of debugging.

 And can't thank <a href="https://github.com/Delboy/Fruit-Hunter">Delboy</a> enough for the time saver with the informative description for deployment, saved me hours of writing and I'm so thankfull!

 [Back to top](#table-of-content)