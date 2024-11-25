import pickle

# Simulated database to store serialized data
user_cart_db = {}

def save_cart(user_id, cart):
    """
    Save the user's cart to the database using pickle.
    This code does not validate or sanitize the serialized data, making it vulnerable.
    """
    serialized_cart = pickle.dumps(cart)
    user_cart_db[user_id] = serialized_cart
    print(f"Cart saved for user {user_id}.")

def load_cart(user_id):
    """
    Load the user's cart from the database.
    This code uses pickle.loads without validation, leading to a vulnerability.
    """
    serialized_cart = user_cart_db.get(user_id)
    if not serialized_cart:
        print(f"No cart found for user {user_id}.")
        return None
    # Insecure usage of pickle.loads
    cart = pickle.loads(serialized_cart)
    print(f"Cart loaded for user {user_id}: {cart}")
    return cart

# Simulating an attacker injecting malicious pickled data
def simulate_attack():
    """
    Demonstrates how an attacker could inject malicious pickled data.
    """
    malicious_data = pickle.dumps(eval("lambda: __import__('os').system('echo Hacked!')"))
    user_cart_db["attacker"] = malicious_data
    print("Malicious data injected into the database.")

if __name__ == "__main__":
    # Save a legitimate user's cart
    save_cart("user1", {"items": ["item1", "item2"], "total": 200})
    load_cart("user1")

    # Simulate an attack
    simulate_attack()

    # Attempt to load the attacker's cart (executes malicious code)
    load_cart("attacker")
