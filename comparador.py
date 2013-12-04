# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib2 import urlopen

print 'Content-type: text/html'
print 
print '''<html>
<head><title>Comparativa de precios</title>
<meta charset="utf-8">
<meta http-equiv="refresh" content="10">
</head>
<body>
'''

print '<h2>PROFESIONAL PHP 6</h2>'




url1 = ['http://www.casadellibro.com/libro-profesional-php-6-anaya-multimediawrox/9788441526341/1339131']
url2 = ['http://www.amazon.es/PHP-6-Anaya-Multimedia-Wrox/dp/8441526346/']
url3 = ['http://libros.fnac.es/a342029/Ed-Lecky-Thompson-PHP-6']


soup = BeautifulSoup(urlopen(url1))
precio1 = soup.find('span', {'class' : 'new'})
precio1 = precio1.get_text()

soup = BeautifulSoup(urlopen(url2))
precio2 = soup.find('span', {'class' : 'price'})
precio2 = precio2.get_text()

soup = BeautifulSoup(urlopen(url3))
precio3 = soup.find('span', {'class' : 'price prix-rouge'})
precio3 = precio3.get_text()

print '<p>Precio en Casa del libro: ', precio1,'</p>'  
print '<p>Precio en Amazon: ',precio2,'</p>'  
print '<p>Precio en Fnac: ',precio3,'</p>'  


print '</body></html>'
