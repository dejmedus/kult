inventory = {
    # 'dossier': 'dossier'
}

def format_inv():
    inv_str = ''
    for i in inventory:
        inv_str += f' {i} '
                
    return inv_str

def get_inv():
    return inventory

def manage_inv(obj, add):
    # if add is True, add new obj to inv, else delete
    if add:
        # add_to_inv action has now been completed (action['complete'] = True)
        inventory[obj] = obj
    else:
        # if we drop the item, the action of picking it up has still happened
        # and so action['complete'] remains true
        # this would need to change if functionality was needed for putting down and picking back up objects
        inventory.pop(obj)
    return inventory
