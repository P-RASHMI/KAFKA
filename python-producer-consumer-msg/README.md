Hadoop version is :3.3.1 
python version is(python3 --version) :3.8.10
kafka : kafka-topics.sh --version 
2-13 2.8.0 
1)TO INSTALL KAFKA-PYTHON : To execute code in python for kafka 

In terminal : ~$ pip install kafka-python

EXECUTE MESSAGE SENDING USING PYTHON :

To create consumer.py file and producer.py file and to send msgs from producer to consumer using single node 
single broker kafka using PYTHON code:

Go to kafka and start zookeeper server and kafka server using following commands in different terminals :
~/Downloads/kafka_2.13-2.8.0
$ bin/zookeeper-server-start.sh config/zookeeper.properties

$ bin/kafka-server-start.sh  config/server.properties
Now in the separate terminal create topic 

$bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic python-kafka
Start the consumer.sh files in separate terminal:

#$ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic python-kafka

$ bin/kafka-console-consumer.sh  --bootstrap-server localhost:9092 --topic python-kafka --from-beginning

In vs code create a producer.py file,consumer.py file 
Now run the producer.py file you will see the messages gets executed in terminal of consumer

