# vistas "generales"
from django.views.generic import TemplateView
from django.db.models import Count, Q
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.shortcuts import redirect
from calificaciones.models import Calificacion

class HomeView(TemplateView):
    # esta es la portada solo renderiza un html
    template_name = "core/home.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Estadísticas de calificaciones
        stats = Calificacion.objects.aggregate(
            total=Count('id'),
            vigentes=Count('id', filter=Q(estado='VIGENTE')),
            anuladas=Count('id', filter=Q(estado='ANULADA'))
        )
        context.update({
            'total_calificaciones': stats['total'],
            'vigentes': stats['vigentes'],
            'anuladas': stats['anuladas'],
        })
        return context


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return reverse('home')
        else:
            return reverse('calif_list')
