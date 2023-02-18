from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user.views import Register, PasswordChangeForm
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls'), name='home-page'),
    path('register/', Register.as_view(), name='register'),
    path('register/success/', TemplateView.as_view(template_name='registration/success.html'), name='register-success'),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

