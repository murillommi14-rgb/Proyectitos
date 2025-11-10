# enrutador principal aca declaramos rutas globales
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import HomeView, CustomLoginView  # nuestra portada

urlpatterns = [
    path("admin/", admin.site.urls),                 # panel admin
    path("", CustomLoginView.as_view(), name="login"),       # login
    path("home/", HomeView.as_view(), name="home"),       # home
    path("calificaciones/", include("calificaciones.urls")),  # modulo calificaciones
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
