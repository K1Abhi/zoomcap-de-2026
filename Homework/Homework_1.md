#### Question 1. What's the version of pip in the python:3.13 image?

```shell
> docker run -it --entrypoint=bash python:3.13

root@97bc649207fe:/# pip -V
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```
- Solution is : **pip 25.3**
---
#### Question 2. Given the docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?
<img width="391" height="577" alt="image" src="https://github.com/user-attachments/assets/ba6930c3-07f0-4704-bad7-cf872066abac" />     
- Solution is : `postgres:5432`
---
