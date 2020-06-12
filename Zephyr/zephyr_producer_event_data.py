import csv
import threading
from time import sleep

from kafka import KafkaProducer


class ZephyrProducerEventData(threading.Thread):

    def __init__(self):
        super(ZephyrProducerEventData, self).__init__()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/ZEPHYR/2020_02_07__13_18_12_Event_Data.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('Zephyr', value=string.encode(), key="Event_Data".encode(),partition=3)
                print("sent Event_Data")
                sleep(3)

    def run(self):
        self.start_streaming()