package com.example.appiot

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.appcompat.app.AppCompatActivity

/**
 * SplashActivity es la primera pantalla que se muestra al usuario.
 * Su propósito es mostrar el logo o la marca de la aplicación durante un breve período de tiempo
 * antes de redirigir al usuario a la pantalla principal o de inicio de sesión.
 */
class SplashActivity : AppCompatActivity() {

    // Define el tiempo que se mostrará el splash screen en milisegundos (ej. 3000ms = 3 segundos)
    private val SPLASH_TIME_OUT: Long = 3000

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        // Se utiliza un Handler para ejecutar una acción después de un tiempo determinado.
        // Esto nos permite mostrar el splash durante el tiempo definido en SPLASH_TIME_OUT.
        Handler(Looper.getMainLooper()).postDelayed({
            // Una vez transcurrido el tiempo, se crea un Intent para abrir LoginActivity.
            val intent = Intent(this, LoginActivity::class.java)
            startActivity(intent)

            // Se llama a finish() para cerrar SplashActivity.
            // Esto evita que el usuario pueda volver a esta pantalla presionando el botón "Atrás".
            finish()
        }, SPLASH_TIME_OUT)
    }
}
