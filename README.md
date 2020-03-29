# big-data-vagrant

**big-data-vagrant** is a vagrant environment based on:
[Ubuntu 18.04 Bionic Beaver](https://app.vagrantup.com/ubuntu/boxes/bionic64)

Vagrant file contains following dockerized apps:
1. [Spark Master Node](https://hub.docker.com/r/bde2020/spark-master/builds)
1. [Spark Worker Node](https://hub.docker.com/r/bde2020/spark-worker/builds)
1. [Airflow](https://hub.docker.com/repository/docker/kwdocker2020/airflow-spark)
1. [Microsoft SQL Server 2019](https://hub.docker.com/_/microsoft-mssql-server)
1. [Kafka (Fast-Data-Dev)](https://hub.docker.com/r/lensesio/fast-data-dev)

## Project structure

```|-- .gitignore
|-- bootstrap.sh
|-- README.md
|-- vagrantfile
|-- docker/
|   |-- docker-compose.yml
|   |-- airflow-spark/
|   |   |-- Dockerfile
|-- docs/
|   |-- spark_windows_setup.md
|-- files/
|   |-- airflow/
|   |   |-- dags/
|   |   |   |-- hello_world.py
|   |-- data/
|   |   |-- hello_world/
|   |   |   |-- FL_insurance_sample.csv
|   |-- spark/
|   |   |-- jobs/
|   |   |   |-- hello_world/
|   |   |   |   |-- 000_hello_world.py
|   |   |   |   |-- packages/
|   |   |   |   |   |-- packages.zip
```
## Prerequsites
1. [Get free Lenses license](https://lenses.io/downloads/lenses/)
1. Create *LENSES_LICENSE* environment variable and save your link as its value:   
```setx LENSES_LICNSE [put your link here]```

## Installation
1. Clone [big-data-vagrant repository](https://github.com/iamkamilwojcik/big-data-vagrant)
## Usage

1. Run Command Prompt and navigate to    
```cd big-data-vagrant```
1. Start your big-data-vagrant environment:    
``` vagrant up```
1. Establish SSH connection when it's finished:    
```vagrant ssh```
1. Check if all containers are up and running:  
```docker container ls```
1. If some of them is down, go to ```cd /src/docker``` and debug: ```docker-compose logs```


## How to login
**Ubuntu**:    
- login: *vagrant*     
- password: *vagrant*

**Spark**
- Spark Master UI link: ```http://127.0.0.1:10001/```
- Spark Worker UI link: ```http://127.0.0.1:10002/```

**Airflow**
- Airflow UI link: ```http://127.0.0.1:10005/```

**SQL Server**:    
- host: *127.0.0.1,10003* 
- login: *sa*    
- password: *VeryComplicatedPassword2020* 

**Lenses**
- Lenses UI link: ```http://127.0.0.1:10004/```
- login: *admin*
- password: *admin*


