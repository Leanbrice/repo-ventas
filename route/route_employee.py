#ruta empleado
from flask import Blueprint,request,jsonify
from Database import db
from model.employee import Employee

employee=Blueprint("employee",__name__)
#Recibir empleados
@employee.route("/api/get_employee",methods="GET")

def get_employee():
    #Obtengo todos los objetos de empleados de db
    employees = Employee.query.all() 

    return jsonify([employee.serialize() for employee in employees])#formato jsonify

#Agregar empleados nuevos
@employee.route("/api/post_employee",methods=["POST"])

def post_employee():
    database=request.get_json()
    if not database:
        return jsonify({"Error":"No se encontraron datos"}),404
    
    try:
        new_employee=Employee(database["name"],database["email"],database["phone"],database["birthday"])
        print(f"Creando al nuevo empleado{new_employee.name}")
        
        db.session.add(new_employee)
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"Error":str(e)}),500
    
@employee.route("/api/delete_employee",methods=["DELETE"])

def delete_employee(id):
    employee=Employee.query.get(id)
    if not employee:
        return jsonify({"mensaje","No se encuentra empleado"}),404
    
    try:
        db.session.delete(employee)
        db.session.commit()
    
    except Exception as e:
        return jsonify({"Error":str(e)}),500

