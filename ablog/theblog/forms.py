from django import forms 
from theblog.models import Post,Category


"""Post modeli için bir Form sinifi oluşturuyor. Form, kullanicinin 
bir başlik, başlik etiketi, yazar ve gönderi gövdesi gibi bilgileri 
girerek bir blog gönderisi oluşturmasina izin verir.
"""

# choices = [('coding','coding'),('sports','sports'),('entertaintment','entertainment')]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag', 'author','category','body','snippet', 'header_image')

        widgets = {
            # ilk title satırının sonuna ,'placeholder': 'This is Title Placeholder Stuff' eklersek kutucuğa kalıcı yazı eklemiş oluruz 
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id':'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control','placeholder': '', 'id':'elder', 'type':'hidder'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # textarea küçük harf alanı anlamında kullanılır
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

            
}

class EditForm(forms.ModelForm):
    """ Meta sınıfı formun daha fazla özelliklerini belirlemek için 
    kullanılan bir sınıftır.Bu özellikler sayesinde, 
    bu form belirli bir modelle ilişkilendirilebilir ve bu modeldeki 
    alanlar otomatik olarak formun alanları olarak ayarlanabilir.
     """
    class Meta:
        model = Post
        # hangi alanların kullanılacağını belirtir
        fields = ('title', 'author', 'body','snippet')

        """ widgets özelliği, her bir alanın nasıl görüneceğini belirler.
        Bu widgetler, bir form alanının görünümünü 
        CSS sınıfları ile özelleştirmek için kullanılabilir. 
        """

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

}
            