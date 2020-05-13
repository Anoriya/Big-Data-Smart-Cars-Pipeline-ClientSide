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
from camera_producer import CameraProducer

cameraProducer = CameraProducer()
awProducer = AwProducer()
zephyrProducerBr = ZephyrProducerBR()
zephyrProducerGeneral = ZephyrProducerGeneral()
zephyrProducerECG = ZephyProducerECG()
zephyrProducerEventData = ZephyrProducerEventData()
empaticaProducerACC = EmpaticaProducerACC()
empaticaProducerBVP = EmpaticaProducerBVP()
empaticaProducerEDA = EmpaticaProducerEDA()
empaticaProducerHR = EmpaticaProducerHR()
empaticaProducerIBI = EmpaticaProducerIBI()
empaticaProducerTAGS = EmpaticaProducerTAGS()
empaticaProducerTEMP = EmpaticaProducerTEMP()

awProducer.start()
zephyrProducerBr.start()
zephyrProducerGeneral.start()
zephyrProducerECG.start()
zephyrProducerEventData.start()
empaticaProducerACC.start()
empaticaProducerBVP.start()
empaticaProducerEDA.start()
empaticaProducerHR.start()
empaticaProducerIBI.start()
empaticaProducerTAGS.start()
empaticaProducerTEMP.start()
cameraProducer.start()

