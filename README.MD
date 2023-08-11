# Lightsail Workshop
Welcome to the Lightsail Workshop! This guide will walk you through the process of setting up a To Do application stack on a Container using Amazon Lightsail.

Specifically, this workshop will cover:
- Creating the infrastructure you will use in the subsequent labs
- Deploying a two-tier To Do stack application in a Lightsail container
- Rearchitecting the application by separating the front-end from the database

## Table of Contents
- [Prerequisites](#prerequisites)
- [Step 1: Verify the application locally](#step-2-connect-to-your-instance)
- [Step 2: Deploy the RDS DB](#step-1-launch-an-instance)
- [Step 3: Attach RDS DB to your Flask application](#step-3-update-and-install-packages)
- [Step 4: Deploy application to Lightsail](#step-3-update-and-install-packages)
- [Cleanup](#Cleanup)

## Prerequisites
An Amazon Web Services (AWS) account

Basic knowledge of the Linux command line

## Step 1: Verify the application locally

## Step 2: Deploy the RDS DB

In this section we’ll deploy a RDS database. Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

Step 1. Sign into the AWS Management Console and open the Amazon RDS console 

Step 2. Click on Create Database

![image](./media/images/gid-rds-create-01.png)

Step 3. For Choose a database creation method, select Standard option. With Standard Create, you setup the configurations for your database.

Step 4. Select MySQL in Engine Options

Step 5. When you select MySQL as your database engine, the latest version will be automatically selected for you. For this lab, select MySQL version X.X.X.

Step 6. For Template, there are three options available: Production, Dev/Test and Free Tier. For the lab purpose, we will select Free Tier

Step 7. In Settings section, fill in the following for each field

![image](./media/images/gid-rds-create-04.png)

Step 8. In DB Instance size section, for DB instance class, select burstable classes-db.t2.micro. This option will be automatically selected for you.

Step 9. In the Storage section, select the Storage Type as General Purpose SSD. You can select or deselect the option for Auto Scaling for the lab purposes

Step 10. Since we selected the Template option as Free Tier-used only for doing hands-on or testing the applications, Multi-AZ deployment is not required and hence, the Availability and Durability section will be disabled for you.

Step 11. In the Connectivity section:

![imgage](./media/images/gid-rds-create-07.jpg)


Step 12. For Database authentication, there are two options to select from. Password Authentication will authenticate the user only with the database password. With Password and IAM Database authentication, the user will be authenticated with the database password and also with the user credentials through IAM roles and policies. For this lab, we will select: Password Authentication.

Step 13. Expand on Additional Configuration. For the Database options, provide the following:
- Initial Database name: lightsaildb
- DB Parameter group and Option group: default.mysqlx.x

Step 14. For Backup:
- Check on enable automatic backups.
- Provide Backup retention period as 7 days.
- Backup Window: No preference
- Leave rest as defaults

Step 15. Review your settings and click Create database.

Step 16. In the RDS Dashboard, monitor your new DB instance until the status changes from “creating” to “backing up” to “available”.

For more information refer to the [original workshop guide](https://catalog.us-east-1.prod.workshops.aws/workshops/f3a3e2bd-e1d5-49de-b8e6-dac361842e76/en-US/basic-modules/50-rds/rds-mysql/2-rds)

## Step 3: Attach RDS DB to your Flask application

### 3.1 Enable VPC peering
In order for Lightsail resources to communicate with other AWS resources, you need to enable VPC peering between Lightsail and the default AWS VPC for the same region as your Lightsail resources. Note that Lightsail can only peer with the default AWS VPC.

### 3.2 Edit RDS Security Group

### 3.3 Use the RDS Endpoint in Flask application

## Step 4: Deploy Container to Lightsail

### 4.4 Verify the application
Now you’ll verify that the application installed correctly and is correctly communicating with the RDS MySQL database.

The diagram below lays out the current architecture of the application.

## Cleanup
Congratulations! You have successfully set up a LAMP stack on your Amazon Lightsail instance. You now have a functional environment for hosting websites and applications that require a web server, database, and server-side scripting.