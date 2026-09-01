from fastapi import FastAPI, HTTPException, Depends
from models import Product
import model_db 
from config import session, engine
from sqlalchemy.orm import Session

app = FastAPI()


model_db.base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Hello, i'm HERE!"}


products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]


# Dependencie Injection - function to get db
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# Database -> Add above products value in product_db
def init_db():
    db = session()
    count = db.query(model_db.Product).count

    if count == 0:
        for product in products:
            db.add(model_db.Product(**product.model_dump()))
        db.commit()

init_db()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_product = db.query(model_db.Product).all()
    return db_product


@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):

    db_product = db.query(model_db.Product).filter(model_db.Product.id == id).first()
    if db_product:
        return db_product
    # for product in products:
    #     if product.id == id:
    #         return product

    raise HTTPException(status_code=404, detail="Product Not Found!")


@app.post("/product")
def add_products(product: Product):
    products.append(product)
    return product


@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully!"

    raise HTTPException(status_code=404, detail="Product Not Found!")


@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            products.remove(products[i])
            return "Product deleted successfully!"

    raise HTTPException(status_code=404, detail="Product Not Found!")
 