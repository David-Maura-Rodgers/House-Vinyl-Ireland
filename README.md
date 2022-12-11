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
* Use basket icon on main nav bar to access my shopping basket from anywhere on the site. 
* Be able to review purchases from secure checkout page and be given an appropriate breakdown
* Be able to remove or amend quantity on secure checkout page 
* Be able to checkout of the site and pay for selected records

### Profile: 
* Be able to enter my personal information in a secure environment.
* Have the option to register with the site to save my personal information for a faster checkout next time I visit the site.
* I would like to have the option to have my order sent to a different address to the billing address.
* I would like to have the option to add a gift tag and have the items wrapped.
* I would like to pay for my purchase using a trusted payment portal.
* On submitting my order, I would like to receive a confirmation email with my order details and a unique order number.
* I would like to receive a dispatch confirmation email with and estimated delivery date.
* Be able to contact the site owner by means of a contact form.
* Be able to subscribe to a newsletter.
* Have the option to unsubscribe from the newsletter mailing list.


* As a registered site visitor I would like to:
  * Have the option to login with a social media account for a speedier "1 click" login.
  * Be able to access my account/profile page.
    * I would like to be able to view my personal information.
    * I would like to be able to update my personal information.
    * I would like to be able to delete my personal information.
    * I would like to be able to view my order history and any current orders to track progress.
    * I would like the option to delete my account.
  * Be able to publish reviews and ratings of products I have received.
    * I would like to be able to create a review.
    * I would like to be able to update a review.
    * I would like to be able to delete a review.
    * I would like to be able to rate a product out of 5 stars.
 
#### Site Owner Goals
 
* As the site owner I would like to:
  * Provide a site that's highly accessible to all customers.
  * Be able to advertise any offers or relative information to customers by means of an information banner.
  * Be able to gather subscribers for my newsletter by advetising the link on the site.
  * Be able to manage products.
    * I would like to be able to add new products to the site.
    * I would like to be able to update existing products.
    * I would like to be able to delete existing products.
  * Be able to view my workload.
    * I would like to be able to view all current orders in production sorted by date ordered.
    * I would like to be able to change the status of an order when the product has been created.
    * I would like to change the status of an order when the product has been dispatched.
    * I would like to send an order despatched email to the customer when the order is complete.

