#!C:/Users/HP/AppData/Local/Programs/Python/Python35/python.exe
print("Content-type: text/html\r\n\r\n") 
print("<html><head><link rel='stylesheet' type='text/css' href='css/style.css'></head><body>") 
# main container div start
print("<div class='container'>") 
# header section start
print("<div class='header-section'>") 


# navigation menu start 
print("<div class='nav-section'>") 

#navi start
print("<ul class='nav'>") 
print("<li><a href='iindex.py'>Home</a></li>")
print("<li><a href='about.py'>About</a></li>")
print("<li><a href='gallery.py'>Gallery</a></li>")
print("<li><a href='Product.py'>product</a></li>")
print("<li><a href='Contact.py'>contact</a></li>")
print("</ul>") 

#navi end
print("</div>") 
# navigation menu end 

# slider section start
print("<div class='slider-sec'>") 
print("<img src='images/i1.jpg' width='100%' height='100%'>")
print("</div>") 
# slider section end


print("</div>") 
# header section end


# content area start
print("<div class='main-cnt'>") 

# content row 1 start
print("<div class='cnt-row1'>") 
#left section start
print("<div class='cnt-row1-left'>") 
print("<h3 align='center'>WELCOME TO I WORLD </h3>")
print("<p class='cnt-row1-para'>'''Apple's latest mobile launch is the iPhone 12 Pro. The smartphone was launched in 13th October 2020. The phone comes with a 6.10-inch touchscreen display with a resolution of 1170 pixels by 2532 pixels at a PPI of 460 pixels per inch. The phone packs 64GB of internal storage cannot be expanded.The iPhone 12 Pro is a dual SIM (GSM and GSM) smartphone that accepts Nano-SIM and eSIM. Connectivity options include Wi-Fi, Wi-Fi standards supported, GPS, Bluetooth, NFC, Lightning, 3G and 4G (with support for Band 40 used by some LTE networks in India). Sensors on the phone include Face unlock, 3D face recognition, Compass Magnetometer, Proximity sensor, Accelerometer, Ambient light sensor, Gyroscope and Barometer.'''</p>")
print("</div>") 
#left section end

#right section start

print("<div class='cnt-row1-right'>") 
print("<img src='images/i2.png' width='100%' height='100%'>")
print("</div>") 
#right section end

print("</div>") 
# content row 1 end

# content row 2 end
print("<div class='cnt-row2'>")
print("<img src='images/i3.jpg' width='100%'>")
print("</div>") 
# content row 2 end

#footer start
print("<div class='footer-section'>")
print("<p class='footer-para'>© 2020  |.| All Rights RESERVED |.| DESIGN BY I SMART </p>")
print("</div>") 
#footer end

print("</div>") 
# content area end

print("</div>") 
# main container div end
print("</html></body>")


