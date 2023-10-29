# **Load Testing using Locust**

## Installing Locust
pip install locust

## To run a locust file
#locust -f tests/locust/locustpost.py --headless -u 10 -r 10 -t 5s --html postreport.html --host http://localhost:8000 
where -u = maximum no. of consecutive users making requests,
      -r = no.of users per second
      -t = time of the test
      -html = report filename
      --host = hosting url

## Locustfile.py
It includes basic code for analysing the load test for create,update and get operations of API

## Locust_doc.pdf file
This file  has screenshots from a sample report file that is generating while performing locust test