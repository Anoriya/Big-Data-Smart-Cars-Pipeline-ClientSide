from datetime import datetime

from kafka import KafkaConsumer, TopicPartition


def on_assign(c, ps):
    for p in ps:
        p.offset = -2
    c.assign(ps)


consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id="grp")

consumer.subscribe(["camera"])

for msg in consumer:
    print(msg, 'utf-8', 'ignore')
