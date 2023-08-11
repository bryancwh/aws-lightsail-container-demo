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