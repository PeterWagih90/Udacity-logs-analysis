# Log_Analysis_Udacity

## A. Softwares required by the log analysis project: ##
	1. Python
	2. psycopg2
	3. PostgreSQL 
 A vagrant managed virtual machine(VM) is used to run the log analysis project which includes the above softwares. This will need Vagrant and VirtualBox software installed on your system.

## B. Setup Project and Installation: ##
	1. Install Vagrant and VirtualBox
	2. Download or Clone fullstack-nanodegree-vm repository.
	3. Copy the newsdata.sql file and content of this current repository, by downloading. it from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

	

## C. Launching the Virtual Machine: ##
	1. To run the Vagrant VM in Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
 		 *$ vagrant up
	2. Then Log into VM using command:
  		*$ vagrant ssh
	3. Change directory to /vagrant and check for the files using ls.
	4. Load the data from the database using the command:
  		*$ psql -d news -f newsdata.sql
	    (i )  use \c to connect to database="news"
	    (ii)  use \dt to see the tables in database
	    (iii) use \dv to see the views in database
	    (iv) use \q to quit the database
		
		
## D. Running
   1. Make sure you have newsdata.sql, the SQL script file with all the data. It can be downloaded from the Udacity course page.

   2. Then run the following command to execute it in news database. You might have to create the database before-hand.

   3. psql -d news -f newsdata.sql (if you didn't load it already)

   4. Finally run the script.
   python2 /vagrant/logs-analysis-project.py
   
   5. It will present you with necessary stats.
   

## E. The database includes three tables: ##
	1. The Authors table
	2. The Articles table
	3. The Log table

## F. PSQL Command Used To create views on these tables: ##
	1.The authors table includes information about the authors of articles.
	Create view article_counting using:
	create or replace view article_counting as select path, count(*) as count from log group by path order by count desc limit 3 offset 1;

	
	2.The log table includes one entry for each time a user has accessed the site.
	Create view error using:
	create or replace view error as select date(time), count(*) as count from log where status ='404 NOT FOUND' group by date(time) order by count desc;
	
	Create view successful using:
	create or replace view successful as select date(time), count(*) as count from log where status ='200 OK' group by date(time) order by count desc;

## G. Running the queries: ##
	1. From the vagrant directory inside the virtual machine,run newsdata.py using:
		  *$ python newsdata.py
		  
## K. Calculating Results:(Output) ##
	1. What are the most popular three articles of all time?
	Path views  Count
	Candidate is jerk, alleges rival views  338647
	Bears love berries, alleges bear views  253801
	Bad things gone, say good people views  170098

	2. Who are the most popular article authors of all time?
	Path views  Count
	Ursula La Multa views  507594
	Rudolf von Treppenwitz views  423457
	Anonymous Contributor views  170098
	Markoff Chaney views  84557

	3. On which days did more than 1% of requests lead to errors?
	Day - Error Percentage % errors
	2016-07-17 - 2.32 % errors
