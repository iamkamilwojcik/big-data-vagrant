# Apache Spark 2.4.5

This document describes installation of Apache Spark 2.4.5 on Windows 10 Professional.

# Steps

1. Install [JDK](http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-windows-x64.exe) to a path that does not have a space in it (```C:\java\jdk```.
JDK installer will ask you to install JRE as well. It should be installed to ```C:\java\jdk```.  
1. Download [Apache Spark](https://www.apache.org/dyn/closer.lua/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz) 
1. Extract files from:  
```YOUR_PATH\spark-2.4.5-bin-hadoop2.7.tgz\spark-2.4.5-bin-hadoop2.7.tar\spark-2.4.5-bin-hadoop2.7``` to:    ```C:\spark```:
1. Go to ```C:\spark\conf``` and rename ```log4j.properties.template``` to ```log4j.properties```
1. Edit ```log4j.properties``` and replace: ```log4j.rootCategory=INFO, console``` to ```log4j.rootCategory=ERROR, console```
1. Create following path: ```C:\winutils\bin``` and paste winutils.exe
1. Install [Microsoft Visual C++ 2010 SP1 Redistributable Package (x64)
](http://www.microsoft.com/en-us/download/details.aspx?id=13523)
1. Install [Microsoft Visual C++ 2015 Redistributable Update 3 RC
](https://www.microsoft.com/en-us/download/details.aspx?id=52685)
1. Create following path: ```C:\tmp\hive```
1. Run CMD with admin previliges and execute following commands: ```cd c:\winutils\bin winutils.exe chmod 777 c:\tmp\hive```
1. Run CMD ***without*** admin previliges and create following environment variables:   
```setx SPARK_HOME C:\spark```   
```setx JAVA_HOME C:\java\jdk```   
```setx HADOOP_HOME C:\winutils```
1. Update paths environment variable:    
```setx path "%PATH%;%SPARK_HOME%\bin;%JAVA_HOME%\bin"```
