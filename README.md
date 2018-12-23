
---
# Logs Analysis
A Udacity FSND project.
___

## INTODUCTION:
This is the solution for the Logs Analysis project in Udacity Full Stack Nanodegree course. In this, we have to execute complex queries on a large database.

The program I wrote in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

---
#### Requests For This log_analysis_project:
** install: **
* [vagrant](https://www.vagrantup.com/downloads.html).
* [virtual Machine](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
* download a FSND virtual Machine.
* 'newsdata.sql' It can be downloaded from the Udacity course page.
  * The "newsdata.sql" has three different tables:
    *  ** authors: ** table includes information about the authors of articles.
    * ** Articles: ** table includes the articles themselves.
    * ** Log: ** table includes one entry for each time a user has accessed the site.
---
**From terminal:**

* you need to install the package from the terminal
`pip3 install psycopg2`

* To test python code quality install: `pip3 install pycodestyle`

   * Then use:
`pycodestyle log.py`

---
** After get the above software installed, follow the following instructions:**
* cd vagrant
* vagrant up
* vagrant ssh
* cd /vagrant
* cd log_analysis_project

## Running
Laod the data from the "newsdata.sql" by using the following command:
</br>`psql -d news -f news data.sql`

** To Run the script:**
</br>`python log.py`
