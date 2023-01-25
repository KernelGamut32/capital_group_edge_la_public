# Cloud Deploy

## Setting Up EC2 Instance with Connection to PostgreSQL RDS Database

Follow this tutorial to create an initial EC2 instance and connected RDS database:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TUT_WebAppWithRDS.html

Once those steps are complete, connect to the EC2 instance by:

- Clicking the link for your instance and clicking the `Connect` button, or
- Clicking the checkbox next to your instance and clicking the `Connect` button

Follow the provided instructions in the AWS Management Console for changing permissions on the key pair file you created and downloaded, and connect via SSH to the EC2 instance.

Once connected to your EC2 instance, run `sudo yum update -y` to update the EC2 OS. Assuming you’ve used Amazon Linux (as outlined in the tutorial above), run `sudo amazon-linux-extras install posgresql13` to install the PostgreSQL client tools.

Upon completion, you should be able to connect to your PostgreSQL instance using `psql -U postgres -h <RDS endpoint>`. You’ll be prompted for the `postgres` user password you setup when creating the RDS instance.
Use https://github.com/KernelGamut32/capital_group_edge_la_public/blob/main/capstone/data-def.sql (or your own SQL scripts to create your capstone database in RDS).

## Deploying a FastAPI Application to AWS EC2

Follow this tutorial for deploying and executing your Python code on EC2:

https://towardsdatascience.com/how-to-run-your-python-scripts-in-amazon-ec2-instances-demo-8e56e76a6d24

Follow this tutorial to create a Dockerized instance of your FastAPI app (use `sudo yum` instead of `sudo apt-get` if running Amazon Linux on EC2):

https://dev.to/theinfosecguy/how-to-deploy-a-fastapi-application-using-docker-on-aws-4m61
