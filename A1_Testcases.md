#### Test Case R2.0.1: If the user has logged in, redirect back to the user profile page /
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

#### Test Case R2.1.1: If user has not logged in, show the user registration page
Actions:
 - open /logout
 - open /register
 - validate that current page contains `#password2`

#### Test Case R2.2.1: The registration page shows a registration form requesting: email, user name, password, password2
Actions:
 - open /logout
 - open /register
 - validate that current page contains `input[#email]`
 - validate that current page contains `input[#name]`
 - validate that current page contains `input[#password]`
 - validate that current page contains `input[#password2]`

#### Test Case R2.3.1: The registration form can be submitted as a POST request to the current URL (/register)
Actions:
 - open /logout
 - open /register
 - validate that current page contains `form[method='post'] input[#btn-submit]`

#### Test Case R2.4.1: Email cannot be empty
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

#### Test Case R2.4.2: Password cannot be empty
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
 
#### Test Case R2.4.3: Email must not fail to conform to RFC 5322
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
#### Test Case R2.4.4: Email must conform to RFC 5322
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
#### Test Case R2.4.5: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character - negative
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
#### Test Case R2.4.6: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
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

#### Test Case R2.5.1: Password and password2 cannot be different

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

#### Test Case R2.6.1: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character - negative
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

#### Test Case R2.7.1: User name has to be longer than 2 characters and less than 20 characters - negative
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

#### Test Case 2.8.1: For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)
This case is covered by the conjunction of R2.4.1, R2.4.2, R2.4.3, R2.4.5, R2.5.1, R2.6.1, R2.7.1. A pass on all of these cases is a pass for R2.8.1.
#### Test Case 2.9.1: If the email already exists, show message 'this email has been ALREADY used'
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
#### Test Case 2.10.1: If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
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

#### Test Case 2.10.1: If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page - negative
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

