
from kafka import KafkaConsumer
import pydoop.hdfs as hdfs

consumer = KafkaConsumer('newTopic-stockdata')
hdfs_path = 'hdfs://localhost:9000/StockDatapydoop/stock_file.txt'

for message in consumer:
    values = message.value.decode('utf-8')
    with hdfs.open(hdfs_path, 'at') as f:
        f.write(f"{values}\n")
    
