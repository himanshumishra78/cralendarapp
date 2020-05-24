# cralendarapp
# Assignment-1
I used Django framework to complete my project for backend
The Total Server Space Used is 61 MB if we include code dependency
Link:-https://avatarapp-hm.herokuapp.com/
Heroku is Cloud Server which is also used as a web server.
This Prject is hosted on single dynamo.
# Best_Principal_Design:-
admin_root_work is by-default admin I change admin_root_work for security reason 
Link:-https://avatarapp-hm.herokuapp.com/admin_root_work/
Username:-himanshu45
password:-himanshu9888698590
After login we can see how many account are there who are sign in with us and also used for other security reason
# inportant_variable_used:-
LOGIN_REDIRECT_URL='home:index'
I created this in a way when session browser close then it is going to close with session browser
Multiple_User:-As mentioned in assignment to do that multiple user can be login at the same time it is done, Try to login from 2-3 browser 
after sign-up it will show on the top which of the user are simultaneously using this.
Secret key is present in .env file and i include this .env file in .gitignore because i dont want to include .env file.
# Functionality
When we click to home it forces us to login





