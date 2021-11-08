Hadoop version is :3.3.1 
python version is(python3 --version) :3.8.10 
kafka : (kafka-topics.sh --version ) :2-13 2.8.0

STORE THE LIVE STOCK DATA FROM API TO HADOOP USING PYDOOP WITH PYTHON :

Install PYDOOP : in terminal (pydoop-2.0.0)
~$ pip3 install pydoop

Start the services of hadoop :
$start-all.sh
$jps

Go to the directory of kafka and start the zookeeper server:
~/Downloads/kafka_2.13-2.8.0
$ bin/zookeeper-server-start.sh config/zookeeper.properties

Go to another terminal and start kafka server inside kafka directory(~/Downloads/kafka_2.13-2.8.0):
$ bin/kafka-server-start.sh config/server.properties

Go to the vs code path of the producer and consumer in terminal :
Execute the consumer code of python:
(~/Desktop/Python_work/hadoop/KAFKA/pydoop-stockdata)
                         $ python3  stock_data-consumer.py

Go to the vs code and run the producer code(stock_data-producer.py)

Now, go to localhost://9870 
