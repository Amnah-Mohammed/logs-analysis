# /usr/bin/python2.7
import psycopg2
DBNAME = "news"

db = psycopg2.connect(database=DBNAME)  # Connect to news


# Takes a query as parameter and returns a result
def ex_query(query):
    cursor = db.cursor()  # create a database cursor
    cursor.execute(query)  # execute the query
    rows = cursor.fetchall()  # fetchall rows
    return rows


#  Q for1 question Return the most popular 3 articles of all time
first_query = """
           SELECT articles.title,
           count(*)
           FROM articles,log
           WHERE log.path = concat('/article/',articles.slug)
           GROUP BY articles.title
           ORDER BY count(*) desc
           LIMIT 3;
    """


first_query_result = ex_query(first_query)
print('1. What are the most popular three articles of all time?')
for result in first_query_result:
    print("\"" + str(result[0]) + "\"" + ' -- ' + str(result[1]) + ' views ')
print("\n")

# Q for the 2 question Return the most popular article authors of all time
second_query = """
            SELECT authors.name,
             count(*)
            FROM articles,authors, log
            WHERE log.path = concat('/article/',articles.slug)
            AND articles.author = authors.id
             GROUP BY name
             ORDER BY count(*) DESC;
     """

second_query_result = ex_query(second_query)
print('2. Who are the most popular article authors of all time?')
for result in second_query_result:
    print("\"" + str(result[0]) + "\"" + ' -- ' + str(result[1]) + ' views ')
print("\n")

# Q for the 3 question Return days did more than 1% of requests lead to errors
third_query = """
         SELECT errors.date, errors.error,
        (errors.error + requests.success) AS total
    FROM (SELECT DATE(time), count(*) AS error FROM log
    WHERE status != '200 OK'
    GROUP BY DATE(time)) AS errors,
    (SELECT DATE(time), count(*) AS success FROM log
    WHERE status = '200 OK'
    GROUP BY DATE(time)) AS requests
    WHERE errors.date = requests.date
    AND errors.error*100 > (errors.error + requests.success)
    ;
    """

third_query_result = ex_query(third_query)
print('3. On which days did more than 1% of requests lead to errors?')
for result in third_query_result:
    date = result[0].strftime('%B %d, %Y')
    percentage = 100*result[1]/result[2]
    print("\"" + date + "\"" + ' -- ' + str(percentage) + '% errors')
    print("\n")
