from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

"""Yönetici paneli için bir yol (admin/) tanimlar ve theblog.urls dosyasındaki diğer 
tüm URL yollarini da dahil eder. Bu, theblog uygulamasindaki görünüm fonksiyonlarının ana 
URL yapilandirmasi içinde kullanilabileceği anlamina gelir
işlevi, belirli bir URL yolunu belirterek uygulamanin hangi görünüm fonksiyonuna yönlendirileceğini tanımlar
"""
urlpatterns = [
         
        path('admin/', admin.site.urls), 
        # ilgili view fonksiyonunu belirtir
        path('', include('theblog.urls')), 
        path('members/', include('django.contrib.auth.urls')), 
        path('members/', include('members.urls')), 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""(path('admin/', admin.site.urls))Bu satirin anlami Django, admin ile başlayan her URL için
ona uyan bir view bulur demektir. Bu durumda bir sürü 
yönetici URL'lerini ekliyoruz, böylece hepsi bu küçük
dosyanin içinde sikiştirilmiş bir şekilde durmuyor -- 
bu hali daha okunabilir ve düzenli.
"""

"""(path('', include('theblog.urls')) ile Django artik 'http://127.0.0.1:8000/' adresine gelen her şeyi 
blog.urls'e yönlendirecek ve oradaki yönergelere bakacak.
"""


        