import csv
import threading
from time import sleep

from kafka import KafkaProducer


class AwProducer(threading.Thread):

    def __init__(self):
        super(AwProducer, self).__init__()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/rached/Bureau/5-mcluet/AW/test 2020-02-07 13-23-32.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('Aw', value=string.encode())
                print("sent")
                sleep(0.1)

    def run(self):
        self.start_streaming()