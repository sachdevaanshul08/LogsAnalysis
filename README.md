# About The Project

This project demonstrate the internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, this code will answer questions about the site's user activity.

NOTE - The program written in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to following questions.

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

        Example:
        "Princess Shellfish Marries Prince Handsome" — 1201 views
        "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
        "Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

        Example:
        Ursula La Multa — 2304 views
        Rudolf von Treppenwitz — 1985 views
        Markoff Chaney — 1723 views
        Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to [this lesson][HTTPSTATUS] for more information about the idea of HTTP status codes.)

        Example:
        July 29, 2016 — 2.5% errors

## The virtual machine
This project makes use of the same Linux-based virtual machine (VM).

### Installing the Virtual Machine
You'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser.

We're using tools called [Vagrant][vagrant] and [VirtualBox][virtualbox] to install and manage the VM. You'll need to install these to execute this project. The instructions on this page will help you do this.

### Conceptual overview
[This video][conceptualoverview] offers a conceptual overview of virtual machines and Vagrant. You don't need to watch it to proceed, but you may find it informative.

### Use a terminal
You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from [git-scm.com][gitscm].

If you'd like to learn more about Git, take a look at our course about [Git][gitcourse].

### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here][vbdownload]. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is successfully installed, you will be able to run `vagrant --version`   in your terminal to see the version number.
If Vagrant is successfully installed, you will be able to run vagrant --version in your terminal to see the version number.


### Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this [file: FSND-Virtual-Machine.zip][fsnd] This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

Navigating to the FSND-Virtual-Machine directory and listing the files in it.
Navigating to the FSND-Virtual-Machine directory and listing the files in it.

## Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
Starting the Ubuntu Linux installation with `vagrant up`.

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!

Logging into the Linux VM with `vagrant ssh`.
Logged in!

If you are now looking at a shell prompt that starts with the word vagrant , congratulations — you've gotten logged into your Linux VM.

## Download the data
Next, [download the data here][newsdb] You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)

To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
Here's what this command does:

   ` psql — the PostgreSQL command line program`
    `-d news — connect to the database named news which has been set up for you`
    `-f newsdata.sql — run the SQL statements in the file newsdata.sql`

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Explore the data
Once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.

    \dt — display tables — lists the tables that are available in the database.
    \d table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:
| Table | Details |
| ------ | ------ |
|authors |The authors table includes information about the authors of articles.|
|articles|The articles table includes the articles themselves.|
 |log |The log table includes one entry for each time a user has accessed the site.|

As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.



### To execute the project in your virtual machine

1. Bring the virtual machine back online (with `vagrant up`), do so now. Then log into it with `vagrant ssh`.
2. Download this repository in your `vagrant` directory.
3. execute the `python3 newsdb.py`

You will see the following output on your terminal-

        Top Accessed Articles

        "candidate-is-jerk" — 338647 views
        "bears-love-berries" — 253801 views
        "bad-things-gone" — 170098 views

        Most Popular Authors

        Ursula La Multa — 507594 views
        Rudolf von Treppenwitz — 423457 views
        Anonymous Contributor — 170098 views

        On following days, more than 1% of requests lead to errors

        17 Jul 2016 - 2.26% errors

VOILA!!! You have succssefully executed the Logs Analysis.


[newsdb]: <https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip>
[HTTPSTATUS]:<https://classroom.udacity.com/courses/ud303/lessons/6ff26dd7-51d6-49b3-9f90-41377bff4564/concepts/75becdb9-da2a-4fbf-9a30-5f3ccd1aa1d6>
[vagrant]:<https://www.vagrantup.com/>
[virtualbox]:<https://www.virtualbox.org/wiki/Download_Old_Builds_5_1>
[conceptualoverview]:<https://www.youtube.com/watch?v=djnqoEO2rLc>
[gitscm]:<https://git-scm.com/downloads>
[gitcourse]:<https://www.udacity.com/course/ud123>
[vbdownload]:<https://www.virtualbox.org/wiki/Download_Old_Builds_5_1>
[fsnd]:<https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip>
