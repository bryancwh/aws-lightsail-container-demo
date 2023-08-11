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
- [Conclusion](#Conclusion)

## Prerequisites
An Amazon Web Services (AWS) account

Basic knowledge of the Linux command line

## Step 1: Verify the application locally

Step 1. Go to your Flask application [todo.py](./todo.py)

Step 2. Ensure the local deployment is uncommented, and the lightsail deployment is commented out. 

![image](./media/images/local_code.png)

Step 3. Go to your [Dockerfile](./Dockerfile) and verify the build

Step 4. In your terminal, build the application, then run it to test that it is working.

```
docker build -t lightsail-todo-local .

docker run -it --rm -p 8080:8080 lightsail-todo-local
```

You should see the following

![image](./media/images/app.png)


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

![image](./media/images/gid-rds-create-07.jpg)


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

Step 1. Go to the Lightsail console home page and click Account in the top right corner. Choose Account from the pop out menu.

![image](./media/images/account_menu.png)

Step 2. Click on Advanced from the horizontal menu

Step 3. Under VPC peering ensure the Enable VPC peering box is checked for the region where your application is deployed.

![image](./media/images/vpc_peering.png)

### 3.2 Edit RDS Security Group
The next step is to edit the security group for the RDS instance to allow traffic from the Lightsail subnet

Step 1. Return to the RDS console

Step 2. Under Resources click on DB Instances

Step 3. Click on the name of the database you created at the beginning of the workshop

Step 4. Under Connectivity and security click on the security group name

![image](./media/images/rds_sg.png)

Step 5. Click the Inbound tab near the bottom of the screen and click the Edit button

![image](./media/images/sg_edit.png)

Step 6. Click Add rule in the pop up box

Step 7. From the Type drop down choose MySQL/Aurora

Step 8. In the source box enter 172.26.0.0/16 (this is the CIDR address for the Lightsail subnet)

![image](./media/images/sg_values.png)

Step 9. Click Save

### 3.3 Use the RDS Endpoint in Flask application

Step 1. Return to the RDS console entry for your RDS database

Step 2. Under Connectivity and security copy the Endpoint value

![image](./media/images/rds_endpoint.png)

Step 3. Go to you Flask application [todo.py](./todo.py)

Step 4. Change the SQLAlchemy Database URI to use the RDS DB Endpoint

![image](./media/images/todo_code.png)

## Step 4: Deploy Container to Lightsail

### 4.1 Build and deploy the container to Docker Hub

Step 1. Build the container 

```
docker buildx build --platform linux/amd64 -t lightsail-todo .
```

Step 2. Push the container to Docker Hub

```
docker tag lightsail-todo bryancwh/lightsail-todo
docker login
docker push bryancwh/lightsail-todo
```

Step 3. Go to Docker Hub and verify that your docker has been pushed

![image](./media/images/docker.png)

### 4.2 Create a Lightsail container service 

Now that you have a container ready on Docker Hub, let’s create a Lightsail Container Service.

Step 1. Go to Lightsail console and click Create container service

![image](./media/images/lightsail.png)

Step 2. Select the size of the container you want to use in terms of vCPU and memory available to my application Select the number of container instances you want to run in parallel for high availability or scalability reasons. 

![image](./media/images/container_capacity.png)

> **_NOTE:_** You can change the number of container instances or their power (vCPU and RAM) at any time, without interrupting the service. 

Step 3. Click on **Set up deployment** and specify a customer deployment. Choose name for your image and give the address of the image on Docker Hub. 

![image](./media/images/set_up_deployment.png)

Step 4. Specify a name for your container service 

![image](./media/images/identify_service.png)

### 4.3 Verify the application

After a while, your deployment is active and you can test the endpoint

![image](./media/images/active.png)

The endpoint DNS address is available on the top-right side of the console. Click it.

![image](./media/images/endpoint.png)

You should get the following:

![image](./media/images/app.png)

## Conclusion
Congratulations! You have successfully set up a To Do application using the Amazon Lightsail Container service. You now have a functional environment for hosting websites and applications that require a web server, database, and server-side scripting.