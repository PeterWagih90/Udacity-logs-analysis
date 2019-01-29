# Logs Analysis

A Udacity FSND project.


## Introduction

This is the solution for the Logs Analysis project in Udacity Full Stack Nanodegree course.
In this, we have to execute complex queries on a large database (> 1000k rows) to extract intersting stats.

The database in question is a newspaper company database where we have 3 tables; `articles`, `authors` and `log`.
* `articles` - Contains articles posted in the newspaper so far.
* `authors` - Contains list of authors who have published their articles.
* `log` - Stores log of every request sent to the newspaper server.

This project implements a single query solution for each of the question in hand.
See [logs-analysis-project.py](logs-analysis-project.py) for more details.

## File location

Keep in mind that if file wasn't executed on root `/` use `vagrant/logs-analysis-project`


## View Creation Statement
create or replace view article_counting as select 
                     path, count(*) as count from log group by path
                     order by count desc limit 3 offset 1;
					
## Running

* Make sure you have `newsdata.sql`, the SQL script file with all the data. It can be downloaded from the Udacity course page.

* Then run the following command to execute it in `news` database. You might have to create the database before-hand.

```sh
psql -d news -f newsdata.sql
```

* Finally run the script.

```sh
python2 /vagrant/logs-analysis-project.py
```

* It will present you with necessary stats.
Please see result file.
