import csv
import threading
from time import sleep
#from kafka import KafkaProducer
from kafka import KafkaProducer


class EmpaticaProducerACC(threading.Thread):

    def __init__(self):
        super(EmpaticaProducerACC, self).__init__()
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/sartharion/Bureau/5-mcluet/EMPATICA/ACC.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('Empatica', value=string.encode(), key="ACC".encode(),partition=0)
                print("sent ACC")
                sleep(1)

    def run(self):
        self.start_streaming()