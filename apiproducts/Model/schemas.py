from pydantic import BaseModel

class Product(BaseModel):
    id: int
    Name : str
    Quantity: int
    Description : str
    Price : float
    Category : int


class ProductCreate(BaseModel):
    Name : str
    Quantity: int
    Description : str
    Price : float
    Category : int
