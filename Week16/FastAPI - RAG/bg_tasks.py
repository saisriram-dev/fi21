from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

#Example 01
# Step 1: Define the slow function
def write_audit_log(username: str, action: str):
    print(f"Opening file to log {action}...")
    time.sleep(2) # Simulating a slow file write
    # In reality, you'd write to a file or database here
    print(f"Finished writing log: {username} performed {action}")

@app.delete("/files/{file_id}")
def delete_file(file_id: int, username: str, bg_tasks: BackgroundTasks): # Step 2: Add parameter
    
    # Step 3: Queue the task. 
    # Notice we don't use parenthesis like write_audit_log()!
    # We pass the function name, followed by its arguments.
    bg_tasks.add_task(write_audit_log, username, "deleted a file")
    
    # This returns instantly, before the 2-second sleep finishes!
    return {"message": f"File {file_id} deleted successfully."}


# Example 02
def notify_shipping_department(order_id: int):
    # Imagine this makes a network request to the shipping API
    print(f"Notifying shipping to pack order #{order_id}")

@app.post("/checkout")
def checkout(order_id: int, bg_tasks: BackgroundTasks):
    # Charge the credit card (we do this immediately so we know if it failed)
    payment_status = "Success" 
    
    # Send the notification in the background so the user's browser doesn't hang
    bg_tasks.add_task(notify_shipping_department, order_id)
    
    return {"message": "Payment successful! Your order is being packed."}
