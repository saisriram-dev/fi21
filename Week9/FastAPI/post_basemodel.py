from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# The product class inherits from BaseModel
class Product(BaseModel):
    name: str
    price: float
    quantity: int
    tax: bool = True  # Default value is True

    """
    While using BaseModel, we needn't use __init__ method.
    Also, the type hints won't just define or give info about the variables 
    but also validate them (only works when we use BaseModel).
    So if the data type is wrong, it will throw an error.

    This class represents a product with the following attributes:
    - name: str
    - price: float
    - quantity: int
    - tax: bool = True
    """


products = []


@app.post("/products/")
def add_product(product: Product):
    # The type of the attribute 'product' is base class Product
    # If the data type is wrong (i.e, if it doesn't follow BaseModel's attributes), it will throw an error
    products.append(product)
    return {"message": "Product added successfully", "product": product}


@app.get("/products/")
def get_products():
    return {"message": "Products retrieved successfully", "products": products}
