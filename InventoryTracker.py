import sqlite3

def create_inventory_table():
    conn = sqlite3.connect('Inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            quantity INTEGER DEFAULT 0,
            category TEXT,
            price REAL,
            threshold INTEGER DEFAULT 5  # Low-stock alert
        )
    ''')
    conn.commit()
    conn.close()

def add_item(item, quantity, category, price, threshold=5):

    if not item or quantity < 0 or price < 0:
        print("Invalid item data.")
        return False
    
    try:
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO items (item, quantity, category, price, threshold)
            VALUES (?, ?, ?, ?, ?)
        ''', (item, quantity, category, price, threshold))
        conn.commit()
        print(f"Added {quantity}x {item} to inventory")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def restock_item_name(item_name, addQuantity):
    try:
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        # Check if item exists
        cursor.execute("SELECT quantity FROM items WHERE item = ?", (item_name,))
        result = cursor.fetchone()

        if result:
            current_quantity = result[0]
            new_quantity = current_quantity + addQuantity
            cursor.execute("UPDATE items SET quantity = ? WHERE item = ?", (new_quantity, item_name))
            conn.commit()
            print(f"Restocked {item_name}: {current_quantity} → {new_quantity}")
        else:
            print(f"Item '{item_name}' not found in inventory.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def restock_item_by_id(item_id, addQuantity):
    if addQuantity <= 0:
        print("Quantity to restock must be greater than zero.")
        return False

    try:
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        # Fetch current quantity for the item
        cursor.execute("SELECT item, quantity FROM items WHERE id = ?", (item_id,))
        result = cursor.fetchone()

        if result:
            item_name, current_quantity = result
            new_quantity = current_quantity + quantity_to_add

            # Update the item's quantity
            cursor.execute("UPDATE items SET quantity = ? WHERE id = ?", (new_quantity, item_id))
            conn.commit()
            print(f"✅ Restocked '{item_name}': {current_quantity} → {new_quantity}")
            return True
        else:
            print(f"❌ No item found with ID {item_id}")
            return False

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

    finally:
        if conn:
            conn.close()

def remove_item_by_id(item_id):
    try:
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        # Check if item exists
        cursor.execute("SELECT item FROM items WHERE id = ?", (item_id,))
        result = cursor.fetchone()

        if result:
            item_name = result[0]
            cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
            conn.commit()
            print(f"🗑️ Removed '{item_name}' (ID: {item_id}) from inventory.")
            return True
        else:
            print(f"❌ No item found with ID {item_id}")
            return False

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

    finally:
        if conn:
            conn.close()

def remove_item_by_name(item_name):
    try:
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        # Check if the item exists
        cursor.execute("SELECT id FROM items WHERE item = ?", (item_name,))
        result = cursor.fetchone()

        if result:
            cursor.execute("DELETE FROM items WHERE item = ?", (item_name,))
            conn.commit()
            print(f"🗑️ Removed item '{item_name}' from inventory.")
            return True
        else:
            print(f"❌ Item '{item_name}' not found in inventory.")
            return False

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

    finally:
        if conn:
            conn.close()

def view_items():
    try:
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        rows = cursor.fetchall()

        if rows:
            print("📦 Inventory:")
            print("-" * 60)
            for row in rows:
                print(f"ID: {row[0]} | Item: {row[1]} | Qty: {row[2]} | "
                      f"Category: {row[3]} | Price: ${row[4]:.2f} | Threshold: {row[5]}")
        else:
            print("⚠️ Inventory is empty.")

        return rows

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

    finally:
        if conn:
            conn.close()