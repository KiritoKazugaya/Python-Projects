import qrcode as qr
#install package django 'qrcode'
#pip install qrcode[pil] install this
type= input("Enter the type of url you want to convert to QR : ")
url= input("Enter the url to be converted to QR code : ")
img=qr.make(url)
img.save(type+".png")


