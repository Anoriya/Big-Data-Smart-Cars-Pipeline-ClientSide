import csv
from kafka import KafkaProducer


class AwProducer:

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/AW/test 2020-02-07 13-23-32.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('Aw', value=string.encode())
                print("sent")
                # sleep(1)