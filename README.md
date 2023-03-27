# <h1 align=center>My-Python-Projects</h1>


<p align="center">
  <img width='300' height='250' src='/Assets/Namaste.jpg'> 
</p>

I am sharing few of my python projects which I have developed and still developing along my self-learning journey.
Few were for college grades, more are for fun!!!
<br>
<br>
In the README, I am listing brief description of handful of these projects.
 
## **Automatic Birthday Wisher**
This is a program to automatically wish the person on her birthday via email. For that, an excel sheet has to be craeted in the folder where is the source file. We will add the following rows, such as Sno, Name, Birthday, Message, Year, Email. I have shared the sample file. Now to send email we will use the smtplib library. We will be using Gmail for this application. Now we need to create a function which will send email using a gmail id. To use this service we need to enable less secure apps on the gmail account. And finally we will schedule the program from the task scheduler for 12:00 AM daily.

 **Modules Used :** pandas, datetime, smtplib <br>
 <a href='/Projects/Automatic Birthday Wisher'> <strong> <em> Visit Project </strong> </em> </a>

## **Automatic Folder Organiser**
We all have some folder like Downloads folder which are very messy. For such situations, this program comes to rescue. It will organise all the files into different folders viz 'Images', 'Documents', 'Music', 'Videos', 'Applications', 'Zipped'.
Then again within in the Documents, it will organise the files into folders - 'Word', 'Presentation', 'Pdf', 'Text', 'Excel', 'CSV', 'Web Pages'
To use this program you have to move it to the folder which you want to organise and then run it from there.

**Packages/Libraries Used :** os <br>
 <a href='/Projects/Automatic Folder Organiser.py'> <strong> <em> Visit Project </strong> </em> </a>
 
## **Colourful Spiral Traversing**
This program makes spiral traversing in colourful lines. For this purpose, I have used turtle module.
   ![Colourful](https://user-images.githubusercontent.com/92518496/227700398-63fb24eb-dee4-4c1b-830a-766781d4886a.gif)
   
**Packages/Libraries Used :** turtle, random <br>
 <a href='/Projects/Colourful Spiral Traversing.py'> <strong> <em> Visit Project </strong> </em> </a>

## **Image Processing**
This program is divided into two sections:
 <pre>     1. Flipping the mirriored image - As image is stored as a matrix in computer. Now, to flip the image, we have to 
        flip that matrix i.e. transpose that matrix
     2. Enhancing the image - Image enhancement is done using Contrast limited Adaptive Histogram Equalization (CLAHE). 
        CLAHE technique works better when image is black and white. So first it is converted in Gray Scale Image, then 
        CLAHE is applied using built-in function.           </pre>
        
 **Packages/Libraries Used :** Image from PIL, cv2 <br>
 <a href='/Projects/Image Processing'> <strong> <em> Visit Project </strong> </em> </a>      
  
## **6 Degrees Of Separation**
Six degrees of separation is the theory that any person on the planet can be connected to any other person on the planet through a chain of acquaintances that has no more than five intermediaries. To test it I have taken facebook data in file facebook_combined.txt.gz. 
This is in edge list representation. Here anonymous people 
are taken as nodes and edge between any two nodes 
represents friendship between them. Now, we have to prove
the theory of Six Degrees of Separation. 

 **Packages/Libraries Used :** networkx, numpy <br>
 <a href='/Projects/6 Degrees Of Separation'> <strong> <em> Visit Project </strong> </em> </a>
 
## **Lottery Simulation Program**
This is a lottery simulation to give an idea of how many times a person can win in given number of times. Price of 1 bet is Rs.100 and winning amount is Rs.1000.
account variable keeps the track of the net money you have.    
User will be asked for how many times he want to play.    
Finally, a graph will be plotted to have a look at the patter of net profit or loss 

**Packages/Libraries Used :** random, matplotlib.pyplot <br>
 <a href='/Projects/Lottery Simulation Program.py'> <strong> <em> Visit Project </strong> </em> </a>

## **Whatsapp Automation**
This is Whatsapp Automation project. Here, I have send Whatsapp messages to one of my contacts using Python. To do so, we need to install chromedriver. It will also
require inspecting web elements. Detailed steps are given as comments in the code itself.

**Packages/Libraries Used :** selenium <br>
<a href='/Projects/Whatsapp Automation Using Python.py'> <strong> <em> Visit Project </strong> </em> </a>

## **FLAMES**
This is the classic FLAMES - 'FRIENDS','LOVE','AFFECTION','MARRIAGE','ENEMIES','SIBILING' game. I am sure almost everyone would have played it in childhood.
This game involves the name of two persons. After applying a logic, they are termed one of these - 'FRIENDS','LOVE','AFFECTION','MARRIAGE','ENEMIES','SIBILING'.

**Packages/Libraries Used :** string <br>
<a href='/Projects/Games/FLAMES.py'> <strong> <em> Visit Project </strong> </em> </a>

## **Monty Hall**
This game is based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a BMW; behind the others, goats. You pick a door, say No. 1, 
and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?"
There are 3 doors, one contains BMW and other two contain goats. Is it to your advantage to switch your choice?
We have to check the number of wins with swap and without swap.

**Packages/Libraries Used:** random <br>
<a href='/Projects/Games/Monty Hall.py'> <strong> <em> Visit Project </strong> </em> </a>

## **Tic Tac Toe**
This is the simulation of the classic tic tac toe game.
**Packages/Libraries Used :** numpy <br>
<a href='/Projects/Games/Tic Tac Toe.py'> <strong> <em> Visit Project </strong> </em> </a>

 
