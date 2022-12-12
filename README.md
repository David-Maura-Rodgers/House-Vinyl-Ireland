# HOUSE VINYL IRELAND - README
 
## PURPOSE OF THIS SITE:
House Vinyl Ireland is an online e-commerce Record store. The site specifically sells Vinyl Records in the House music Genre, released through various different labels.
 
The live site can viewed here - https://house-vinyl-ireland.herokuapp.com/
 
## IMPORTANT INSTRUCTIONS:
When handling payments, this site makes use of the [Stripe](https://stripe.com/gb) payment system. When you are testing the payment function of this site; the payment section will ask you to enter card details: Please only enter 4242 until you reach the end. This is the card number that will be recognised by Stripe when a user just wants to test the payment functionality.
 
If you wish to register or receive a confirmation email, you need to enter a real email address or generate a test email through an email generator site when registering or purchasing items.
 
<br>
 
## SUPERUSER SITE ADMIN FUNCTION:
This site uses Django's Admin functionality for content moderation control. The site has a Superuser with their own login credentials.
 
The Admin panel can be accessed simply from the home page. You can navigate to it by clicking in the URL bar, hit / (forward slash) on keyboard and type admin. Like so: **/admin** and hit **enter**
 
**NOTE:**
- During the development of this project, I posted several test review posts and added Test Records. This was done to test the functionality of the **Create Review**, **Edit Review** and **Delete Review** functions. And to test that Records were successfully added, edited and deleted.
- You will also find some comments visible in the review detail, this was also done to test comment functionality.
- **(All of the review content is simply just placeholder text used to test the functionality of content display for site)**
- Site Admin can do all of the above from the admin panel.
 
<br>
 
# User Experience UX
## User Stories
 
### Navigation:
* Use the main nav bar to move to each section of the site, where login allows
* See all records available when going to ALL VINYL nav link
* See record from a particular label by using the BROWSE LABEL dropdown nav link
* Perform Search using search bar in main nav - user can search by record title or record artist as placeholder text indicates
* When viewing list of available records, basic information about title, artist and price is shown 
* When clicking on any record, they will be able to see a tracklist and description of the record
* Can register/login to the site from any page.

### Purchasing:
* Add desired record to shopping basket from product/record details page
* Be able to select quantity of record needed
* See confirmation that prodcuts have been added to shopping basket
* Be taken to a secure checkout page
* Use basket icon on main nav bar to access my shopping basket from anywhere on the site
* Be able to review purchases from secure checkout page and be given an appropriate breakdown
* Be able to remove or amend quantity on secure checkout page 
* Confident that the site is using a reputable financial services compnay to process payments
* Be able to checkout of the site and pay for selected records
* Be shown an order summary straight after succesful payment has been taken
* On submitting my order, I would like to receive a confirmation email with my order details and a unique order number

### Profile & Contact: 
* Be able to enter my personal information in a secure environment.
* Have the option to register with the site to save my personal information so this is carried over for future purchases
* Be able to contact the site owner by means of a contact form.
* Be able to subscribe to a newsletter
* Be able to view my personal information
* Be able to update my personal information
* Be able to delete my personal information
* View all previous purchases made from My Profile page

### Record Reviews: 
* Be able to select a record I have previously bought and leave a review
* Be able to view any review posted by other users
* Have the option to edit or delete reviews I have posted

<br>

## Site Owner Goals

### Site Admin Function
* Add records to the store via the STORE MANAGEMENT link on main nav when logged in
* Also be able add records from Site Admin page
* Add nay new Labels so that new records can be assigned to them, if the label did not exist previously.
* Edit or Delete records from STORE MANAGEMENT link or site admin on back end
* Show any deals that are being offered on the site's scrolling banner
* View all submitted record reviews so they can be approved for publishing to the site if appropriate
* View all contacts made via the CONTACT US link from site users and respond accordingly

<br>

## Agile Planning
<hr>
This project was developed using agile methodologies by delivering apps and features within different epics and sprints, focusing on the most important 'must have' features and some 'could have' or 'should have' features. This approach ensured that all core requirements were completed first to give the project its intended functionlaty with some features that can be added in the future.

The Kanban board was created using github projects and can be located [here](https://github.com/users/David-Maura-Rodgers/projects/2) and can be viewed to see more information on the project cards.

![Kanban image](docs/readme/kanban.png)

## Epics

The project had **10** main Epics (milestones):
<br>

**EPIC 1 - Getting Set Up**
 
The getting set up epic is for carrying out all tasks needed to the app off the ground. This included some of the following steps:

- Install as follows: pip3 install Django==3.2 django-allauth==0.41.0 Pillow black django-crispy-forms stripe
- Set Up All Auth Templates
- Get Settings.py ready for intended sites functions: context processors and authentication back ends
- Create Main Nav and Social Media links
- Create Base and Home html pages

**EPIC 2 - View Records on Site**

This Epic was concerned with rendering all records on the site to the user and how the user interacted with these products. This included the below tasks and stories:

- User must be able to navigate to the products page (All Vinyl) and see a list of records for sales
- User can use the Browse Label link in the Main Nav to choose the Label they are interested in the most
- Create Admin on back handle so I can have control over the products details
- From the product details page, user should be able to click on the record they want, see more details about that record and be able to add this to their shopping bag using quantity input buttons


**EPIC 3 - Shopping Basket**

The Shopping Basket epic is for all stories related to the user's ability to add records to the shopping basket, in addition to veiwing these and amending them. This included the following:

- User should be able to select the quantity of each record they want using the plus and minus buttons provided on the products details page:
- User should be able to see the value of selected products in shopping basket icon in Main Nav and page
- User should be able to remove items and adjust quantities in their basket, the basket should respond accordingly

**EPIC 4 - Toasts and Messages**

This Epic was concerned with providing messages back to the site user according the their inputs and interactions. This didn't a lot of time to complete. However, it is still an important fearture for the site to have. This included:

- Create Toast Success, Alert, Warning and Info templates
- These messages are rendered for the site user to see

**EPIC 5 - The Checkout App**

This Epic involed the creation of the Checkout App and its initial functionality. This is a key part of the project and involved the below:

- Create Order and Item Checkout models
- Create functions within these models to generate order number and calculate the total of basket items
- Create Admin on backend so I can view details of orders made on site
- Create Signals and Order Form python files
- Checkout Page will provide a summary of records to be purchased

**EPIC 6 - Stripe Setup and Order Summary**

This epic involved a lot of work and several files needed to be created. This was to ensure that the user can make purchases on the site with **Stripe** being used to handle this. The steps are as below:

 - Set Up Stripe Account and Stripe elements file
 - Create Stripe Elements JS file for Stripe payment intents
 - Order form will render back succesful purchase details to the user
 - Create Webhooks to Secure Payment Intents


**EPIC 7 - User Profile & Contact Page**

This epic handled the requirement for the user to have their own Profile Page, which would provide information about delivery details and previous orders:

- User should Have Their Own Profile page: models and views created for this
- User should be able to use the all auth templates to log in and out
- User Can View Order History
- Have a CONTACT US page to submit and queries to the site owner


**EPIC 7 - Post Record Reviews**

This epic handled a feature that registered site users can avail of. The user can leave reviews against records they have bought. These are approved by site admin for site visitors and to see.

- ??
- ??
- ??

**EPIC 8 - Newsletter**

This epic handled a feature that registered site users can avail of. The user can leave reviews against records they have bought. These are approved by site admin for site visitors and to see.

- ??
- ??
- ??

**EPIC 9 - Deployment**

This epic handled a feature that registered site users can avail of. The user can leave reviews against records they have bought. These are approved by site admin for site visitors and to see.

- ??
- ??
- ??

**EPIC 10 - Documentation**

This epic handled a feature that registered site users can avail of. The user can leave reviews against records they have bought. These are approved by site admin for site visitors and to see.

- ??
- ??
- ??

<br>

# The-Structure-Plane

## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality on Menus and Bookings
* Restricted role based features
* Home page with restaurant information

<br>

## Features

**Navigation Menu**

The Main Navigation contains links for Home, All Vinyl, Record Reviews, Sign In, Register and Contact Us. This also includes the My Account and Shopping Basket icons.

- ***If the user is signed in, they will see sign out and have the option to view their profile from the My Account dropdown***
- ***If the user is the Admin/SuperUser, they will have the Store Management Nav link available to them, and the edit and delete options when on the record details page***

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

![Navbar](docs/readme/main-nav.png)

<br>

**Home Page & Search Bar**

The home page contains a hero image of a seaside restaurant and the restaurant information at the top of the page. This will immediately make it evident to the user, what the purpose of the website is.

The home page contains the main nav, a scrolling banner to detail any deals that are available. It also includes social media links and 2 images. These features are shown as below:

![Home Page](docs/readme/home-page.png)

<br>

The search bar can be used to return any record to the user that matched either the title of artist of the record as shown below:

![Search Bar](docs/readme/search-bar.png)

<br>

**Footer/Newsletter**

???????????????????

![Footer](docs/readme_images/footer.PNG)

<br>

**All Vinyl Page**

This page is accessed when the user selects the ALL VINYL nav link. This will return a list of available records for sale on the site as shown below:

![All Vinyl Page](docs/readme/all-vinyl.png)

<br>

**Record Details Page**

This page will render more details on the record aside from the Title, Artist, Label and Price. This page will show a description and a track list. 

- This includes a quantity selector feature
- And a add to basket or keep shopping buttons
- ***Edit and Delete buttons for SuperUser only***

As shown below:

![Record Details](docs/readme/record-detail.png)

<br>

**Browse Vinyl**

There is a Dropdown BROWSE VINYL link on the main nav. When selected a list of labels appears and the user will be returned with the records of the label they have selected:

![Edit Menu](docs/readme/browse-label.png)

<br>

**Shopping Basket**

The shopping basket page will display all records selected by the user: title, artist, quantity, price and record image. The use will also have the ability to amend quantities and remove records:

![Shopping Basket](docs/readme/basket.png)

<br>

**Secure Checkout & Form**

From the shopping basket page, the site user will have the option to go to the secure checkout in order to finalise their purchase, as shown below:

![Secure Checkout Button](docs/readme/secure-checkout-button.png)

<br>

The site user will then be taken to the Checkout page. They will see a summary of the order they are about to make along with a form they need to submit to complete their purchase, both are shown below:

![Secure Checkout Page](docs/readme/checkout-page.png)

<br>

![Secure Checkout Form](docs/readme/checkout-form.png)


**Checkout Success Page**

After a successful purchase, the site user is then taken to the checkout success page:

![Checkout Success](docs/readme/checkout-form.png)

<br>

**Record Reviews**

The site user can access posted reviews on records that are created by other registered site user, by selecting the RECORD REVIEWS dropdown on the main nav. The site user can also choose to create a review, if they are a registered user.
* ***Only registered users can create reviews, this is also shown below.***

![Posted Review](docs/readme/posted-review.png)
![Review Detail](docs/readme/review-detail.png)
![Create Review](docs/readme/create-review.png)

<br>

**Contact Page**

Site user can use the contact page. The contents of this communication will be sent to the site owner.

![Create Review](docs/readme/contact.png)

<br>

**Store Management**
(***For Super User only***)

Site owner can add a new record. And they can also edit or delete a record from the record details page:

![Add Record](docs/readme/add-record.png)
![Edit/Delete Record](docs/readme/edit-delete.png)

<br>

**Error Pages**

TO BE COMPLETED . . . . . 

<br>

# The-Skeleton-Plane

## Wireframes

TO BE COMPLETED . . . . . 

<br>

# Testing

Test cases and results can be found in the [TESTING.md](TESTING.md) file. This was moved due to the size of the file.

## Ligthouse Testing
Please see screen shot below for results of lighthouse testing on the deployed site

## HTML
 
All pages were run through the [w3 HTML Validator](https://validator.w3.org/)
 
**NOTE:**
- Due to the Django templating language code used in the HTML files, these could not be copied and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI.
 
- To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.
 
<br>
 
## CSS
All pages were run through the [w3 CSS Validator](https://jigsaw.w3.org/css-validator/)
 
<br>
 
## PYTHON
 
All pages were run through the official [CI Python Linter](https://pep8ci.herokuapp.com/) validator to ensure all code was compliant.
 
**NOTE:**
- I had to add # noqa to lines 85 and 86 in the ***webhook_handler.py file in the checkout app*** as I could not find a way to shorten them. 
- I had to add # noqa to lines 21, 22 and 23 in the ***forms.py file in the contact app*** as I could not find a way to shorten them. 
- I had to add # noqa to line 10 in the ***widgets.py file in the products app*** as I could not find a way to shorten them. 
 
<br>
 
## JAVASCRIPT
JavaScript code was run through [JSHINT](https://jshint.com) javascript validator.
 
**NOTE:**
- There is only a very small piece of JavaScript in this project which is found in base.html. The function captures any toasts/messages generated by the app and closes them after 2.5 seconds.
 
<br>
 
## Responsiveness
The html elements of this page have largely been constructed using Bootstrap.
- I have used the Inspect option to go through the responsiveness of all pages:
 