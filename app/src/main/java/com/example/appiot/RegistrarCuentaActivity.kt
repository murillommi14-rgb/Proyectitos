package com.example.appiot

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity

/**
 * RegistrarCuentaActivity permite a los nuevos usuarios crear una cuenta.
 * Se recogen datos como usuario, email y contraseña.
 * La actividad valida que los campos no estén vacíos y que las contraseñas coincidan.
 * Esto demuestra un flujo de registro de usuario y la importancia de la validación de datos de entrada.
 */
class RegistrarCuentaActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_registrar_cuenta)

        // Se obtienen las referencias a las vistas del layout.
        val etUsuarioReg = findViewById<EditText>(R.id.etUsuarioReg)
        val etEmailReg = findViewById<EditText>(R.id.etEmailReg)
        val etClaveReg = findViewById<EditText>(R.id.etClaveReg)
        val etConfirmarClave = findViewById<EditText>(R.id.etConfirmarClave)
        val btnCrear = findViewById<Button>(R.id.btnCrear)

        // Se configura el listener para el botón "Crear".
        btnCrear.setOnClickListener {
            val usuario = etUsuarioReg.text.toString()
            val email = etEmailReg.text.toString()
            val clave = etClaveReg.text.toString()
            val confirmarClave = etConfirmarClave.text.toString()

            // Se realizan las validaciones necesarias.
            if (usuario.isEmpty() || email.isEmpty() || clave.isEmpty() || confirmarClave.isEmpty()) {
                // Si algún campo está vacío, se notifica al usuario.
                mostrarDialogoDeError(getString(R.string.error), getString(R.string.campos_vacios))
            } else if (clave != confirmarClave) {
                // Si las contraseñas no coinciden, se muestra un error.
                // Esto es una medida de seguridad básica para asegurar que el usuario ha introducido la contraseña que quería.
                mostrarDialogoDeError(getString(R.string.error), getString(R.string.claves_no_coinciden))
            } else {
                // Simulación de la creación de una nueva cuenta.
                // Se informa al usuario de que la cuenta se ha creado con éxito y se le redirige al Login.
                mostrarDialogoDeExito(getString(R.string.registrar_cuenta), getString(R.string.cuenta_creada))
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
            // Cierra la actividad actual (RegistrarCuentaActivity)
            // y vuelve a la anterior en la pila, que es LoginActivity.
            finish()
        }
        builder.setCancelable(false) // Evita que el usuario cierre el diálogo pulsando fuera de él.
        builder.show()
    }
}
