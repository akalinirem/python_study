from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView ,CreateView,UpdateView,DeleteView
from django.views import generic
from theblog.models import Post,Category
from theblog.forms import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# updateview fonksiyonu görünümleri güncellemek için kullanılır

# views.py web uygulaması görünüm fonksiyonudur.

"""(home fonksiyou tanimlanmiş http isteklerini işlemek üzere request nesnesini alir)
def home(request):      
 
('render' fonksiyonuyla 'home.html' adli  template dosyasini işler http yanitini oluşturur) 
    return render(request, 'home.html', {})           
    
'render' fonksiyonunun üçüncü paremetreresi template dosyasina ileten bağimsiz 
değişkenleri içeren bir sözlüktür bu paremetre de boş bir sözlük kullanilir.
"""

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:   
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('theblog:article-detail', args=[str(pk)]))
    

class HomeView(ListView):
   
    """Post modelini temsil eden "Post" adli bir veritabani modelini kullanarak 
    "home.html" adli bir template dosyasini kullanarak bir liste görünümü oluşturur. 
    "ListView" sinifi, veri tabanindan alinan verileri bir liste şeklinde temsil eden Django sinifidir.
    Bu örnekte, "Post" modelinden nesnelerin bir listesini görüntülemek için kullanilir.
    """

    """show the list of blog"""

    model = Post
    template_name = 'home.html'
    
    """'ordering'siralama yapmak üzere kullanilir.
    'id' alanina göre siralama yapilacaği belirtiliyor.- sembolü, 
    siralamanin tersine çevrileceğini belirtir. 
    Yani burada, id alanina göre azalan siralama yapilacaktir.
    """
    ordering = ['-post_date']
    # ordering = ['-id']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html', {'cat_menu_list': cat_menu_list})

    
def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html', {'cats': cats.title().replace('-',' '),
        'category_posts':category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
            cat_menu = Category.objects.all()
            context = super(ArticleDetailView, self).get_context_data()

            stuff = get_object_or_404(Post, id=self.kwargs['pk'])
            total_likes = stuff.total_likes()

            liked = False
            if stuff.likes.filter(id=self.request.user.id).exists():
                liked = True
            
            context["cat_menu"] = cat_menu
            context["total_likes"] = total_likes
            context["liked"] = liked
            return context

class AddPostView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'body')



class UpdatePostView(UpdateView):
    model = Post
    """EditForm sınıfı, genellikle bir veritabanındaki verileri düzenlemek 
    için kullanılan bir formdur.
    Form, kullanıcının verileri değiştirmesine ve ardından bu 
    değişiklikleri veritabanına kaydetmesine olanak tanır.
    """
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(generic.DeleteView):
    model = Post
    # 'template_name' özelliği, silme işleminin gerçekleşeceği özel bir şablon dosyasının adını belirtir.
    template_name = 'delete_post.html'
     # 'success_url' kullanıcının bir gönderiyi başarıyla sildikten sonra yönlendirileceği URL'yi belirtir.
     # 'reverse_lazy' argüman olarak verilen URL adına göre URLs.py dosyasındaki ilgili URL'yi döndürür.
    success_url = reverse_lazy('theblog:home')
