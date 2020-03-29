from base.driver import driver

spark_driver = driver(app_name='000_hello_world')
spark_session = spark_driver.spark_start()

def load_show():
    df = spark_session.read.csv(path="/src/data/hello_world/FL_insurance_sample.csv", inferSchema=True, sep=",")
    df.show(20)

load_show()