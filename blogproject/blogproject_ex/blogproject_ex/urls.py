
from django.contrib import admin
from django.urls import URLPattern, path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),

    # html form 을 이용하여 블로그에 객체 만들기
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),

#    django form을 이용해 블로그 객체 만들기
   path('formcreate/' , views.formcreate,name='formcreate'),

#   django moeldform 을 이용해 블로그 객체 만들기
   path('modelformcreate/' , views.modelformcreate,name='modelformcreate'),



   path('detail/<int:blog_id>',views.detail, name='detail'),

   
   path('create_comment/<int:blog_id>',views.create_comment, name='create_comment'),

   
   path('login/',accounts_views.login,name='login'),

   path('logout/',accounts_views.logout , name='logout'),
    
   ]
# media 파일에 접근할 수 있는 url도 추가해주어야 함
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
