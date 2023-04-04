from fastapi import FastAPI, Body
import schemas

app = FastAPI()

fakeDatabase = {
    1: {'task': 'Clean car'},
    2: {'task': 'Write Blog'},
    3: {'task': 'Start Stream'}
}


@app.get("/")
def getItems():
    return fakeDatabase

# to run app uvicorn main:app --reload
# Swagger UI automatically included in /docs#


@app.get("/{id}")
def getItem(id: int):
    return fakeDatabase[id]


""" 
method 1
@app.post("/")
def addItem(task:str):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task": task}
    return fakeDatabase
"""
# method2 using pydantic schema


@app.post("/")
def addItem(item: schemas.Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task": item.task}
    return fakeDatabase


"""
 # method 3 using request body
@app.post("/")
def addItem(body=Body()):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task": body['task']}
    return fakeDatabase """


@app.put("/{id}")
def updateItem(id: int, item: schemas.Item):
    fakeDatabase[id]['task'] = item.task
    return fakeDatabase


@app.delete("/{id}")
def deleteItem(id: int):
    del fakeDatabase[id]
    return fakeDatabase
