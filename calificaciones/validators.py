import os
from django.core.exceptions import ValidationError
from django.conf import settings

def validate_file_type(file):
    """Valida el tipo MIME del archivo basado en extensión"""
    allowed_extensions = ['.csv', '.xlsx', '.xls', '.pdf']
    file_extension = os.path.splitext(file.name)[1].lower()

    if file_extension not in allowed_extensions:
        raise ValidationError(f'Extensión de archivo no permitida: {file_extension}. Permitidas: {", ".join(allowed_extensions)}')

def validate_file_size(file):
    """Valida el tamaño del archivo"""
    max_size = getattr(settings, 'FILE_UPLOAD_MAX_MEMORY_SIZE', 10485760)  # 10MB default
    if file.size > max_size:
        raise ValidationError(f'Archivo demasiado grande. Máximo permitido: {max_size // (1024*1024)}MB')

def validate_csv_columns(df):
    """Valida que el DataFrame tenga las columnas requeridas"""
    required_columns = [
        'tipo_mercado', 'origen', 'mercado', 'instrumento', 'secuencia',
        'numero_dividendo', 'tipo_sociedad', 'fecha', 'valor_historico',
        'ejercicio', 'descripcion', 'isfut_casilla', 'factor_actualizacion'
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValidationError(f'Columnas faltantes en el archivo: {", ".join(missing_columns)}')

def antivirus_scan(file):
    """Escaneo básico de antivirus (placeholder para implementación real)"""
    # En producción, integrar con ClamAV u otro antivirus
    # Por ahora, solo verificar que no contenga código ejecutable básico
    try:
        content = file.read(1024).decode('utf-8', errors='ignore')
        suspicious_patterns = ['<script', 'javascript:', 'vbscript:', 'onload=', 'onerror=', 'eval(']
        if any(pattern in content.lower() for pattern in suspicious_patterns):
            raise ValidationError('Contenido sospechoso detectado en el archivo')
    except UnicodeDecodeError:
        # Si no puede decodificar como texto, asumir que es binario válido
        pass
    finally:
        file.seek(0)

def validar_suma_factores_limitada(instance):
    """Valida que la suma de factores no exceda 1.0"""
    factores = [
        getattr(instance, f'factor{i}', 0) or 0 for i in range(1, 27)
    ]
    suma = sum(factores)
    if suma > 1.0:
        raise ValidationError(f'La suma de los factores no puede exceder 1.0. Suma actual: {suma}')
