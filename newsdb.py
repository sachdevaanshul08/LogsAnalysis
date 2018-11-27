#!/usr/bin/env python3
# "Database code" for the DB News.
# coding=utf-8

import psycopg2


def connect():
    try:
            db = psycopg2.connect("dbname=news")  # Connect to database
            c = db.cursor()  # Create cursor
            return db, c
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)


def get_toparticles():
    conn, cur = connect()
    cur.execute("""SELECT a.title,count(*) as num FROM articles a,
                 log l WHERE l.path = concat('/article/', a.slug) GROUP BY
                 a.title ORDER BY num DESC LIMIT 3""")
    topArticles = cur.fetchall()
    conn.close()
    return topArticles


def most_popularauthors():
    conn, cur = connect()
    cur.execute("""SELECT au.name,count(*) as num FROM articles a, authors
                 au, log l WHERE l.path = concat('/article/', a.slug) and
                 a.author=au.id  GROUP BY au.id ORDER BY num DESC LIMIT 3""")
    popularAuthors = cur.fetchall()
    conn.close()
    return popularAuthors


def get_errorDays():
    conn, cur = connect()
    cur.execute("""SELECT * from (SELECT TO_CHAR(time,'dd Mon YYYY')
                 as times, ROUND(100* (SUM(CASE WHEN status = '404 NOT FOUND'
                 THEN 1 ELSE 0 END)::numeric)/count(*), 2)
                 as percent FROM log GROUP BY times) as alias
                 WHERE alias.percent>1""")
    errorDays = cur.fetchall()
    conn.close()
    return errorDays


print()

# TOP ACCESSED ARTICLES
print("Top Accessed Articles\n")
topArticles = get_toparticles()
for value in topArticles:
    print("\"{}\" - {} views".format(value[0], value[1]))

print()

# MOST POPULAR AUTHORS
print("Most Popular Authors\n")
popularAuthors = most_popularauthors()
for value in popularAuthors:
    print("{} - {} views".format(value[0], value[1]))

print()

# MORE ERRRO DAYS
print("On following days, more than 1% of requests lead to errors\n")
errorDays = get_errorDays()
for value in errorDays:
    print("{} - {} % errors".format(value[0], value[1]))
