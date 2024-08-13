from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi
from datetime import datetime

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URL"), tlsCAFile=certifi.where())
db = client['punto_venta']
collection = db['productos']


@app.route('/agregar', methods=['POST'])
def agregar_producto():
    data = request.json
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    result = collection.insert_one(data)
    return jsonify({"msg": "Producto agregado", "id": str(result.inserted_id)}), 201


@app.route('/historial', methods=['GET'])
def ver_historial():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({"error": "Fecha no proporcionada"}), 400
    try:
        fecha_formateada = datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Formato de fecha incorrecto, use YYYY-MM-DD"}), 400

    productos = collection.find({"fecha": fecha})
    resultado = list(productos)
    for producto in resultado:
        producto["_id"] = str(producto["_id"])

    return jsonify(resultado), 200

@app.route('/corte_dia', methods=['GET'])
def corte_dia():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({"error": "Fecha no proporcionada"}), 400
    try:
        fecha_formateada = datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Formato de fecha incorrecto, use YYYY-MM-DD"}), 400
    productos = collection.find({"fecha": fecha})
    total = 0
    for producto in productos:
        try:
            total += float(producto['precio'])
        except (ValueError, TypeError):
            return jsonify({"error": f"El precio '{producto['precio']}' no es un número válido"}), 400
    return jsonify({"fecha": fecha, "total": total}), 200

if __name__ == '__main__':
    app.run(debug=True)
