# cralendarapp
# Assignment-1
I used Django framework to complete my project for backend <br />
The Total Server Space Used is 61 MB if we include code dependency<br />
Link:-https://avatarapp-hm.herokuapp.com/  <br />
Heroku is Cloud Server which is also used as a web server.<br />
This Prject is hosted on single dynamo. <br />
# Best_Principal_Design:-
admin_root_work is by-default admin I change admin_root_work for security reason <br />
Link:-https://avatarapp-hm.herokuapp.com/admin_root_work/          <br />
Username:-himanshu45                                <br />                                           
password:-himanshu9888698590                                           <br />
After login we can see how many account are there who are sign in with us and also used for other security reason <br />
# inportant_variable_used:-
LOGIN_REDIRECT_URL='home:index'                                
I created this in a way when session browser close then it is going to close with session browser       <br />
Multiple_User:-As mentioned in assignment to do that multiple user can be login at the same time it is done, Try to login from 2-3 browser 
after sign-up it will show on the top which of the user are simultaneously using this.           <br />
Secret key is present in .env file and i include this .env file in .gitignore because i dont want to include .env file.       <br />
# Functionality
When we click to home it forces us to login





