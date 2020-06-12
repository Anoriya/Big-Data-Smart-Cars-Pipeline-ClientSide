from kafka import KafkaConsumer


consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id="Car")

consumer.subscribe(["result"])

for msg in consumer:
    print(msg, 'utf-8', 'ignore')
