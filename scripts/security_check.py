#!/usr/bin/env python
"""
Script de verificación de seguridad para CI/CD
Ejecuta análisis de seguridad estático y dependencias
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Ejecuta un comando y retorna el resultado"""
    print(f"\n🔍 Ejecutando: {description}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - PASÓ")
            return True
        else:
            print(f"❌ {description} - FALLÓ")
            print("Error output:", result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error ejecutando {description}: {e}")
        return False

def main():
    """Función principal de verificación de seguridad"""
    print("🚀 Iniciando verificación de seguridad...")

    # Cambiar al directorio del proyecto
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)

    checks_passed = 0
    total_checks = 0

    # 1. Verificar que no hay SECRET_KEY hardcodeada
    total_checks += 1
    if run_command('grep -r "SECRET_KEY.*=" nuam_mantenedor/settings.py | grep -v "os.environ"', "Verificación de SECRET_KEY no hardcodeada"):
        checks_passed += 1

    # 2. Verificar que DEBUG=False en producción
    total_checks += 1
    if run_command('grep "DEBUG.*=.*os.environ" nuam_mantenedor/settings.py', "Verificación de DEBUG desde variables de entorno"):
        checks_passed += 1

    # 3. Ejecutar Bandit para análisis de seguridad estático
    total_checks += 1
    if run_command('bandit -r . -x ./venv,./__pycache__,./migrations,./static,./media', "Análisis de seguridad Bandit"):
        checks_passed += 1

    # 4. Verificar dependencias con Safety
    total_checks += 1
    if run_command('safety check', "Verificación de vulnerabilidades en dependencias"):
        checks_passed += 1

    # 5. Verificar configuración de CSP
    total_checks += 1
    if run_command('grep "CSP_DEFAULT_SRC" nuam_mantenedor/settings.py', "Verificación de Content Security Policy"):
        checks_passed += 1

    # 6. Verificar configuración HTTPS
    total_checks += 1
    if run_command('grep "SECURE_SSL_REDIRECT" nuam_mantenedor/settings.py', "Verificación de HTTPS forzada"):
        checks_passed += 1

    # 7. Verificar rate limiting
    total_checks += 1
    if run_command('grep "AXES_FAILURE_LIMIT" nuam_mantenedor/settings.py', "Verificación de rate limiting"):
        checks_passed += 1

    # Resultado final
    print(f"\n📊 Resultado: {checks_passed}/{total_checks} verificaciones pasaron")

    if checks_passed == total_checks:
        print("🎉 ¡Todas las verificaciones de seguridad pasaron!")
        return 0
    else:
        print("⚠️  Algunas verificaciones fallaron. Revisa la configuración de seguridad.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
