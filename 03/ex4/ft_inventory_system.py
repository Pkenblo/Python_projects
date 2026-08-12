import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":", 1)
        item_name = parts[0]
        qty_str = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(qty_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    item_count = len(inventory)
    print(f"Total quantity of the {item_count} items: {total_qty}")

    if total_qty > 0:
        for item, qty in inventory.items():
            pct = round((qty / total_qty) * 100, 1)
            print(f"Item {item} represents {pct}%")

        most_item = None
        most_qty = -1
        least_item = None
        least_qty = float("inf")

        for item, qty in inventory.items():
            if qty > most_qty:
                most_qty = qty
                most_item = item
            if qty < least_qty:
                least_qty = qty
                least_item = item

        print(f"Item most abundant: {most_item} with quantity {most_qty}")
        print(f"Item least abundant: {least_item} with quantity {least_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
