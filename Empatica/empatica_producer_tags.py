import csv
import threading
from time import sleep
#from kafka import KafkaProducer
from kafka import KafkaProducer


class EmpaticaProducerTAGS(threading.Thread):

    def __init__(self):
        super(EmpaticaProducerTAGS, self).__init__()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/EMPATICA/tags.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('Empatica', value=string.encode(), key="TAGS".encode())
                print("sent TAGS")
                sleep(1)

    def run(self):
        self.start_streaming()