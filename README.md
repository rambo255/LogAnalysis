# LogAnalysis

Log Analysis Project

## Project Overview
>In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## Steps To Run

#### Prerequisites:

  * [Python3](https://www.python.org/)
  
  * [Vagrant](https://www.vagrantup.com/)
  
  * [VirtualBox](https://www.virtualbox.org/)
  
#### Virtual Environment Setup:
  
  * Install Vagrant and VirtualBox
  
  * Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  
  * Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  
  * Unzip this file after downloading it. The file inside is called newsdata.sql.
  
  * Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/rambo255/LogAnalysis)
  
  * Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  ```
    $ vagrant up
  ```
  
  * Then Log into this using command:
  ```
    $ vargrant ssh
  ```
  
  * Change directory to /vagrant and look around with ls and cd.
  
  * Load the data in local database using the command:
  ```
    > psql -d news -f newsdata.sql
  ```
  
  * Use `psql -d news` to connect to database.
  
  Once connected to DB, create the following views with the given query queries:

## Run the Analysis
 *  RUN `python log_analysis.py`
 
 ## Result of Analysis
 *   Result is in the 'output.txt' file.

