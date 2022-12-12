# Functional Testing
 
## Authentication tests

<br>

**Description:**
 
Ensure that site user can register as a user on the site with required credentials
 
Steps:
 
1. Navigate to [House Vinyl Ireland](https://house-vinyl-ireland.herokuapp.com) and click Register link on Nav Bar
2. Enter username, email and password
3. Click Sign up
 
Expected:
 
If all required details are entered successfully, the user can then access the site for its intended use.
 
Actual:
 
User is informed that they have signed up successfully and they have access to site functionality

<hr>
<br>
 
**Description:**
 
**User is able to sign in to the site**
 
Steps:
1. Navigate to [House Vinyl Ireland](https://house-vinyl-ireland.herokuapp.com) and click Sign In on the Nav Bar
2. Enter login details
3. Click login
 
Expected:
 
User is successfully logged in and redirected to the home page
 
Actual:
 
User is successfully logged in and redirected to the home page
 
<hr>
<br>
 
**Description:**
 
**User is able to sign out of the site**
 
Steps:
1. Login to the website
2. Click the on Sign Out on the Nav Bar
3. Click confirm on the confirm logout page
 
Expected:
 
User is logged out
 
Actual:
 
User is logged out

<hr>
<br>

**Description:**
 
**Home Page**
 
Steps:
1. Login to the website
2. From anywhere on the site user can access the home page
3. User arrives at home page as the default page for the site
 
Expected:
 
User arrives at the Home Page when they first arrive to the site. User can get back to Home page from anywhere on site by clicking on the Home Page main nav link
 
Actual:
 
User arrives at the Home Page when they first arrive to the site. User can get back to Home page from anywhere on site by clicking on the Home Page main nav link

<hr>
<br>

**Description:**
 
**All nav links and buttons work as intended**
 
Steps:
1. Ensure site user is logged in
2. Click all navbar links to ensure they direct user as intended
4. Click all Cancel, Submit and Home buttons
 
Expected:
 
User should be able to click on all links and buttons as described in the steps above and works as intended
 
Actual:
 
User can click on all links and buttons as described in the steps above and they work as intended
 
<hr>
<br>
 
**Description:**
 
**Site Pagination works as intended**
 
Steps:
1. Ensure site user is logged in
2. Ensure there is more than 6 review posts on the posted review page
3. Click on previous and next buttons that appear once the above condition is met
 
Expected:
 
User should be able to click on the next button which appears if there are more than 6 review posts on a page. Similarly, user should be able to go back from that page to previous page with the back button
 
Actual:
 
User can click on both the next and previous buttons if there are more that 6 review posts on Home page or posted reviews page

<hr>
<br>

**Description:**
 
**Social Media Links**
 
Steps:
1. Login to the website
2. User can click on the Social Media Links provided on Home page and be taken to the corresponding page
 
Expected:
 
From the Home Page, user can click on the Social Media Links provided and be taken to the corresponding social media page in a new window
 
Actual:
 
From the Home Page, user can click on the Social Media Links provided and be taken to the corresponding social media page in a new window

<hr>
<br>
 
**Description:**
 
**User can view a list of records**
 
Steps:
1. Ensure site user is logged in
2. Click on All Vinyl link on the Nav Bar
 
Expected:
 
Site user can see a list or all records available on the site. Including record image, title, artist, label and price.
 
Actual:
 
Site user can see a list of all records available on the site with all the info mentioned above.
 
<hr>
<br>

**Description:**
 
**User Can View Records by Label**
 
Steps:
1. Ensure site user is logged in
2. Click on Browse Vinyl link on the Nav Bar
3. From the dropdown, select which label they want
 
Expected:
 
Site user can see a list or all records under a particluar Label selected from the dropdown list.
 
Actual:
 
Site user can see a list or all records under a particluar Label selected from the dropdown list.
 
<hr>
<br>
 
**Description:**
 
**User can see further details on Record**
 
Steps:
1. Ensure site user is logged in
2. Click on record image to be taken to record deatils page
 
Expected:
 
User selects record they want to see more details on by clicking on record image shown from the list of available records on the products page. They are then shown the record description and track list.
 
Actual:
 
User selects record they want to see more details on by clicking on record image shown from the list of available records on the products page. They are then shown the record description and track list.
 
<hr>
<br>
 
**Description:**
 
**Quantity function, Add to Basket function and Keep Shopping function**
 
Steps:
1. Ensure site user is logged in
2. Click on quantity minus and plus signs to adjust quantity
3. Click Add to Basket button
4. Click on Keep Shopping button
 
Expected:
 
User can successfully select the quantity of the select record, they can also add to the shopping basket and receive a toast to confirm this. They can aslo return to a list of all the available records when the click Keep Shopping button.
 
Actual:
 
User can successfully select the quantity of the select record, they can also add to the shopping basket and receive a toast to confirm this. They can aslo return to a list of all the available records when the click Keep Shopping button.
 
<hr>
<br>
 
**Description:**
 
**Shopping Basket Icon and Secure Checkout link**
 
Steps:
1. Ensure site user is logged in
2. Click on either the Shopping Basket Icon or the Secure Checkout link that appears on the toast message upon adding records
to the shopping basket
 
Expected:
 
User is taken to the secure checkout page if they either click on the Shopping Basket Icon or the Secure Checkout link that appears on the toast message
 
Actual:
 
User is taken to the secure checkout page if they either click on the Shopping Basket Icon or the Secure Checkout link that appears on the toast message
 
<hr>
<br>
 
**Description:**
 
**Update and/or Remove Records from Basket Page**
 
Steps:
1. Ensure site user is logged in
2. Change quanity and click update
3. Or click remove ti get get rid of record from basket completely
 
Expected:
 
User can adjust the quantity of record in the bag, click update and the new quantity will be displayed. User can also remove record and it be removed from the basket.
 
Actual:
 
User can adjust the quantity of record in the bag, click update and the new quantity will be displayed. User can also remove record and it be removed from the basket.
 
<hr>
<br>
 
**Description:**
 
**Successfuly Arrive at Checkout Page**
 
Steps:
1. Ensure site user is logged in
2. Click on secure checout button from the basket page
 
Expected:
 
User is taken to page where they can see and order summary and order form that must be completed to complete the purchase
 
Actual:
 
User is taken to page where they can see and order summary and order form that must be completed to complete the purchase
 
<hr>
<br>
 
**Description:**
 
**Payment is taken successfuly and order summary is display**
 
Steps:
1. Ensure site user is logged in
2. Complete Order Form 
3. Complete Card Payment Details
4. Click on Complete Order
 
Expected:
 
User can complete the order form and card payment details on checkout page, and then click the Complete Order button to finalise the transaction. Once this is done, user will be shown an order summary and have an email sent to them as confirmation.
 
Actual:
 
User can complete the order form and card payment details on checkout page, and then click the Complete Order button to finalise the transaction. Once this is done, user will be shown an order summary and have an email sent to them as confirmation.
 
<hr>
<br>
 
**Description:**
 
**User can delete their reviews**
 
Steps:
1. Ensure site user is logged in
2. From either the Home page or Your Reviews page, click on any review owned by the user
3. Click on the Delete Review button
4. Click on Confirm Delete button
 
Expected:
 
User can click the Delete Review button from their reviews once they are on the review detail page. They are then taken to a page which asks them to either Confirm Delete or Cancel Delete via buttons.
 
Actual:
 
User can click the Delete Review button from their reviews once they are on the review detail page. They are then taken to a page which asks them to either Confirm Delete or Cancel Delete via buttons.
 
<hr>
<br>
 
**Description:**
 
**Record Reviews: Posted Reviews**
 
Steps:
1. Ensure site user is logged in
2. Click on the RECORD REVIEWS nav link on main nav
3. From this dropdown select Posted Reviews
 
Expected:
 
User can see all reviews posted by other site users on records that are available for purchase
 
Actual:
 
User can see all reviews posted by other site users on records that are available for purchase
 
<hr>
<br>

**Description:**
 
**Record Reviews: Create a Review**
 
Steps:
1. Ensure site user is logged in
2. Click on the RECORD REVIEWS nav link on main nav
3. From this dropdown select Create A Review
4. Submit a review
 
Expected:
 
User can access the form on the create a review page. They can successfully complete the required fields on this form and and submit their review to Admin for approval.
 
Actual:
 
User can access the form on the create a review page. They can successfully complete the required fields on this form and and submit their review to Admin for approval.
 
<hr>
<br>


**Description:**
 
**Contact Us Page**
 
Steps:
1. Ensure site user is logged in
2. Click on the CONTACT US link on main nav
3. Submit the form with your message
 
Expected:
 
User can access the form on the complete a message to be sent to the site admin.
 
Actual:
 
User can access the form on the complete a message to be sent to the site admin.
 
<hr>
<br>


**Contact Us Page**
 
Steps:
1. Ensure site user is logged in
2. Click on the CONTACT US link on main nav
3. Submit the form with your message
 
Expected:
 
User can access the form on the Contact Us page and complete a message to be sent to the site admin.
 
Actual:
 
User can access the form on the Contact Us page and complete a message to be sent to the site admin.
 
<hr>
<br>

**My Profile Page**
 
Steps:
1. Ensure site user is logged in
2. Click on the MY ACCOUNT main nav link
3. From this dropdown, click on My Profile
 
Expected:
 
User can access a list of previous orders from the My Profile page. They can click on the order number links and get more details about their prevouse purchases.
 
Actual:
 
User can access a list of previous orders from the My Profile page. They can click on the order number links and get more details about their prevouse purchases.
 
<hr>
<br>

**Store Management - Add Record**
 
Steps:
1. Ensure site admin is logged in
2. Click on the STORE MANAGEMENT main nav link
3. Enter details of a new record to be added
 
Expected:
 
Site Admin can click on STORE MANAGEMENT main nav link and be taken to the form to add a new record. Once done, they will be taken directly to this records detail page.
 
Actual:
 
Site Admin can click on STORE MANAGEMENT main nav link and be taken to the form to add a new record. Once done, they will be taken directly to this records detail page.
 
<hr>
<br>

**Store Management - Edit and Delete Record**
 
Steps:
1. Ensure site admin is logged in
2. Click on the any record from the records page
3. Click on either the Edit or Delete buttons
4. If edit is selected, complete the form for the record to be edited
 
Expected:
 
Site Admin can click on any record and be taken to the record details page, form there they can select to either edit or delete the record. If they chose to Edit, they can complete a form for these records and be shown the edited record straight after submission. If the select Delete, the record will be removed from the record database, both front and back end.
 
Actual:
 
Site Admin can click on any record and be taken to the record details page, form there they can select to either edit or delete the record. If they chose to Edit, they can complete a form for these records and be shown the edited record straight after submission. If the select Delete, the record will be removed from the record database, both front and back end
 
<hr>
<br>
 
**Form Validation - Across Entire Site**
 
Steps:
1. Ensure site user is logged in
2. Click on any page, like those listed above and attempt to complete the form
3. Enter values that you expect to throw an error back to you
4. Enter values that you know should be accepted and submit the form
 
Expected:
 
Site user can access all forms on the site and attempt to submit with values they would expect to pass form validation. Site user can also enter details that they would expect to fail or type mistakenly and they are met with an error message telling them the error they have made.
 
Actual:
 
Site user can access all forms on the site and attempt to submit with values they would expect to pass form validation. Site user can also enter details that they would expect to fail or type mistakenly and they are met with an error message telling them the error they have made.
 
<hr>
<br>
