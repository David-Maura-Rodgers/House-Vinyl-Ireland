# Functional Testing
 
## Authentication tests

<br>

**Description:**
 
Ensure that site user can register as a user on the site with required credentials
 
Steps:
 
1. Navigate to [House Vinly Ireland](https://house-vinyl-ireland.herokuapp.com) and click Register link on Nav Bar
2. Enter username, email and password
3. Click Sign up
 
Expected:
 
If all required details are entered successfully, the user can then access the site for it's intended use.
 
Actual:
 
User is informed that they have signed up successfully and they have access to site functionality

<hr>
<br>
 
**Description:**
 
**User is able to sign in to the site**
 
Steps:
1. Navigate to [House Vinly Ireland](https://house-vinyl-ireland.herokuapp.com) and click Sign In on the Nav Bar
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
 
**Quantity function, Add to Basket function and Keep Shooping function**
 
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
 
**User can edit their reviews**
 
Steps:
1. Ensure site user is logged in
2. From either the Home page or Your Reviews page, click on any review owned by the user
3. Click on the Edit Review button
4. Change text in fields
5. Click on Submit Changes button
 
Expected:
 
User can click the Edit Review button from their reviews once they are on the review detail page. They are then taken to a form which allows user to edit previously entered content.
 
Actual:
 
User can click the Edit Review button from their reviews once they are on the review detail page. They are then taken to a form which allows user to edit previously entered content. They are then redirected to the Your Reviews page and receive a toast message confirming that they have successfully updated their review.
 
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
 
**User can Edit and Delete *ONLY* their own reviews**
 
Steps:
1. Ensure site user is logged in
2. From either the Home page or Your Reviews page, click on any review owned by the user
 
Expected:
 
If the user is not the gamer/owner of their post, they should not be able to see any option to Edit or Delete a review.
 
Actual:
 
User can only see an option to go back to the Home page, and no buttons appear for Edit or Delete review.
 
<hr>
<br>
 
**Description:**
 
**All nav links and buttons work as intended**
 
Steps:
1. Ensure site user is logged in
2. Click all navbar links to ensure they direct user as intended
3. Click all Review Title links (with dynamic colour background) to make sure they go to the corresponding review detail page
4. Click all Cancel, Submit and Back to home buttons
 
Expected:
 
User should be able to click on all links and buttons as described in the steps above and works as intended
 
Actual:
 
User can click on all links and buttons as described in the steps above and they work as intended
 
<hr>
<br>
 
**Description:**
 
**All social media footer icon links work as intended**
 
Steps:
1. Ensure site user is logged in
2. Click all icon links in footer to ensure they direct user as intended
 
Expected:
 
User should be able to click on all icon links in the footer as described in the steps above and work as intended
 
Actual:
 
User can click on icon links in the footer as described in the steps above and they work as intended
 
<hr>
<br>
 
**Description:**
 
**Site Pagination works as intended**
 
Steps:
1. Ensure site user is logged in
2. Ensure there is more than 6 review posts on the home page and/or Your Reviews page
3. Click on previous and next buttons that appear once the above condition is met
 
Expected:
 
User should be able to click on the next button which appears if there are more than 6 review posts on a page. Similarly, user should be able to go back from that page to previous page with the back button
 
Actual:
 
User can click on both the next and previous buttons if there are more that 6 review posts on Home page or Your Reviews page