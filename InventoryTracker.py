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