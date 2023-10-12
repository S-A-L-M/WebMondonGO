from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Config.db import db, app, ma


#Importar routes API
# from api.roles import routes_roles






#rutas | ¡¡¡RECUERDA PRIMERO IMPORTAR LA RUTA Y DESPUÉS AGREGARLO EN LA UBICACION DE RUTAS!!!! |
from Rutas.Main import routes_Main


#ubicacion del api
# app.register_blueprint(routes_roles, url_prefix="/api")






#ubicacion rutas
app.register_blueprint(routes_Main, url_prefix="/fronted")



@app.route("/")
def index():
    titulo= "Pagina Main"
    return render_template('/Main/Main.html', titles=titulo)


@app.route("/algo")
def otr():
    return "hola mondongo"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')



