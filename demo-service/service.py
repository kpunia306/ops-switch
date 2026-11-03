"""Cart and Checkout Service - Core Order Processing."""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class CartItem:
    item_id: str
    name: str
    price: float
    quantity: int

@dataclass
class Cart:
    cart_id: str
    user_id: str
    items: List[CartItem] = field(default_factory=list)
    coupon_code: Optional[str] = None

COUPONS = {
    "SWITCH20": 0.20,
    "DEVTOOLS10": 0.10,
}

def calculate_total(cart: Cart) -> float:
    subtotal = sum(item.price * item.quantity for item in cart.items)
    
    # Broken logic introduced in v1.2.1:
    # Directly looks up cart.coupon_code in dict without validation
    if cart.coupon_code:
        discount = COUPONS[cart.coupon_code]
        subtotal -= subtotal * discount

    return round(subtotal, 2)

def process_checkout(cart: Cart) -> dict:
    if not cart.items:
        raise ValueError("Cannot checkout empty cart")
    
    total = calculate_total(cart)
    return {
        "status": "success",
        "cart_id": cart.cart_id,
        "total_amount": total,
        "currency": "USD"
    }
