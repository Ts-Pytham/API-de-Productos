from fastapi import FastAPI, APIRouter, HTTPException
from Model.schemas import *

app = FastAPI(title = "API de productos")

router = APIRouter()

products = [
    {
        "id" : 1,
        "Name" : "Iphone 13",
        "Quantity" : 12,
        "Description" : "Nuevo celular de Apple",
        "Price" : 4500000,
        "Category" : 1
    },

    {
        "id" : 2,
        "Name" : "MSI GF13 Thing",
        "Quantity" : 10,
        "Description" : "Laptop para gamers",
        "Price" : 5000000,
        "Category" : 2
    }
]

@router.get("/products/")
def getProducts() -> dict:
    print(products)
    return products

@router.get("/products/{id}", status_code = 200)
def getProductsID(*, id : int) -> dict:
    result = [product for product in products if id == product["id"]]
    if(result):
        return result
    else:
        raise HTTPException(detail = "El id no encontró en los productos", status_code = 404)

@router.get("/products/category/{category_id}", status_code = 200)
def getCategory(*, category_id : int) -> dict:
    result = [product for product in products if category_id == product["Category"]]
    if(result):
        return result
    else:
        raise HTTPException(detail = "El id no encontró la categoría", status_code = 404)

@router.post("/products/", status_code = 201, response_model = Product)
def postProducts(product : ProductCreate) -> dict:
    new_id = len(products) + 1
    new_product = Product(
        id = new_id,
        Name = product.Name,
        Quantity = product.Quantity,
        Description = product.Description,
        Price = product.Price,
        Category = product.Category
    )
    products.append(new_product.dict())
    return new_product

app.include_router(router)