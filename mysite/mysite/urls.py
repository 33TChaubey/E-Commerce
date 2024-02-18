from django.contrib import admin
from django.urls import path, include
from users import views as userviews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecom/', include('ecom.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/',userviews.ProfilePage,name='profilepage'),
    path('profformedit/<int:prof_id>/',userviews.ProfileEdit,name="profformedit"),
    path('profformcreate/<int:user_id>/',userviews.ProfileCreate,name="profformcreate")
]

urlpatterns += [] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)