sleep 20
docker exec -i airflow airflow connections -d --conn_id spark-local
docker exec -i airflow airflow connections -a --conn_id spark-local --conn_host spark://spark-master --conn_port 7077 --conn_type spark