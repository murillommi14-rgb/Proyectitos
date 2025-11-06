package com.example.appiot

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity

/**
 * LoginActivity es la pantalla donde los usuarios pueden iniciar sesión.
 * También ofrece opciones para registrarse o recuperar la contraseña.
 * Esta actividad demuestra el uso de componentes de UI, la gestión de eventos de clic
 * y la navegación a otras actividades.
 */
class LoginActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        // Se obtienen las referencias a las vistas (EditText y Button) del layout activity_login.xml.
        // Esto nos permite interactuar con ellas, por ejemplo, leer el texto de un EditText o definir qué pasa cuando se pulsa un botón.
        val etUsuario = findViewById<EditText>(R.id.etUsuario)
        val etClave = findViewById<EditText>(R.id.etClave)
        val btnIngresar = findViewById<Button>(R.id.btnIngresar)
        val btnRecuperarClave = findViewById<Button>(R.id.btnRecuperarClave)
        val btnRegistrarCuenta = findViewById<Button>(R.id.btnRegistrarCuenta)

        // Se configura el listener para el botón de "Ingresar".
        // Este bloque de código se ejecutará cada vez que el usuario haga clic en él.
        btnIngresar.setOnClickListener {
            val usuario = etUsuario.text.toString()
            val clave = etClave.text.toString()

            // Se valida que los campos no estén vacíos.
            // En una aplicación real, aquí se haría una llamada a un servidor para autenticar al usuario.
            if (usuario.isEmpty() || clave.isEmpty()) {
                mostrarDialogo(getString(R.string.error), getString(R.string.campos_vacios))
            } else {
                // Simulación de un inicio de sesión exitoso.
                // Se muestra un mensaje de bienvenida para dar feedback al usuario.
                mostrarDialogo(getString(R.string.login), getString(R.string.login_exitoso))
            }
        }

        // Se configura el listener para el botón "Recuperar Clave".
        // Al hacer clic, se inicia la RecuperarClaveActivity.
        btnRecuperarClave.setOnClickListener {
            val intent = Intent(this, RecuperarClaveActivity::class.java)
            startActivity(intent)
        }

        // Se configura el listener para el botón "Registrar Cuenta".
        // Al hacer clic, se inicia la RegistrarCuentaActivity.
        btnRegistrarCuenta.setOnClickListener {
            val intent = Intent(this, RegistrarCuentaActivity::class.java)
            startActivity(intent)
        }
    }

    /**
     * Muestra un diálogo de alerta (AlertDialog) con un título y un mensaje.
     * Es una forma útil y estándar en Android de mostrar notificaciones o mensajes importantes al usuario.
     * @param titulo El texto que aparecerá en la cabecera del diálogo.
     * @param mensaje El cuerpo del mensaje que se quiere mostrar.
     */
    private fun mostrarDialogo(titulo: String, mensaje: String) {
        val builder = AlertDialog.Builder(this)
        builder.setTitle(titulo)
        builder.setMessage(mensaje)
        // Se añade un botón "OK" para que el usuario pueda cerrar el diálogo.
        builder.setPositiveButton("OK", null)
        builder.show()
    }
}
