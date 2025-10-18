'''import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10, border=5,)
qr.add_data("https://g.co/kgs/1ZaVC6L")

qr.make(fit=True)
img=qr.make_image(fill_color="blue", back_color="White")
img.save("ZMreview.png")



#simple
import qrcode as qr
img= qr.make("https://g.co/kgs/DGV3Bmj")
img.save("OnEdgeSalon.png")
'''
import qrcode as qr
img= qr.make("https://www.google.com/maps/place/Heaven+Drops/@34.528668,74.2137304,17z/data=!4m8!3m7!1s0x38e0e1bd103385e7:0x69b88c6555aa4d05!8m2!3d34.528668!4d74.2137304!9m1!1b1!16s%2Fg%2F11xgjm9y11?entry=ttu&g_ep=EgoyMDI1MDUyOC4wIKXMDSoASAFQAw%3D%3D")
img.save("Heaven drops.png")