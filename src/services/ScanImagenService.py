
from src.utils.Logger import Logger

class ScanImageService():
    
    @classmethod
    def scanImage(cls, image):
        Logger.add_to_log("info", "Se escanea la imagen")
        try:
            # logic to scan an image
            pass
        except Exception as ex:
            print(ex)