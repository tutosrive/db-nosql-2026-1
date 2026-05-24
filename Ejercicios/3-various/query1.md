1. Contar el número de personas por "género"
   > Agrupacion: Cuando aparece "por cada" "para cada" ...

```shell
# Ver la estructura de la coleccion
db.personas.findOne({})
```

### Forma N°1

```shell
db.personas.aggregate(
    [
        {
            $group: {
                _id: "$gender",
                total: {$sum: 1}
            }
        }
    ]
)
```

### Forma N°2

```shell
db.personas.aggregate(
    [
        {
            $group: {
                _id: {
                    genero: "$gender"
                },
                total: {$sum: 1}
            }
        }
    ]
)
```

### Forma N°3

```shell
db.personas.aggregate(
    [
        {
            $group: {
                _id: "$gender",
                total: {$sum: 1}
            },
        },
        {$sort: {total: 1}}
    ]
)
```

---

> Modificación

Contar el número de personas por "género", con la siguiente salida:

```json
{
    genero: x,
    total: x
}
```

```shell
db.personas.aggregate(
    [
        {
            $group: {
                _id: "$gender",
                total: {$sum: 1}
            },
        },
        {
            $project: {
                _id: 0,
                genero: "$_id",
                total: 1
            }
        },
        {$sort: {total: 1}}
    ]
)
```
