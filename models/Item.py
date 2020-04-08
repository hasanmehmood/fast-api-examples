from pydantic import BaseModel


# This model will help us validating the required fields in
# the request payload
class Item(BaseModel):
	name: str
	price: float
	is_offer: bool = None
