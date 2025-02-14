import qrcode
from PIL import Image
from qrcode.console_scripts import error_correction

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,
                 border=4)
type= input("Enter the File name of url you want to convert to QR : ")
url= input("Enter the url to be converted to QR code : ")
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill_color="gold",
                  back_color="silver")
img.save(type+".png")
