## Test Case Set 2: Get /register
### R2.0: If the user has logged in, redirect back to the user profile page /
#### Test Case R2.0.1: Check that re-registration is bypassed for a user that is already logged in
Test Data:
```
test_user = User(
	email='test_frontend@test.com',
	name='test frontend',
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /register
 - validate that current page contains `#welcome-header` element

### R2.1: otherwise, show the user registration page
#### Test Case R2.1.1: Check that user registration page is served to a user that is not logged in
Actions:
 - open /logout
 - open /register
 - validate that current page contains `#password2`

### R2.2: The registration page shows a registration form requesting: email, user name, password, password2
#### Test Case R2.2.1: Check that "email", "user name", "password", and "password2" elements are present in login page and that they are all form text inputs
Actions:
 - open /logout
 - open /register
 - validate that current page contains `input[#email]`
 - validate that current page contains `input[#name]`
 - validate that current page contains `input[#password]`
 - validate that current page contains `input[#password2]`

### R2.3: The registration form can be submitted as a POST request to the current URL (/register) 
#### Test Case R2.3.1: Check that there is a submit button for registration
Actions:
 - open /logout
 - open /register
 - validate that current page contains `form[method='post'] input[#btn-submit]`

### R2.4: Email, password, password2 all have to satisfy the same required as defined in R1
#### Test Case R2.4.1: Check that registration fails if email is empty 
Test Data:
```
test_user = User(
	email='',
	name='test frontend',
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#message` element shows `email format is incorrect`

#### Test Case R2.4.2: Check that registration fails if password is empty
Test Data:
```
test_user = User(
	email='test_frontend@test.com',
	name='test frontend',
	password=''
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#message` element shows `password format is incorrect`
 
#### Test Case R2.4.3: Check that registration fails if email does not conform to RFC 5322
Test Data:
```
test_user = User(
	email='<each invalid example from https://en.wikipedia.org/wiki/Email_address#Examples',
	name='test frontend',
	password=generate_password_hash('test_frontend')
)
```
Mocking:
 - Mock backend.get_user to return a test_user instance 

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#message` element shows `email format is incorrect`

(Note: this test shall be run for each of the emails referenced in test_user.email)
#### Test Case R2.4.4: Check that registration succeeds while email conforms to RFC 5322
Test Data:
```
test_user = User(
	email='<each valid example from https://en.wikipedia.org/wiki/Email_address#Examples',
	name='test frontend',
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#welcome-header` element is present
 
 (Note: this test shall be run for each of the emails referenced in test_user.email)
#### Test Case R2.4.5: Check that registration fails when password is shorter than 6 chars or has no upper case char or has no lower case char or has no special character 
Test Data:
```
test_user = User(
	email='test_frontend@test.com',
	name='test frontend',
	password=<each of ['1Aa!5', '1aa!56', '1AA!56', '1Aa456']>
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#message` element is present and reads `password format is incorrect`
 
 (Note: this test shall be run for each of the passwords listed in test_user.password)
#### Test Case R2.4.6: Check that registration succeeds while password is at least 6 chars and has an upper case, lower case, and special character
Test Data:
```
test_user = User(
	email='test_frontend@test.com',
	name='test frontend',
	password='1Aa!56'
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#welcome-header` element is present 

### R2.5: Password and password2 have to be exactly the same
#### Test Case R2.5.1: Check that registration fails when password and password2 are different

Test Data:
```
test_user = User(
	email='test_frontend2@test.com',
	name='test frontend',
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter `'1Aa!57'` into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#message` element is present and reads `password2 format is incorrect`

(Note: Positive case was covered by R2.4.6)

### R2.6: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. 
#### Test Case R2.6.1: Check that registration fails if name is empty or name contains non-alphanumeric chars or has a space as first or last char
Test Data:
```
test_user = User(
	email='test_frontend2@test.com',
	name=<each of ['', 'aa!', ' aa', 'aa ']>
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#message` element is present and reads `name format is incorrect`

(Note: this test case shall be run for each of the names listed in test_user.name)
(Note: positive case was covered by R2.4.6)

### R2.7: User name has to be longer than 2 characters and less than 20 characters
#### Test Case R2.7.1: Check that registration fails if username is too short or too long
Test Data:
```
test_user = User(
	email='test_frontend2@test.com',
	name=<each of ['12', '12345678901234567890']>
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#message` element is present and reads `name format is incorrect`

(Note: this test case shall be run for each of the names listed in test_user.name)
(Note: positive case was covered by R2.4.6)

### R2.8: For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
#### Test Case 2.8.1: Check redirects and error messages
This case is covered by the conjunction of R2.4.1, R2.4.2, R2.4.3, R2.4.5, R2.5.1, R2.6.1, R2.7.1. A pass on all of these cases is a pass for R2.8.1.
### R2.9: If the email already exists, show message 'this email has been ALREADY used' 
#### Test Case 2.9.1: Check registration fails for email already in use with special error message
Test Data:
```
test_user = User(
	email='test_frontend@test.com',
	name='test frontend'
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - open /logout (to invalidate current session)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the `#message` element is present and reads `this email has been ALREADY used`
### R2.10: If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
#### Test Case 2.10.1: Check that proper registration creates user and proceeds to /login
Test Data:
```
test_user = User(
	email='test_frontend2@test.com',
	name='test frontend'
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the current page contains `h1` with value `Log In`

#### Test Case 2.10.2: Check user not created on improper form, stays on /register
Test Data:
```
test_user = User(
	email='test_frontend3@test.com',
	name='test frontend '
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /register
 - enter test_user's email into element `#email`
 - enter test_user's name into element `#name`
 - enter test_user's password into element `#password`
 - enter test_user's password into element `#password2`
 - click element `input[type="submit"]`
 - validate that the current page contains `h1` with value `Register`

## Test Case Set 3: Get /
### R3.0: If the user is not logged in, redirect to login page
#### Test Case 3.0.1: Check user not logged in gets redirect to /login
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /
 - validate that current page contains `h1` element with value `Log In`
#### Test Case 3.0.2: Check user logged in does not redirect to /login
Test Data:
```
test_user = User(
	email='test_frontend@test.com',
	name='test frontend',
	password=generate_password_hash('test_frontend')
)
```

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - validate that current page contains `#welcome-header` element

### R3.1: This page shows a header `'Hi {}'.format(user.name)`
#### Test Case 3.1.1: Check element present containing welcome message `Hi <user.name>`
Test Data: As in R3.0.2

Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - validate that current page contains `h2` element with value `Hi test frontend!`

### R3.2: This page shows user balance.
#### Test Case 3.2.1: Check element present containing user balance
Test Data: As in R3.0.2

Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - validate that current page contains `#balance` element

### R3.3: This page shows a logout link, pointing to /logout 
#### Test Case 3.3.1:  Check element present containing link to /logout
Test Data: As in R3.0.2

Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - validate that current page contains `a[href='/logout']` element

### R3.4: User profile page lists all available tickets, with information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired
#### Test Case 3.4.1: Check table row present matching a non expired ticket in the database 
Test Data: As in 3.0.2; additionally:
```
test_ticket = Ticket(
    owner='test_frontend@test.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    date='20200901'
)
```
Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_ticket to return a test_ticket instance

Actions:
 -  open /logout (to invalidate any logged-in sessions that may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /
 - enter test_ticket's name into element `form[#sell_form] input[#sell_name]`
 - enter test_ticket's quantity into element `form[#sell_form] input[#sell_quantity]`
 - enter test_ticket's price into element `form[#sell_form] input[#sell_price]`
 - enter test_ticket's date into element `form[#sell_form] input[#sell_date]`
 - click element `form[#sell_form] input[#sell_submit]`
 - open /
 - validate that there exists a `#ticket-table tr#<x>`such that 
	 - `#x td.ticket-name` equals test_ticket.name, and
	 - `#x td.ticket-quantity` equals test_ticket quantity, and
	 - `#x td.ticket-price` equals test_ticket price, and
	 - `#x td.ticket-date` equals test_ticket date