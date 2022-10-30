inventory = {}

def format_inv():
    inv_str = ''
    for i in inventory:
        inv_str += f' {i} '
    return inv_str

def get_inv():
    return inventory

# if add is True, add new obj to inv, else delete
def manage_inv(obj, add):
    if add:
        inventory[obj] = obj
    else:
        # if we drop the item, the action of picking it up has still happened
        # and so action['complete'] remains true
        inventory.pop(obj)

    return inventory
