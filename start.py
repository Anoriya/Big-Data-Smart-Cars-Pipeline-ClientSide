import threading

from AirQuality.GazMassConcentration import GazMassConcentration
from AirQuality.GazQuantity import GazQuantity
from Aw.aw_producer import AwProducer
from Empatica.empatica_producer_ACC import EmpaticaProducerACC
from Empatica.empatica_producer_BVP import EmpaticaProducerBVP
from Empatica.empatica_producer_EDA import EmpaticaProducerEDA
from Empatica.empatica_producer_HR import EmpaticaProducerHR
from Empatica.empatica_producer_IBI import EmpaticaProducerIBI
from Empatica.empatica_producer_TEMP import EmpaticaProducerTEMP
from Empatica.empatica_producer_tags import EmpaticaProducerTAGS
from Zephyr.zephy_producer_br_rr import ZephyrProducerBR
from Zephyr.zephy_producer_general import ZephyrProducerGeneral
from Zephyr.zephyr_producer_ecg import ZephyProducerECG
from Zephyr.zephyr_producer_event_data import ZephyrProducerEventData
from Camera.camera_producer import CameraProducer


class Start(threading.Thread):

    def __init__(self):
        super(Start, self).__init__()
        # Camera
        self.cameraProducer = CameraProducer()
        # Aw
        self.awProducer = AwProducer()
        # Zephyr
        self.zephyrProducerBr = ZephyrProducerBR()
        self.zephyrProducerGeneral = ZephyrProducerGeneral()
        self.zephyrProducerECG = ZephyProducerECG()
        self.zephyrProducerEventData = ZephyrProducerEventData()
        # Empatica
        self.empaticaProducerACC = EmpaticaProducerACC()
        self.empaticaProducerBVP = EmpaticaProducerBVP()
        self.empaticaProducerEDA = EmpaticaProducerEDA()
        self.empaticaProducerHR = EmpaticaProducerHR()
        self.empaticaProducerIBI = EmpaticaProducerIBI()
        self.empaticaProducerTAGS = EmpaticaProducerTAGS()
        self.empaticaProducerTEMP = EmpaticaProducerTEMP()
        # AirQuality
        self.gazQuantity = GazQuantity()
        self.gazMassConcentration = GazMassConcentration()

    def start_engine(self):
        self.awProducer.start()
        self.zephyrProducerBr.start()
        self.zephyrProducerGeneral.start()
        self.zephyrProducerECG.start()
        self.zephyrProducerEventData.start()
        self.cameraProducer.start()
        self.empaticaProducerACC.start()
        self.empaticaProducerBVP.start()
        self.empaticaProducerEDA.start()
        self.empaticaProducerHR.start()
        self.empaticaProducerIBI.start()
        self.empaticaProducerTEMP.start()
        # empaticaProducerTAGS.start()
        # Airquality
        self.gazQuantity.start()
        self.gazMassConcentration.start()

    def run(self):
        self.start_engine()
