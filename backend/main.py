from fastapi import FastAPI

from fastapi.responses import JSONResponse

from pydantic import BaseModel
from typing import List, Union
import subprocess

app = FastAPI()

class Person (BaseModel):
    name: str
    age: int
    address: str

DB: List[Person] = [
Person(name="John", age=29, address="USA"),
Person(name="Emma", age=25, address="Canada"),
Person(name="Alex", age=31, address="India"),
Person(name="John", age=22, address="USA"),
Person(name="Emma", age=29, address="Canada")
]

@app.get("/api")
def read_root():
    return DB

@app.get('/run-python-script')
def run_python_script():
    result = subprocess.run(['python', 'pythonscript.py'], capture_output=True, text=True)
    return JSONResponse(content={'result': result.stdout})



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
