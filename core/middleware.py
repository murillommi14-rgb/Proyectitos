# middleware para capturar el request actual asi sabemos quien hizo que
import threading
_local = threading.local()

def get_current_request():
    return getattr(_local, "request", None)

def get_current_user():
    req = get_current_request()
    if req and hasattr(req, "user") and req.user.is_authenticated:
        return req.user
    return None

def get_ip_and_ua():
    req = get_current_request()
    if not req:
        return None, ""
    xff = req.META.get("HTTP_X_FORWARDED_FOR")
    ip = xff.split(",")[0].strip() if xff else req.META.get("REMOTE_ADDR")
    ua = req.META.get("HTTP_USER_AGENT", "")
    return ip, ua

class CurrentRequestMiddleware:
    # guarda el request en memoria local del hilo 
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        _local.request = request
        return self.get_response(request)
