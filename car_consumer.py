import threading
from time import sleep

from PyQt5.QtCore import pyqtSignal, QObject
from kafka import KafkaConsumer


class CarConsumer(threading.Thread, QObject):
    msg_q = pyqtSignal(object)

    def __init__(self):
        super(CarConsumer, self).__init__()
        QObject.__init__(self)
        self.consumer = KafkaConsumer(
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id="CarX")

        self.consumer.subscribe(["result"])

    def consume(self):
        for msg in self.consumer:
            self.msg_q.emit(msg.value.decode("utf-8"))

    def run(self):
        self.consume()
