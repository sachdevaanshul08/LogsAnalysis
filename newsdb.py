#!/usr/bin/env python3
# "Database code" for the DB News.
# coding=utf-8

import psycopg2


def get_toparticles():
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    cur.execute("""select a.slug,count(*) as num from articles a,
                 log l where l.path LIKE '%'|| a.slug group by
                 a.slug order by num desc limit 3""")
    topArticles = cur.fetchall()
    conn.close()
    return topArticles


def most_popularauthors():
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    cur.execute("""select au.name,count(*) as num from articles a,
                 authors au, log l where l.path LIKE '%'|| a.slug and
                 a.author=au.id  group by au.id order by num desc limit 3""")
    popularAuthors = cur.fetchall()
    conn.close()
    return popularAuthors


def get_errorDays():
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    cur.execute("""select * from (SELECT TO_CHAR(time,'dd Mon YYYY')
                 as times, ROUND(100* (SUM(CASE WHEN status like
                '4'||'%' THEN 1 ELSE 0 END)::numeric)/count(*), 2)
                 as percent FROM log group by times) as alias
                 where alias.percent>1""")
    errorDays = cur.fetchall()
    conn.close()
    return errorDays


print()

# TOP ACCESSED ARTICLES
print("Top Accessed Articles\n")
topArticles = get_toparticles()
for value in topArticles:
    print("\"" + value[0] + "\"" + " — " + str(value[1]) + " views")

print()

# MOST POPULAR AUTHORS
print("Most Popular Authors\n")
popularAuthors = most_popularauthors()
for value in popularAuthors:
    print(value[0] + " — " + str(value[1]) + " views")

print()

# MORE ERRRO DAYS
print("On following days, more than 1% of requests lead to errors\n")
errorDays = get_errorDays()
for value in errorDays:
    print(value[0] + " - " + str(value[1]) + "% errors\n")
