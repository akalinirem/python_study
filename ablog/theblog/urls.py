from django.urls import path
# from . import views
from theblog.views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView


# url sayısı arttığında birbirine karışmaması için nereden geldiğini yazarız
app_name = 'theblog' 

"""(path('',views.home, name="home"))ana URL'e home adinda bir view atiyoruz. Django URL resolver 
ful URL'in başindaki domain adini (yani, http://127.0.0.1:8000 /) göz ardi eder, 
böylece bu URL kalibi (pattern) boş bir string ile eşleşecek. Bu kalip, 
Django'ya eğer siteye biri 'http://127.0.0.1:8000/' adresinden gelirse 
gitmesi gereken yerin views.home olduğunu söylüyor.

 Son kisim name='home', görünümü (view) tanimlamak için kullanilan URL'in adidir. 
Bu view'un adi ile ayni olabilir ama tamamen farkli bir şey de olabilir. 
Bundan sonra projede isimlendirilmiş URL'leri kullaniyor olacağiz, 
bu yüzden uygulamadaki her URL'i isimlendirmek önemli. Ayni zamanda 
URL isimlerini eşsiz ve kolay hatirlanabilir şekilde seçmeliyiz.
""" 


"""web uygulamasinin ana sayfasina yönlendirir.' HomeView' adli bir sinif tabanli görünümü kullanarak, 
'as_view() yöntemi çağrilarak ana sayfa görüntülenir. 

'name' parametresi, yönlendirmenin bir ad vererek tanimlanmasina olanak tanir. 

Bu ad, uygulamasinin diğer kisimlarinda kullanilabilir ve URL'yi belirlemek için kullanilabilir.
"""

""" 'article-detail' adli bir URL tanimlar. Bu URL, 'ArticleDetailView'
adli bir sinif tabanli görünüme yönlendirir ve "pk" adli bir parametre alir.
'pk', makalelerin benzersiz kimliklerini temsil eden bir tamsayi değeridir. 
Bu URL, belirli bir makaleye doğrudan erişim sağlar. 
Bu URL yönlendirmesi de bir ad ile tanimlanir ve 'name' parametresi ile belirtilir.
"""

urlpatterns = [
    # path('',views.home, name="home"),
    path('', HomeView.as_view(), name= "home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/' , AddPostView.as_view(), name='add_post'),
    path('add_category/' , AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/remove/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category_list/<str:cats>', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    
]

"""<int:pk> ifadesi, bir URL'de bir tam sayi değerini ifade eder ve genellikle bir veritabani
modelinin id alani veya benzeri bir alanina karşilik gelir.
Bu ifade, bir URL'deki sayisal değeri yakalar ve bu değeri bir view  
fonksiyonuna argüman olarak geçirir. 
Bu sayede, bu view fonksiyonu belirtilen sayisal değeri kullanarak istenen 
veritabani kaydini bulabilir ve kullanicilara sunabilir.
"""

"""UPDATEVIEW özellikle bir model formu kullanarak model nesnesinin güncellenmesine yönelik kod tekrarini
önler ve veritabanina kaydetme işlemlerini de otomatik olarak yapar. Böylece, 
geliştiriciler veritabani işlemleri için 
daha az kod yazarak daha verimli bir şekilde çalişabilirler.
"""
