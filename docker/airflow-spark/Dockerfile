FROM puckel/docker-airflow:1.10.9

# set variables
ENV SPARK_VERSION 2.4.5
ENV HADOOP_VERSION=2.7
ENV SPARK_HOME /usr/local/apps/spark
ENV JAVA_HOME /usr
ENV PATH $PATH:$JAVA_HOME/bin:$SPARK_HOME/bin


# install Java
USER root
RUN echo "deb http://security.debian.org/debian-security stretch/updates main" >> /etc/apt/sources.list                                                   
RUN mkdir -p /usr/share/man/man1/ && \
    apt-get update -y && \
    apt-get install -y openjdk-8-jdk

RUN apt-get install unzip -y && \
    apt-get autoremove -y

# install Spark	
RUN mkdir -p /usr/local/apps && \
    cd /usr/local/apps/ && \
	curl -o spark.tgz https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xvzf spark.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark && \
    rm spark.tgz
	
USER airflow
