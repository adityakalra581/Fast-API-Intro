## Integrating FastAPI-login

from fastapi import FastAPI 
from pydantic import BaseModel

from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

import requests

app = FastAPI()

db = []

## First Model.
class Employees(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(50)
    time = fields.CharField(50)
    date = fields.CharField(50)
    day = fields.CharField(50)


Emp_Pydantic = pydantic_model_creator(Employees, name='Employees')
EmpIn_Pydantic = pydantic_model_creator(Employees, name='EmployeesIn', exclude_readonly=True)

@app.get('/')
def index():
    return {"message":"hello world"}

## Create an Employee: [method = POST]
# @app.post('/create')
# def create_employee(emp:Employees):
#     db.append(emp.dict())
#     return db[-1]

@app.post('/emp/create')
async def create_emp(emp: EmpIn_Pydantic):
    emp_obj = await Employees.create(**emp.dict(exclude_unset=True))
    return await Emp_Pydantic.from_tortoise_orm(emp_obj)

## Get all the details from the Database: [method = GET]
@app.get('/emp/all')
async def get_emp():
    return await Emp_Pydantic.from_queryset(Employees.all())


## Get one entry:
@app.get('/emp/{name}')
async def get_one_emp(name: str):
    return await Emp_Pydantic.from_queryset_single(Employees.get(name=name))


## Deleting an entry:

@app.delete('/emp/{name}')
async def delete_emp(name: str):
    await Employees.filter(name=name).delete()
    return {}


### Registering ORM:
### Database used: SQLITE
### Models stored in app.py file

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['app']},
    generate_schemas=True,
    add_exception_handlers=True
)




