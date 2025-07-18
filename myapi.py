from fastapi import FastAPI
from fastapi import Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
students = {
    1: {
        "name": "Nour",
        "age": 22,
        "position":"software dev"
    }
}
class Student(BaseModel):
    name:str
    age:int
    year:str

@app.get("/")
def index():
    return {"name":"First Date"}

@app.get("/getstudent/{student_id}")
def get_student(student_id: int= Path(description = "the Id of the student you want to view",gt=0)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(*, name:Optional[str]=None, test:int):
    for student_id in students:
        if(students[student_id]["name"] == name):
            return students[student_id]
    return {"Data" : "not found"}



@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:Student):
    if student_id in students:
        students[student_id]=student
        return students[student_id]
    return{"Error":"Student not found"}
        