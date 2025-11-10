from locust import HttpUser, task, between
import json
from datetime import date


class CalificacionUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Login
        response = self.client.post("/accounts/login/", {
            "username": "testuser",
            "password": "testpass"
        })
        if response.status_code != 200:
            # Cree el usuario si no existe.
            self.client.post("/admin/core/user/add/", {
                "username": "testuser",
                "password1": "testpass",
                "password2": "testpass"
            })

    @task(3)
    def view_list(self):
        self.client.get("/calificaciones/")

    @task(2)
    def create_calificacion(self):
        data = {
            "tipo_mercado": "ACCIONES",
            "origen": "CORREDORA",
            "ejercicio": str(date.today()),
            "mercado": "Test Mercado",
            "instrumento": "Test Instrumento",
            "fecha": str(date.today()),
            "secuencia": 10000,
            "numero_dividendo": 0,
            "tipo_sociedad": "A",
            "valor_historico": "100.00",
            "isfut_casilla": False,
            "descripcion": "Load test",
            "factor_actualizacion": "1.0000",
            "factor1": "0.1000",
            "estado": "BORRADOR",
        }
        self.client.post("/calificaciones/crear/", data)

    @task(1)
    def bulk_upload(self):
        # Simular carga masiva (archivo simulado)
        pass  # Requiere manipulación de archivos

    @task(1)
    def export_excel(self):
        self.client.get("/calificaciones/export/excel/")


# Ejecutar con: locust -f locustfile.py --host=http://localhost:8000
# Luego, acceder a http://localhost:8089 para la interfaz web
