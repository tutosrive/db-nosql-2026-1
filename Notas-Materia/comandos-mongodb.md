```mongodb
db.users.updateMany({},{$set: {estado:{descripción: "activo", actualizado:"Hace 1 hora"}}})
```



---

```mongodb
db.users.updateMany({},{$set: {estado:{descripción: "activo", actualizado:"Hace 1 hora", detalles:{detalle:"Creado por Santiago"}}}})
```



---

```mongodb
db.users.updateOne({nombre:"Paula Rojas"},{$set: {aficiones:["catar","bailar","presentar"]}})
```



---

## Ejercicio

- Devolver el nombre del usuario cuyo estado ha sido creado por Juan

---

Dentro del historial debe aparecer un atributo que se llame "medicos", donde aparece un arreglo que esta compuesto por dos claves, "nombre" y "especialidad"

---

Database "dbvehiculos" con una conexion que se llame "persona_vehiculo", e incrustar 3 documentos con 3 niveles, en los cuales aparezca: "cedulapersona", "nombrepersona", "ciudad"
y debe aparecer lainformacion del vehiculo incrustada con una lista de comparendos con una sola clave ...

---

el texto de la pregunta p1r2

---

```mongodb
db.personas.aggregate([
 {
 $project: {
 _id: 0,
 nombre: { $concat: ["$name.first", " ", "$name.last"] },
 ciudad: "$location.city",
 email: "$email",
 estado: "$location.state",
 pais: "$nat",
 edad: "$dob.age"
}
 },
 { $limit: 10 }
])
```



---

edad de registro y descripcion de la locacion

```mongodb
db.personas.aggregate([
 {
 $project: {
 _id: 0,
 nombre: { $concat: ["$name.first", " ", "$name.last"] },
 email: "$email",
 estado: "$location.state",
 edad_registro: "$registered.age", 
descripcion_locacion: "$location.timezone.description"
}
 },
 { $limit: 25 }
])
```



---

# Proyecto

- Nombre
- Introduccion
- Objetivo general
- 2 Objetivos especificos
- Objeto/modelo de negocio
- Consultas
  - Q1: Primer Orden
  - Q2: Segundo Orden
  - Q3: Opcionales 
- 1.5 millones de registros ...
- Se usará Frontend? conexión a que lenguaje? o shell?

---

- top 5 personas mas jovenes
- ambas

```mongodb
db.personas.aggregate([
 {
 $project: {
 _id: 0,
 nombre: { $concat: ["$name.first", " ", "$name.last"] },
 edad: "$dob.age",
 nat: 1
 }
 },
 { $sort: { edad: 1 } },
 {
 $uinonWith: 
}
 { $limit: 5 }
])
```



---

## Proyectar esto

Proyectar en un solo campo el titulo de la persona y el apellido en un campo llamado "nombre" para las personas de sexo femenino cuya edad de registro este entre 15 y
20 años inclusive, limite de 500, ordenados por el apellido ascendentemente

```mongodb
db.personas.aggregate([
 { $match: { "gender": "male", "dob.age": { $gte: 15 , $lte: 20} } },
 { $project: {
 _id: 0,
 nombre: { $concat: ["$name.title", " ", "$name.last"] },
 edad: "$dob.age",
 nat: 1
 }
 },
 {$sort: {"apellido": 1}},
 { $limit: 500 }
 ])
```



---

# Tarea:

Actualizar las edades de todas las personas a la fecha actual ...