from backend.agents.recommendation import recommend_product
from backend.agents.inventory import check_inventory
from backend.agents.payment import process_payment
from backend.agents.fulfillment import create_order


SESSION = {}

def handle_message(session_id, message):
    context = SESSION.get(session_id, {})

    if "formal" in message.lower():
        product = recommend_product("formal")
        context["product"] = product
        SESSION[session_id] = context
        return f"I recommend {product['name']} priced at ₹{product['price']}. Shall I check availability?"

    if "available" in message.lower() or "kolkata" in message.lower():
        product = context.get("product")
        store = check_inventory(product["sku"])
        return f"Available at {store}. Would you like to reserve it?"

    if "reserve" in message.lower():
        payment = process_payment(context.get("product"))
        order = create_order(context.get("product"))
        return f"✅ Order Confirmed! Order ID: {order}. Payment: {payment}"

    return "How can I assist you with your shopping today?"
