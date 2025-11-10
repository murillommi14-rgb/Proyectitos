# rutas del módulo calificaciones
from django.urls import path
from .views import CalificacionListView, CalificacionCreateView, CalificacionUpdateView, CalificacionDeleteView, export_excel, export_pdf, BulkUploadView, download_template_csv, download_template_xlsx, download_template_pdf, preview_bulk_upload, bulk_upload_ajax, dashboard_data

app_name = 'calificaciones'

urlpatterns = [
    path("", CalificacionListView.as_view(), name="calif_list"),
    path("crear/", CalificacionCreateView.as_view(), name="crear"),
    path("<int:pk>/editar/", CalificacionUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", CalificacionDeleteView.as_view(), name="eliminar"),
    path("export/excel/", export_excel, name="export_excel"),
    path("export/pdf/", export_pdf, name="export_pdf"),
    path("carga-masiva/", BulkUploadView.as_view(), name="bulk_upload"),
    path("descargar-plantilla-csv/", download_template_csv, name="download_template_csv"),
    path("descargar-plantilla-xlsx/", download_template_xlsx, name="download_template_xlsx"),
    path("descargar-plantilla-pdf/", download_template_pdf, name="download_template_pdf"),
    path("preview_bulk_upload/", preview_bulk_upload, name="preview_bulk_upload"),
    path("bulk_upload_ajax/", bulk_upload_ajax, name="bulk_upload_ajax"),
    path("dashboard-data/", dashboard_data, name="dashboard_data"),
]
