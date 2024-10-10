from service.service import get,add,delete,update
from fastapi import APIRouter 

router=APIRouter()
@router.get("/")
def get_data():
    return get()
@router.post("/add_data")
def add_data():
    return add()

@router.delete("/delete_data")
def delete_data():
    return delete()

@router.put("/update_data")
def update_data():
    return update()

    
