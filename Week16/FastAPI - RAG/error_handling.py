from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# ---------------------------------------------------------
# Step 1: Create the Custom Blueprint (The Error Class)
# ---------------------------------------------------------
class OutOfStockError(Exception):
    # The __init__ function sets up the error when we trigger it
    def __init__(self, item_name: str, requested: int, available: int):
        self.item_name = item_name
        self.requested = requested
        self.available = available

# ---------------------------------------------------------
# Step 2: Build the Safety Net (The Exception Handler)
# ---------------------------------------------------------
# This tells FastAPI: "If an OutOfStockError happens ANYWHERE, run this code."
@app.exception_handler(OutOfStockError)
async def out_of_stock_handler(request: Request, exc: OutOfStockError):
    # BOth the above arguments request and exc are msut for exception handling
    # We use 'exc' to access the data we stored in the __init__ function
    # Normally we don't need JSONResponse but in exception handling it is mandatory for
    # converting dictionaries to JSON strings.
    # FastAPI automatically takes care of it if no exception is raised.
    return JSONResponse(
        status_code=400, # 400 means "Bad Request" (the user asked for too much)
        content={
            "error_type": "inventory_shortage",
            "message": f"Cannot buy {exc.requested} of '{exc.item_name}'.",
            "action": f"Please lower your quantity. We only have {exc.available} left."
        }
    )

# ---------------------------------------------------------
# Step 3: Trigger the Error in your Business Logic
# ---------------------------------------------------------
@app.post("/buy/{item_name}")
def buy_item(item_name: str, quantity: int):
    inventory = {"laptop": 2, "mouse": 50}
    
    # Check if we have the item
    if item_name not in inventory:
        return {"error": "Item doesn't exist"}
        
    available_stock = inventory[item_name]
    
    # Check if they want too many
    if quantity > available_stock:
        # We TRIGGER the error here, passing in the data.
        # FastAPI immediately stops reading this function and throws 
        # the error up to the safety net (our handler).
        # We can raise an excpetion only if it is an instance of a 
        # class that inherits from Exception
        raise OutOfStockError(
            item_name=item_name, 
            requested=quantity, 
            available=available_stock
        )
        
    return {"message": f"Successfully bought {quantity} {item_name}(s)!"}