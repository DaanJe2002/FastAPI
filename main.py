from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

inventory = {
    1: {
        'name':'milk',
        'price': 3.99,
        'brand':'laciate'
    }

}
@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None,description='The Id of the itme you would like to view')):
    return inventory[item_id]

@app.get('/get-by-name/{item_id}')
def get_name(*,item_id ,name: Optional[str] = None, test : int):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
        return {'Data not found'}
@app.post('/create_item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return{"Error, item already exists"}

    inventory[item_id] = {'name': item.name,'brand':item.brand,'price':item.price}
    return inventory[item_id]