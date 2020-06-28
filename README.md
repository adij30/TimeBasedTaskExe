# TimeBasedTaskExecution
Here Anyonene can create task,based on time

#### Prerequisites
Python Version: 3.X.X

####
#### Running the tests
##### 1.Test for TimeBase

A) CALL U2 India 13:00:00 14:30:00<br>
Current time: 13:30:00<br> Output:
True

 B) CALL U1 India 13:00:00 14:30:00<br>
Current time: 16:30:00<br> Output:
False

c)CALL U2 India 13:00:00 14:30:00<br>
Current time: 12:00:00<br> Output:
13:00:00


##### 2.For enhanced version
A)Email - U1 - India - 13:30:00 14:30:00 Tuesday and Thursday<br> Current datetime: Wednesday 12:00:00<br>
Output:
Thursday 13:30:00

B)Email - U1 - India - 13:30:00 14:30:00 Tuesday and Thursday<br> Current datetime: Friday 12:00:00<br>
Output:
Tuesday 13:30:00

C)Email - U1 - India - 13:30:00 14:30:00 Tuesday and Thursday<br> Current datetime: Thusday 14:00:00<br>
Output:
True

#### For example
##### 1.For TimeBased
Enter your Task Type(Email,Call,SMS):Call<br>
UserName:Suhas<br>
Enter a Start time in 24Hours format as HH:MM:SS :12:00:00<br>
Enter a End time in 24Hours format as HH:MM:SS : 13:00:00<br>
T/t-TimeBased<br>
E/e-EnhancedTimeBased<br>
Choose your option pleaze T/t OR E/e:t<br>
Your Entered Input: <br>
Call Suhas 12:00:00 13:00:00<br>
Output:<br>
12:00:00

##### 2. For EnhacedTimeBased
Enter your Task Type(Email,Call,SMS):Email<br>
UserName:Suhas<br>
Enter a Start time in 24Hours format as HH:MM:SS :14:00:00<br>
Enter a End time in 24Hours format as HH:MM:SS : 16:00:00<br>
T/t-TimeBased<br>
E/e-EnhancedTimeBased<br>
Choose your option pleaze T/t OR E/e:e<br>
Monday Tuesday Wednesday Thursday Friday Saturday Sunday<br>
Enter 1st day for Session(must entered as shown):Monday<br>
Enter 2nd day for Session(must entered as shown):Tuesday<br>
Your Entered Input:<br> 
Email Suhas 14:0:00 16:00:00 Monday Tuesday<br>
Output:<br>
Monday 14:00:00



#### Versioning
We use Git for versioning. For the versions available, see the tags on this repository.

#### Author
 Suhas Wani- Software Developer - bitwin Technology


