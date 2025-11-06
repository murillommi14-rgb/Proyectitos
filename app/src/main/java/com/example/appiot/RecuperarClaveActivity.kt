package com.example.appiot

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity

/**
 * RecuperarClaveActivity permite al usuario solicitar un restablecimiento de contraseña.
 * En esta simulación, el usuario introduce su email y la aplicación muestra una confirmación.
 * Esto demuestra un flujo de recuperación de cuenta y el uso de validaciones simples.
 */
class RecuperarClaveActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_recuperar_clave)

        // Se obtienen las referencias a las vistas del layout.
        val etEmail = findViewById<EditText>(R.id.etEmail)
        val btnEnviar = findViewById<Button>(R.id.btnEnviar)

        // Se configura el listener para el botón "Enviar".
        btnEnviar.setOnClickListener {
            val email = etEmail.text.toString()

            // Se valida que el campo de email no esté vacío.
            // En un escenario real, también se validaría que el formato del email sea correcto.
            if (email.isEmpty()) {
                mostrarDialogoDeError(getString(R.string.error), getString(R.string.campos_vacios))
            } else {
                // Simulación del envío de un correo de recuperación.
                // Se muestra un mensaje de confirmación al usuario y se le redirige al Login.
                mostrarDialogoDeExito(getString(R.string.recuperar_clave), getString(R.string.clave_enviada))
            }
        }
    }

    /**
     * Muestra un diálogo de alerta para errores o validaciones.
     * @param titulo El título del diálogo.
     * @param mensaje El mensaje a mostrar.
     */
    private fun mostrarDialogoDeError(titulo: String, mensaje: String) {
        val builder = AlertDialog.Builder(this)
        builder.setTitle(titulo)
        builder.setMessage(mensaje)
        builder.setPositiveButton("OK", null) // No hace nada al pulsar OK, solo cierra el diálogo.
        builder.show()
    }

    /**
     * Muestra un diálogo de alerta para notificar un éxito y, al pulsar "OK",
     * cierra la actividad actual para volver a la pantalla de Login.
     * @param titulo El título del diálogo.
     * @param mensaje El mensaje a mostrar.
     */
    private fun mostrarDialogoDeExito(titulo: String, mensaje: String) {
        val builder = AlertDialog.Builder(this)
        builder.setTitle(titulo)
        builder.setMessage(mensaje)
        // Al pulsar "OK", se ejecuta el código dentro del listener.
        builder.setPositiveButton("OK") { _, _ ->
            // Cierra la actividad actual (RecuperarClaveActivity)
            // y vuelve a la anterior en la pila, que es LoginActivity.
            finish()
        }
        builder.setCancelable(false) // Evita que el usuario cierre el diálogo pulsando fuera de él.
        builder.show()
    }
}
