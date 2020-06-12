import csv
import threading
from time import sleep

from kafka import KafkaProducer


class ZephyrProducerGeneral(threading.Thread):

    def __init__(self):
        super(ZephyrProducerGeneral, self).__init__()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/ZEPHYR/2020_02_07__13_18_12_General.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('Zephyr', value=string.encode(), key="General".encode(),partition=1)
                print("sent General")
                sleep(5)

    def run(self):
        self.start_streaming()