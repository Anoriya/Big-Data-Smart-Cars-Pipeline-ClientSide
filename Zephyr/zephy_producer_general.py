import csv
from kafka import KafkaProducer


class ZephyrProducerGeneral:

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/ZEPHYR/2020_02_07__13_18_12_General.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('Zephyr', value=string.encode(), key="General".encode())
                print("sent")
                # sleep(1)