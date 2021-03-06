### Create application image 
`docker-compose build`
### Create database
`docker-compose run web python3 manage.py migrate`
### Start application  
`docker-compose up -d`

### Setup daily upvote count reset
Copy `reset_upvotes.sh` to `/etc/cron.daily`

Run `chmod +x /etc/cron.daily/reset_upvotes.sh`

(developstodaytest_web is a name of running container with API application, change when needed)

Test application in browser http://127.0.0.1:8000/api/


### Optional. Load test data
`docker-compose run web python3 manage.py loaddata dumpdata.json`

