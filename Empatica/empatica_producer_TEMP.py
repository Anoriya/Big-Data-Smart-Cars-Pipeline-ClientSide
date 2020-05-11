import csv
from time import sleep
#from kafka import KafkaProducer
from kafka import KafkaProducer


class EmpaticaProducerTEMP:

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def start_streaming(self):
        with open("/home/rached/Bureau/data/5-mcluet/EMPATICA/TEMP.csv",
                  newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                string = ';'.join(row) + "\n"
                self.producer.send('test', value=string.encode())
                print("sent")
                # sleep(1)
