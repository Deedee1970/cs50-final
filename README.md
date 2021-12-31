# CS50 Final Project: My Quiet Place

#### By Denise Donohue

#### Video Demo: https://www.youtube.com/watch?v=JJ5XwyjfwPU

This project is a webpage where users can read God's word, maintain an address book, and keep a personal journal.

Technologies used:

* HTML
* CSS
* JavaScript
* Python
* Flask
* sqlalchemy

#### Description

This is my CS50 final project. I wanted to create a place users can go to get a break from the world. There are three options for users: 

1. Access God's word - users can get a daily verse or delve deeper with a link to [King James Bible Online](https://www.kingjamesbibleonline.org/). 

2. An Address Book - keep all of your family and friend information in one place! Users can update and delete their contacts as needed. We all have that one friend/family member that moves around every few months! It's much easier to edit them here and it saves your erasers!

3. A Personal Journal - As a grief counselor, I encourage family/friends to keep a journal. It helps clear your mind. It helps put things into perspective. It also provides a wonderful way to look back on the days, months, and years that go by so quickly. See how things have changed over time. See how things have remained the same, too. Users can write down their thoughts for the day, prayer requests, pretty much anything they would like to get off their minds. 

### How to Access the Webpage

Users must be registered and logged in for some parts of the website. Users will need a:

* username
* password, which is hashed in the database

To log in, users can enter their name along with the username and password for a slightly more personal touch.

Should users forget to logout, the session will log them out after 30 minutes of non-use.

When users go to the home page, they will be able to access the devotionals without logging in - God's word is free and available to all!

Users must login to access:

* Address book 
* Contact list 
* Journal 
* Prior journal entries

 Of course, you will also need to be logged in to make any changes to your contacts or to delete contacts/journal entries.

### A Brief History: Design Choices and Future Additions

This project has gone through a few changes as it progressed. I considered adding a calendar to link contact's birthday/anniversary information, but just couldn't get it to work. As I learn and grow in this field, I will definitely incorporate it! 

Since I am not able to link birthdays/anniversaries to a calendar, users will find a "Notes" section in the address book. This area is perfect to keep track of these events. This area is also a perfect spot to keep track of where users met the contact and to keep track of children/relatives of the contact.

I also considered adding a waterfall that I created using HTML/CSS. It is very basic, but it goes along with the theme of escaping the outside world for a little bit. Alas, I may just find a way to add it one of these days.

### Database: 

sqlalchemy is used to store the user's registration/login information, family/friend contact information, and journal entries.

### How I Discovered the Beauty of sqlalchemy

I used CS50 Finance as my template for this project. I began the project in the CS50 IDE, using CS50 SQL. This was perfect until I attempted to edit the contact information. No matter how hard I tried, I could not get it to work. Alas, I moved out of the IDE and into VS Code. I researched sqlalchemy and completely converted the original program to what it is today. 

While this caused a bit of setback and frustration (maybe even a few tears), I am actually quite happy things happened the way they did. While SQLite is so much easier to use and I would have loved to do the entire project in the CS50 IDE, moving away and starting over helped me learn so much more. I really like the ability to create models in sqlalchemy. This provides the ability to make changes to the database very easily, which I have learned is very necessary at times! When starting a project like this, one never knows what might be needed in the database(s) down the road. So, this feature is much appreciated!

### Bugs

I did my best to error check, but I am certain there is so much more that could be done. I am sure that after this project is submitted, I will return quite often to make alterations. I can't wait for the day that I look back at it and wonder, "Wow! How could I have been so naive?!" Right now, I can only build this page based on what I have learned thus far. I am certain I will look back on this README page and laugh at it, too!

### Issues?

After hours and hours of searching and so many attempts, I cannot figure out how to get rid of the time stamp for journal entries. I am able to have them return as all 0's, but cannot remove them. Hopefully, some day I will figure it out. Until then, I will keep the time in place, I think it looks better than all 0's.

As of this moment, the Homepage is the only Responsive page. Must continue to work on Responsive Design for entire project.

### What is the Purpose of this Project?

My goal for this project is not simply to finish CS50 and obtain a certificate (that's only a portion). My goal is to create a page that is useful and a small reflection of me. I hope I have achieved that goal. I cannot wait to start using it and sharing it with others!