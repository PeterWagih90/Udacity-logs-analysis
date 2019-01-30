#!/usr/bin/env python3

import psycopg2

DATABASE_NAME = "news"

# What are the most popular three articles of all time?


def top3_articles():

    print ("What are the most popular three articles of all time?")

    output = [('Path', 'Count')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    cur = db.cursor()
    # Query
    cur.execute("create or replace view article_counting as select" +
                " path, count(*) as count from log group by path" +
                " order by count desc limit 3 offset 1;")
    cur.execute("select a.title, c.count from articles a inner join" +
                " article_counting c on '/article/' || a.slug =" +
                " c.path order by c.count desc")
    output += cur.fetchall()
    db.close()

    return output

# Who are the most popular article authors of all time


def top5_articles_writers():
    print ("Who are the most popular article authors of all time?")
    output = [('Path', 'Count')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    cur = db.cursor()
    # Using join between tables to uses the stats from log table
    cur.execute("select au.name, count(au.name) as count from authors au" +
                " inner join articles a on au.id = a.author inner join" +
                " log l on '/article/' || a.slug = l.path group by" +
                " au.name order by count desc limit 5;")
    output += cur.fetchall()
    db.close()

    return output

# On which days did more than 1% of requests lead to errors?


def get_error_stats_by_day():

    print ("On which days did more than 1% of requests lead to errors?")
    output = [('Day', 'Error Percentage')]
    db = psycopg2.connect(dbname=DATABASE_NAME)
    cur = db.cursor()
    # Creating a view to break the query
    cur.execute("create or replace view error as select date(time)," +
                " count(*) as count from log where status =" +
                " '404 NOT FOUND' group by date(time) order by" +
                " count desc;")
    cur.execute("create or replace view successful as select date(time)," +
                " count(*) as count from log where status ='200 OK' " +
                "  group by date(time) order by count desc;")
    # Query to calculate the percentage
    cur.execute("select e.date, round( (100 * cast(e.count as decimal) /" +
                " cast(s.count as decimal)),2) as percentage from " +
                " error e inner join successful s on e.date = s.date " +
                " WHERE round( (100 * cast(e.count as decimal) /" +
                " cast(s.count as decimal)),2)>1 " +
                " order by e.count desc;")
    output += cur.fetchall()
    db.close()

    return output

# Function used to style the output: Option1 to
# views and Option2 to Error


def print_list(option, list):
    if option == 'OPCAO1':
        for x in range(len(list)):
            print ("%s views  %s " % list[x])
    elif option == 'OPCAO2':
        for x in range(len(list)):
            print ("%s - %s %% errors " % list[x])
    else:
        print ("Invalid: Option not found!")


def main():

    print
    print_list('OPCAO1', top3_articles())
    print
    print_list('OPCAO1', top5_articles_writers())
    print
    print_list('OPCAO2', get_error_stats_by_day())
    print


if __name__ == "__main__":
    # execute only if run as a script
    main()
