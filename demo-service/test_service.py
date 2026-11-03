from service import Cart, CartItem, process_checkout, calculate_total

def test_standard_checkout():
    cart = Cart(
        cart_id="cart_101",
        user_id="user_55",
        items=[
            CartItem(item_id="prod_1", name="Switch AI License", price=100.0, quantity=2)
        ]
    )
    result = process_checkout(cart)
    assert result["status"] == "success"
    assert result["total_amount"] == 200.0

def test_checkout_with_coupon():
    cart = Cart(
        cart_id="cart_102",
        user_id="user_60",
        items=[
            CartItem(item_id="prod_1", name="Switch AI License", price=100.0, quantity=1)
        ],
        coupon_code="INVALID_PROMO"  # Triggers the bug!
    )
    result = process_checkout(cart)
    assert result["status"] == "success"

if __name__ == "__main__":
    import sys
    try:
        print("Running test_standard_checkout...")
        test_standard_checkout()
        print("PASS: test_standard_checkout")
        print("\nRunning test_checkout_with_coupon...")
        test_checkout_with_coupon()
        print("PASS: test_checkout_with_coupon")
    except Exception as e:
        print(f"\nCRITICAL FAILURE: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
