import csv
import threading
from time import sleep

from kafka import KafkaProducer


class GazQuantity(threading.Thread):

    def __init__(self):
        super(GazQuantity, self).__init__()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/AIRQUALITY/2020-02-07_13-26-04-SGP30_8373181.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('AirQuality', value=string.encode(), key="quantity".encode(), partition=0)
                print("sent Gaz Quantity")
                sleep(1)

    def run(self):
        self.start_streaming()
