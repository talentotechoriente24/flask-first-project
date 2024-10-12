from app import create_app

# Crear la aplicación Flask usando la función factory `create_app`
app = create_app()

# Punto de entrada principal para ejecutar la aplicación
if __name__ == '__main__':
    # Ejecutar la aplicación Flask con el modo debug activado
    app.run(debug=True)
