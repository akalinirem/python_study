from django.contrib import admin
from theblog.models import Post,Category,Profile


# Post sınıfını kayıt ettiriyoruz.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)




