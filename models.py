from pydantic import BaseModel, Field
from typing import Annotated

class Product(BaseModel):
    # id: Annotated[int, Field(description="Id", examples=101)]
    # name : Annotated[str, Field(description="Name", examples="Samsung S26")]
    # description : Annotated[str, Field(description="Description", examples="King of Mobiles")]
    # price : Annotated[float, Field(description="Price", examples=180000)]
    # quantity: Annotated[int, Field(description="Quantity", examples=210)]

    id: int
    name: str
    description: str
    price: float
    quantity: int
