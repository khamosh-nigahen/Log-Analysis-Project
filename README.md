# Log-Analysis-Reporting-Tool

## Project Overview

This is the third project for the Udacity Full Stack Nanodegree. In this project, a PostgreSQL database is explored by complex SQL queries to get conclusions. Its a reporting tool for a newpaper site to discover what kind of articles the site's readers like and prints out reports (in plain text) based on the data in the database.

## PreRequisites:

1. [Python3](https://www.python.org/)
2. Download and install VM using [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
3. Download and install [Vagrant](https://www.vagrantup.com/downloads.html) for the VM settings

## Setup VM:
1. Run in the working folder `vagrant up` to configure the VM
2. Run `vagrant ssh` to log into the VM
3. Download the [news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and save it in the working VM folder

## Setup Database and Create Views:
1. Run `psql -d news -f newsdata.sql` to generate the database
2. Use `psql -d news` to connect to database.
 
### Create Views:
#### create view view_article using code below:
```
CREATE VIEW view_article AS SELECT title,
       author,
       count(title) AS views
FROM articles,
     log
WHERE log.path LIKE concat('%',articles.slug)
GROUP BY articles.title,
         articles.author
ORDER BY views DESC;
```

##### create view view_author using code below:
```
CREATE VIEW view_author AS SELECT name,
       sum(view_article.views) AS total
FROM view_article,
     authors
WHERE authors.id=view_article.author
GROUP BY authors.name
ORDER BY total DESC;
```

##### create view view_error_log using code below:
```
CREATE VIEW view_error_log AS SELECT date(time),
        round(100.0*sum(case log.status when '200 OK'
        then 0 else 1 end)/count(log.status),2)
        AS percent_error
        FROM log
        GROUP BY date(time)
        ORDER BY percent_error desc;
```

## Execute:
Run `python3 reporting_tool.py` in terminal to generate the database report and check `log_analysis.txt` file.

## License:
The content of this repository is licensed under a [MIT LICENSE](https://choosealicense.com/licenses/mit/#)

