import qrcode

qr = qrcode.make("https://www.facebook.com/profile.php?id=100026610558078")

qr.save("my_facebook.jpg")