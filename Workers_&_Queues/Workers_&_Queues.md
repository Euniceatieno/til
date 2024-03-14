# Queues and workers
* Job Queues and workers come in handy when we want to run some functionalities asynchronously or in the background
* A job is a function set to be executed at a particular time
* A job queue is a colections of jobs set to run sequentially at particular times.
* A worker on the other hand is a processor or server set to handle the processing of a job ,if you have 4 jobs  
the you need 4 workers to process these jobs.
* Jobs are usually efficient when one needs to run tasks that take a long time to execute

* Using Django Q to manage queues and jobs in django.
* To set up job queues, you will need a message broker, which is a system that translates the formal messaging protocol of the sender(Django) to the formal messaging protocol of the receiver (Django Q).  



Among many message brokers ,we have Redis RabbitMQ and many others  

For this learning class ,we are going to use Redis.
* What happens in the backround is that Redis gets the data about the funtions to be executed and relays it   
to the Queue for Django Q to receive.  

# Process Flow
Create an app on heroku and configure the heoku-redis add on
Make sure redis and Djngo Q are installed within your application.
Initializee settings for django Q in the settings.py file of your project

`
Q_CLUSTER = {
    'name': 'myproject',
    'workers': 4, # number of workers. It Defaults to number of CPU of your local machine.
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'redis': {
        'host': 'ec2-54-171-19-145.eu-west-1.compute.amazonaws.com', #Gotten from REDIS_URL
        'password': 'p78f7b20091d2710e27400dda07d097aff472f7d6a5947bd3232683d268fa4c0f',  #Gotten from REDIS_URL
        'port': 31449, #Gotten from REDIS_URL
        'db': 0, }
}
`
