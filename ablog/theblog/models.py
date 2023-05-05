from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


"""'models.Model' Post'un bir Django Modeli olduğunu belirtir, 
bu şekilde Django onu veritabaninda tutmasi gerektiğini bilir.
Post adinda bir tablo oluşturuyoruz.Post modelimizin ismi. 
Başka bir isim de verebilirdik (yeter ki özel karakterler ve 
boşluk kullanmayalim). 

Class isimleri her zaman büyük harf ile başlamalidir.
"""

    
"""Post sinifi models.Model sinifindan template alir title,title_tag,author,body
özellikleri tanimlanir.Bu özellikler title,title_tag,author,body sütunlarina
karşilik gelir.'Charfield','FroeignKey','TextField' sütunlarin veri 
türlerini  belirtir.
"""
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):       
        return self.name
    
    def get_absolute_url(self):
        return reverse('theblog:home')
    

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)
    


class Post(models.Model):

    # 255 karekterlik varchar alanı oluşturulur.
    title = models.CharField(max_length=255)

    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    # 255 karekterlik varchar alanı oluşturulur.
    title_tag = models.CharField(max_length=255, null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)

    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()
   

    def __str__(self):
        
        """bir nesnenin insan tarafindan okunabilir bir dize temsilini döndürmek 
        için kullanilir.
        Yöntem, nesnenin başlik ve yazarinin adini birleştirerek 
        bir dize döndürür.
        """
        return f"{self.title} | {self.author}"
    
    def get_absolute_url(self):
        # return reverse('theblog:article-detail', args=(str(self.id)))
        return reverse('theblog:home')
   



 