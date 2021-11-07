Hadoop version is :3.3.1
python version is(python3 --version) :3.8.10
kafka : kafka-topics.sh --version
2-13 2.8.0

STORE THE LIVE STOCK DATA FROM API TO HADOOP USING PYTHON :

Start the hadoop servers
~$ start-all.sh
~$ jps

Go to the kafka directory:start the zookeeper, kafka server:
~/Downloads/kafka_2.13-2.8.0
           $ bin/zookeeper-server-start.sh  config/zookeeper.properties
~/Downloads/kafka_2.13-2.8.0
           $ bin/kafka-server-start.sh config/server.properties
create the topic in kafka(python-kafka-stock) :
  $bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic python-kafka-stock
 
List the topics :
$ bin/kafka-topics.sh --list --zookeeper localhost:2181

#Use the producer file by going to kafka directory :
         # $ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic python-kafka-stock
 
In the other terminal consumer file by going to kafka directory :
            $ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic python-kafka-stock --from-beginning

Go to the vs code and create stock_data-producer.py ,stock_data-consumer.py and stock_data-hdfscmd.py file
 Create .env file consisting of API key and localhost

In the vs code execute the stock_data-producer.py file and then in the console of consumer.sh you can see the  output data of live stock data:
After that in vs code run the stock_data-hdfscmd.py the output data gets into stockdataconsole.txt file that is created and 
after that the data gets shifted to hadoop

Now go to the hadoop you will see the directory gets created and data shifted to the file :
localhost:9870 

