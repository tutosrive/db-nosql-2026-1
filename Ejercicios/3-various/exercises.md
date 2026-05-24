# Ejercicios

1. Listar por ciudad de origen, top de las 50 ciudades con más personas

```
db.personas.aggregate([
    {
        $group: {
            _id: "$nat",
            total: {$sum: 1}
        }
    },
    {
        $sort: {total: -1}
    },
    {$limit: 50}
])
```

---

2. Listar por ciudad de origen, top de las 50 ciudades con más personas, con nacionalidad y conteo (proyeccion)

```
db.personas.aggregate([
    {
        $group: {
            _id: "$nat",
            total: {$sum: 1}
        }
    },
    {
        $sort: {total: -1}
    },
    {
        $project: {
            _id: 0,
            nacionalidad: "$_id",
            conteo: "$total"
        }
    },
    {$limit: 50}
])
```

---

3. Top de las 5 ciudades donde la persona vive, con menos personas, y debe estar ordenado por la ciudad, alfabeticamente de mayor a menor y por el total del menor a mayor

> Primero top de las ciudades con menos personas

```shell
db.personas.aggregate([
    {
        $group: {
            _id: "$location.city",
            total: {$sum: 1}
        },
    },
    {$sort: {total: 1}},
    {$limit: 5}
])
```

> Ahora si con las ordenaciones

```shell
db.personas.aggregate([
    {
        $group: {
            _id: "$location.city",
            total: {$sum: 1}
        },
    },
    {$sort: {_id: 1, total: 1}},
    {$limit: 5}
])
```

4. Número de personas ordenado por género y nacionalidad, nacionalidad de menor a mayor

```
db.personas.aggregate([
    {
        $group: {
            _id: {
                nacionalidad: "$nat", genero: "$gender"
            }, totalPersonas: {$sum: 1}
        }
    },
    {
        $sort: {"_id.nacionalidad": 1, genero: 1}
    }
])
```

5. El promedio de las edades por gérno y nacionalidad -> Top 5 mayor a menor.

```
db.personas.aggregate([
    {
        $group: {
            _id: {
                genero: "$gender", nacionalidad: "$nat"
            },
            promedio: {$avg: "$dob.age"}
        }
    },
    {$sort: {promedio: -1}},
    {$project: {_id: 0, genero: "$_id.genero", nacionalidad: "$_id.nacionalidad", promedio: 1}},
    {$limit: 5}
])
```

6. a

```
db.personas.aggregate([
    {$match: {"dob.age": {$gt: 20}}},
    {
        $group: {
            _id: {genero: "$gender", ciudad: "$location.city"},
            promedioEdadPersona: {$avg: "$dob.age"},
            promedioEdadRegistro: {$avg: "$registered.age"},
            mayorEdad: {$max: "$dob.age"},
            menorEdad: {$min: "$dob.age"},
            totalLocal: {$sum: 1}
        }
    },
    {$sort: {promedioEdadRegistro: -1}},
    {$limit: 30}
])
```

7. Listar para cada nacionalidad y para cada estado el total de personas pero solo de aquellas cuyo total sea mayor de 10 sin ningun de ordenación

```
db.personas.aggregate([
    {
        $group: {
            _id: {
                nacionalidad: "$nat", estado: "$location.state"
            },
            total: {$sum: 1}
        }
    },
    {$match: {total: {$gte: 10}}},
    {$project: {_id: 0, nacionalidad: "$_id.nacionalidad", estado: "$_id.estado", total: 1
    }}
])
```
