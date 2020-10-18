| Specification | Test case ID | Purpose |
|:-:|-|:-:|
| If the user has logged in, redirect back to the user profile page / | R2.0.1 | Check that re-registration is bypassed for a user that is already logged in |
| otherwise, show the user registration page | R2.1.1 | Check that user registration page is served to a user that is not logged in |
| the registration page shows a registration form requesting: email, user name, password, password2 | R2.2.1 | Check that "email", "user name", "password", and "password2" elements are present in login page and that they are all form text inputs |
| The registration form can be submitted as a POST request to the current URL (/register) | R2.3.1 | Check that there is a submit button for registration |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.4.1 | Email cannot be empty |
| | R2.4.2 | Password cannot be empty |
| | R2.4.3 | Email must not fail to conform to RFC 5322 |
| | R2.4.4 | Email must conform to RFC 5322 |
| | R2.4.5 | Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character - negative |
| | R2.4.6 | Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character |
| Password and password2 have to be exactly the same | R2.5.1 | Check if password and password2 different fails to register |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. | R2.6.1 | Check that registration fails if name is empty or name contains non-alphanumeric chars or has a space as first or last char |
| User name has to be longer than 2 characters and less than 20 characters | R2.7.1 | Check registration fails if username is too short or too long |
| For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute) | R2.8.1 | Check redirect and error message |
| If the email already exists, show message 'this email has been ALREADY used' | R2.9.1 | Check email not already in use |
| If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page | R2.10.1 | Check user created properly |
| | R2.10.2 | Check user not created on improper form |
| If the user is not logged in, redirect to login page | R3.0.1 | Check user not logged in redirect to /login |
| | R3.0.2 | Check user logged in does not redirect |
| This page shows a header `'Hi {}'.format(user.name)` | R3.1.1 | Check element present containing welcome message `Hi <user.name>` |
| This page shows user balance. | R3.2.1 | Check element present containing user balance |
| This page shows a logout link, pointing to /logout | 3.3.1 | Check element present containing link to /logout |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired | R3.4.1 | Check table row present matching a non expired ticket in the database |