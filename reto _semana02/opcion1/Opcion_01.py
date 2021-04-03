from flask import  Flask, request
from flask_cors import CORS

appDep = Flask(__name__)
CORS(appDep)
departamentos = []
@appDep.route("/")

def inicioDep():
    return "Flask se inicio satisfactoriamente"

# appDep.run(debug=True, port=1500)

@appDep.route("/departamento/<int:id>", methods=['GET','PUT','DELETE'])
def departamento(id):
    if len(departamentos) > id: #Consulta si el String es > al id
        if request.method == "GET":
            return {
                "ok": True,
                "content": departamentos[id],
                "message": None
            }
        elif request.method == "PUT":
            data = request.get_json()
            departamentos[id] = data
            return {
                "ok": True,
                "content": departamentos[id],
                "message": "Se actualizo el departamento correctamente"
            }, 201
        elif request.method == "DELETE":
            departamento = departamentos.pop(id)
            return {
                "ok": True,
                "content": departamento,
                "message": "Se elimino el departamento correctamente"
            }, 200
            del departamentos[id]
            return {
                "ok": True,
                "content": None,
                "message": "Se elimino el departamento correctamente"
            }, 200
        else:
            return {
            "ok": False,
            "content": None,
            "message": "El departamento no Existe"
        }

@appDep.route("/departamento/buscar/<string:palabra>")
def buscador(palabra):
    resultado = []
    for departamento in departamentos:
        print (palabra.lower())
        if palabra.lower() in departamento['nombre'].lower():
            resultado.append(departamento)
    if resultado:
        return {
            "ok": True,
            "content": resultado,
            "message": None
        }
    else:
        return {
            "ok": False,
            "content": "No hay resultados",
            "message": None
        }, 404
@appDep.route("/departamentos", methods = ["GET","POST"])
def manejo_departamentos():
    print(request.method)
    if request.method == "GET":
        if departamentos:
            return {
                "ok": True,
                "content": departamentos,
                "message": None
            }
        else:
            return {
                "ok": False,
                "content": None,
                "message": "No hay departamentos"
            }, 404
    elif request.method == "POST":
        data = request.get_json()
        departamentos.append(data)
        return{
            "ok": True,
            "content": None,
            "message": "El departamento se agrego exitosamente"
        }, 201
        
appDep.run(debug=True, port=1300) 