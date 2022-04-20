# Squad Makers

Jokes API chistes aleatorios

## Python Version

`3.9.6`

## Instalacion


```bash
pip install -r requirements/base.txt
```

## Herramientas de Desarrollador

Con el fin de permitir participar a distintos programadores en este repo,
se añadieron algunos linters para seguir algunos estandares a la hora de escribir
código, asi antes de enviar un commit a la rama se verifica y si todo esta bien
pasa de lo contrario modifica o avisa al programador que debe cambiar en su código

- install dev requirements `pip install -r requirements/dev.txt`
- run `pre-commit install`

## Correr el servidor
Es necesario tener docker y docker compose para ejecutar nuestra api, lo hice de esta forma
para que pueda ejecutarse en cualquier entorno sin problema

`docker-compose up`

EL RestAPI estará disponible en http://localhost:8081/


## Hacer Test

Instalamos requirements/test.txt

`pytest tests`

## Ver coverage
Instalamos requirements/test.txt

`pytest --cov`

## Docs
Podemos ver la documentación generada por fastapi en
http://localhost:8081/docs/
http://localhost:8081/redoc/


###TAREA 2:
¿Qué repositorio utilizarías?
PostgreSQL, MariaDB, Casandra, MongoDB, ElasticSearch, Oracle, SQL Server
1. Razona tu respuesta
2. Crea la sentencia para crear la BBDD y el modelo de datos que requerimos
3. Lo mismo que el punto anterior (si lo hiciste con una SQL) pero para un repositorio
noSQL.

### Solución
En este caso tenemos dos colecciones de chistes (Chistes de Papá, Chistes de Chuck Norrys)
Actualmente el sistema no hay relación entre chiste y algún otro modelo y justo ahi es donde brillan las bases
de datos Sql de alguna manera si elegimos ese tipo de base de datos  hay muchas funcionalidades que no usaremos
por eso me decanto mas por una base de datos NoSql donde tendré colecciones (Chistes de Papá, Chistes de Chuck Norrys)
y en ellas documentos que serán los chistes

```python
>> pip install pymongo

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017", )
database =client["jokes"]
dad_joke_collection = database["dad"]
chuck_joke_collection = database["chuck"]

dad_joke = {
    "text": "Funny dad joke",
    "icon": "Icon"
}
chuck_joke = {
    "text": "Funny chuck joke",
    "icon": "Icon"
}
dad_joke_collection.insert_one(dad_joke)
chuck_joke_collection.insert_one(chuck_joke)
client.close()
```

Ahora en caso fuera una base de datos sql
```sql
CREATE TABLE joke (
    icon VARCHAR,
    joke VARCHAR NOT NULL,
    url VARCHAR,
    id SERIAL,
    PRIMARY KEY (id)
 )
 ```
