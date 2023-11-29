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
print("<img src='images/iii1.jpg' width='100%' height='100%'>")
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
print("<img src='images/i2.png' width='100%' height='100%'>")
print("</div>") 
#left section end

#right section start
print("<div class='cnt-row1-right'>") 
print("<h3 align='center'>WELCOME TO I STORE</h3>")
print("<p class='cnt-row1-para'>'''iStore offers the best possible Apple experience through expert advice and a wide range of exclusive services that ensure you get the most out of your Apple products for your personal, business and education purchases and upgrades. Purchase your Apple product on selected FNB credit cards......Products iPhone, iPod, iPad, iMac, MacBook, Macbook Air, MacBook Pro, Mac mini Mac Pro, iPad Air, iPad Air 2, iPad mini, iPad mini 4, iPhone 5s, iPhone 6s, iPhone 6s Plus, Apple TV, Appe Watch, Capas e Acessórios.'''</p>")
print("</div>") 
#right section end


print("</div>") 
# content row 1 end

# content row 2 end
print("<div class='cnt-row2'>")
print("<img src='images/iii3.jpg' width='100%'>")
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

