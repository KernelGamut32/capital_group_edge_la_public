# Running Unit Tests in Python

To run unit tests, in a terminal navigate to the root of your project (the folder where `app.py` lives). For example, navigate to `capstone/postgres-sample/solution`. When there, execute `python -m unittest` to run your unit tests.

To check your test coverage, in the terminal (from the same folder), run `coverage run -m unittest`. To view the results, you can either run `coverage report` (for a view in the terminal) or `coverage html` to generate an HTML view of your coverage percentages. See https://pypi.org/project/coverage/ for information on the coverage tool and installation (if needed).

To view the coverage HTML, expand the generated `htmlcov` folder. In Visual Studio Code, find `index.html`, right-click, and choose `Reveal in Explorer`. This should open the HTML file in file view. Double-click `index.html` to launch in a browser. You can click individual lines to drill in and see coverage details by file.

# Cloud Deploy

## Dockerize Your API

Create a Dockerfile similar to:

```
FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8250"]
```

Create an account at https://hub.docker.com using your "burner" gmail account (or create a new one if required). Run `docker login` - enter Docker Hub handle and password.

Run `docker build -t <docker hub handle>/<unique-image-name>:<version> .` from root folder to create a new Docker image. Run `docker image push <docker hub handle>/<unique-image-name>:<version>` to push the image to Docker Hub.

Use `docker run --name orders_app_cont_ars -p <your port>:<your port> -e PGHOST=<host name - container IP> -e PGDATABASE=<database name> -e PGUSER=<user name> -e PGPASSWORD=<your password here> -d <docker hub handle>/<unique-image-name>:<version>` to test your image locally.

## Setting Up EC2 Instance with Connection to PostgreSQL RDS Database

Follow this tutorial to create an initial EC2 instance and connected RDS database:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TUT_WebAppWithRDS.html

Once those steps are complete, connect to the EC2 instance by:

- Clicking the link for your instance and clicking the `Connect` button, or
- Clicking the checkbox next to your instance and clicking the `Connect` button

Follow the provided instructions in the AWS Management Console for changing permissions on the key pair file you created and downloaded, and connect via SSH to the EC2 instance.

Once connected to your EC2 instance, run `sudo yum update -y` to update the EC2 OS. Assuming you’ve used Amazon Linux (as outlined in the tutorial above), run `sudo amazon-linux-extras install postgresql13` to install the PostgreSQL client tools.

Upon completion, you should be able to connect to your PostgreSQL instance using `psql -U postgres -h <RDS endpoint>`. You’ll be prompted for the `postgres` user password you setup when creating the RDS instance.
Use https://github.com/KernelGamut32/capital_group_edge_la_public/blob/main/capstone/data-def.sql (or your own SQL scripts to create your capstone database in RDS).

## Deploying a FastAPI Application to AWS EC2

### Follow this tutorial for deploying and executing your Python code on EC2:

https://towardsdatascience.com/how-to-run-your-python-scripts-in-amazon-ec2-instances-demo-8e56e76a6d24

### Follow the next set of steps for deploying your API as a Docker container on EC2:

Pre-requisites:

- Install Docker on Amazon Linux using https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/
- Install nginx on Amazon Linux by running `sudo amazon-linux-extras install nginx1`
- Install git on Amazon Linux by running `sudo yum install git`

Follow this tutorial to create a Dockerized instance of your FastAPI app. Execute the steps outlined in pre-reqs above to install Docker, nginx, and git on Amazon Linux, then pick up with step 4 in the following link:

https://dev.to/theinfosecguy/how-to-deploy-a-fastapi-application-using-docker-on-aws-4m61

For the nginx configuration instructions defined in the link above, instead of creating a separate configuration for your API, modify /etc/nginx/nginx.conf instead. Replace the existing `server` configuration with what's suggested in the article:

```
server {
    listen 80;
    server_name <PUBLIC_IP>;
    location / {
        proxy_pass http://127.0.0.1:<your port>;
    }
}
```

Use `docker run --name orders_app_cont_ars -p <your port>:<your port> -e PGHOST=<RDS endpoint> -e PGDATABASE=<database name> -e PGUSER=<user name> -e PGPASSWORD=<your password here> -d <docker hub handle>/<unique-image-name>:<version>` to run the API on the EC2 instance. Test using http://<PUBLIC_IC>/docs.
