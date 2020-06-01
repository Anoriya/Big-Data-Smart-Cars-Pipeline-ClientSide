import csv
import threading
from time import sleep

from kafka import KafkaProducer


class GazMassConcentration(threading.Thread):

    def __init__(self):
        super(GazMassConcentration, self).__init__()
        # self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/AIRQUALITY/2020-02-07_13-26-04-SPS3x_ECAC46730C998045.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                print(string)
                self.producer.send('AirQuality', value=string.encode(), key="concentration".encode(), partition=1)
                print("sent Gaz mass concentration")
                sleep(1)

    def run(self):
        self.start_streaming()