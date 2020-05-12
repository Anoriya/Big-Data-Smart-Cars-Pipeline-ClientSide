from Aw.aw_producer import AwProducer
from Zephyr.zephy_producer_br_rr import ZephyrProducerBR
from Zephyr.zephy_producer_general import ZephyrProducerGeneral
from Zephyr.zephyr_producer_ecg import ZephyProducerECG
from Zephyr.zephyr_producer_event_data import ZephyrProducerEventData
from camera_producer import CameraProducer

#camera = CameraProducer()
#camera.start_streaming()

awProducer = AwProducer()
zephyrProducerBr = ZephyrProducerBR()
zephyrProducerGeneral = ZephyrProducerGeneral()
zephyrProducerECG = ZephyProducerECG()
zephyrProducerEventData = ZephyrProducerEventData()

awProducer.start()
zephyrProducerBr.start()
zephyrProducerGeneral.start()
zephyrProducerECG.start()
zephyrProducerEventData.start()

