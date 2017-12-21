# ! /usr/bin/env python3
import psycopg2
import datetime

# Storing the 3 sql queries into query variables.
query1 = '''select articles.title, count(*) as views from articles, log
            where concat('/article/',articles.slug) = log.path
            group by log.path, articles.title order by views desc limit 3;'''

query2 = '''select authors.name, sum(views) as views from authors,
            (select log.path, count(*) as views from articles, log
            where concat('/article/',articles.slug) = log.path group
            by log.path)foo
            group by authors.name order by views desc;'''

query3 = '''select to_char(date, 'FMMonth DD, YYYY'), percent from
            (select total_error.date as date,
            round(100*total_error.error/total_status.status,2) as percent
            from (select date(time) as date, count(*) as error
            from log where  status != '200 OK' group by date(time))total_error,
            (select date(time) as date, count(*) as status from log
            group by date(time))total_status
            where total_status.date = total_error.date)report
            where percent > 1.0  order by percent desc ;'''
# Storing the 3 questions into q variables
q1 = 'Question 1: What are the most popular three articles of all time?'
q2 = 'Question 2: Who are the most popular article authors of all time?'
q3 = 'Question 3: On which days did more than 1%  of requests lead to errors?'
# Connecting the code to database news and executing the queries
if __name__ == '__main__':
    db = psycopg2.connect("dbname=news")
    conn = db.cursor()
    conn.execute(query1)
    data1 = conn.fetchall()
    conn.execute(query2)
    data2 = conn.fetchall()
    conn.execute(query3)
    data3 = conn.fetchall()
    if len(data1) == 0:
        print "NO DATA PRESENT"
    else:
        print q1
        for i in range(len(data1)):
            print str(data1[i][0]) + '--' + str(data1[i][1]) + " views"
        print " "
    if len(data2) == 0:
        print "NO DATA PRESENT"
    else:
        print q2
        for i in range(len(data2)):
            print str(data2[i][0]) + '--' + str(data2[i][1]) + " views"
        print " "
    if len(data3) == 0:
        print "NO ERROR PRESENT"
    else:
        print q3
        for i in range(len(data3)):
            print str(data3[i][0]) + "--" + str(data3[i][1]) + "% error"
        print " "
    db.close()
