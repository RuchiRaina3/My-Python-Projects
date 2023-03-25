# <h1 align=center>My-Python-Projects</h1>


<p align="center">
  <img width='300' height='250' src='/Assets/Namaste.jpg'> 
</p>

I am sharing few of my python projects which I have developed and still developing along my self-learning journey.
Few were for college grades, more are for fun!!!
<br>
<br>
In the README, I am listing brief description of handful of these projects.

## **6 Degrees Of Separation**
Six degrees of separation is the theory that any person on the planet can be connected to any other person on the planet through a chain of acquaintances that has no more than five intermediaries. To test it I have taken facebook data in file facebook_combined.txt.gz. 
This is in edge list representation. Here anonymous people 
are taken as nodes and edge between any two nodes 
represents friendship between them. Now, we have to prove
the theory of Six Degrees of Separation. 

 **Modules Used :** networkx, numpy <br>
 <a href='/Projects/6 Degrees Of Separation'> <strong> <em> Visit Project </strong> </em> </a>
 
## **Automatic Birthday Wisher**
This is a program to automatically wish the person on her birthday via email. For that, an excel sheet has to be craeted in the folder where is the source file. We will add the following rows, such as Sno, Name, Birthday, Message, Year, Email. I have shared the sample file. Now to send email we will use the smtplib library. We will be using Gmail for this application. Now we need to create a function which will send email using a gmail id. To use this service we need to enable less secure apps on the gmail account. And finally we will schedule the program from the task scheduler for 12:00 AM daily.

 **Modules Used :** pandas, datetime, smtplib <br>
 <a href='/Projects/Automatic Birthday Wisher'> <strong> <em> Visit Project </strong> </em> </a>

## **Automatic Folder Organiser**
We all have some folder like Downloads folder which are very messy. For such situations, this program comes to rescue. It will organise all the files into different folders viz 'Images', 'Documents', 'Music', 'Videos', 'Applications', 'Zipped'.
Then again within in the Documents, it will organise the files into folders - 'Word', 'Presentation', 'Pdf', 'Text', 'Excel', 'CSV', 'Web Pages'
To use this program you have to move it to the folder which you want to organise and then run it from there.

**Modules Used :** os <br>
 <a href='/Projects/Automatic Folder Organiser.py'> <strong> <em> Visit Project </strong> </em> </a>
