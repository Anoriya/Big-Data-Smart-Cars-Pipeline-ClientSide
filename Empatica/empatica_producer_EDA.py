import csv
import threading
from time import sleep
#from kafka import KafkaProducer
from kafka import KafkaProducer


class EmpaticaProducerEDA(threading.Thread):

    def __init__(self):
        super(EmpaticaProducerEDA, self).__init__()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/EMPATICA/EDA.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('Empatica', value=string.encode(), key="EDA".encode(),partition=2)
                print("sent EDA")
                sleep(1)

    def run(self):
        self.start_streaming()