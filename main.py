import curses
from sys import stderr

import scenes
import inventory_helper

inventory = inventory_helper.get_inv()
scene_map = scenes.return_all()
# end_message = 'Thanks for playing!'

def main(stdscr, scene, inventory):

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    image = scene['image']
    header = scene['header']
    body = scene['body']
    options = scene['options']
    actions = scene['actions']
    # will there be a time when a scene doesn't have any actions?
    # actions = scene.get('actions', None)
    
    chosen_option = 0
    highlighted_option_index = 0

    # while enter hasn't been clicked
    while chosen_option != 10:
        stdscr.erase()
        
        if inventory:
            stdscr.addstr(f'inventory: {inventory_helper.format_inv()}\n\n')
        else:
            stdscr.addstr('inventory: \n\n')
        
        if image != None:
            stdscr.addstr(image)
        
        if len(header) > 0:
            stdscr.addstr(f'\n\n                      ---{header}--- \n\n', curses.A_DIM)

        stdscr.addstr(f'    {body}\n',  curses.A_BOLD)

        for i in range(len(options)):
            # if the cursor is currently on this option, highlight it
            if i == highlighted_option_index:
                option_color = curses.color_pair(2)
            else:
                option_color = curses.color_pair(1)
            stdscr.addstr(f'    {i + 1}. ')
            stdscr.addstr(f'{options[i][0]}\n', option_color)

        # by default, the highlighted option is options[0][0] (shown as top of list)
        # if you press the down key and the highlighted option is not at the bottom of the list move down (up is opposite)
        chosen_option = stdscr.getch()
        if chosen_option == curses.KEY_UP and highlighted_option_index > 0:
            highlighted_option_index -= 1
        elif chosen_option == curses.KEY_DOWN and highlighted_option_index < len(options) - 1:
            highlighted_option_index += 1

    # when enter is clicked get the option chosen from arrow menu options
    # get option_type from option[1]. One of:
    # NEXT (next scene), ACTION (view, add_to_inv, or task), RETURN (prev scene)
    option = options[highlighted_option_index]
    option_type = option[1]
    
    # if NEXT, get next scene
    if option_type == 'NEXT':
        next_scene = option[2]
        
        # display end message if END is reached
        if next_scene == 'END':
            stdscr.erase()
            stdscr.addstr('\n\n\n               Thanks for playing! Press enter to quit.')
            wait_for_enter(stdscr)
        
        # else next_scene is a named scene   
        # set the next scene's return instructions and move forward to that scene [option[2]]
        else:
            # return_message = f"return to {scene['name']}"
            # scene_map[next_scene]['options'].append([return_message, 'RETURN', scene['name']])
            scene_map[next_scene]['options'].append(['go back', 'RETURN', scene['name']])
            
            curses.wrapper(main, scene_map[next_scene], inventory)
            
    # if RETURN, remove current return instructions (options[-1]) 
    # then go back to previous scene [option[2]]
    elif option_type == 'RETURN':
        options.pop()

        # option[2] is the previous scenes dict key/name
        curses.wrapper(main, scene_map[option[2]], inventory)
            
    elif option_type == 'ACTION':
        stdscr.erase()
        action = actions[option[2]]
        # if action is not completed
        # complete action (add to inv, view something, a task) 
        if action['complete'] == False:
            # display image and message[0], add to inventory, set complete to TRUE
            if action['action'] == 'ADD_TO_INV':
                stdscr.addstr(f"{action['image']}\n")
                stdscr.addstr(f"\n  {action['message'][0]}") 
                inventory_helper.manage_inv(action['name'], True)
                action['complete'] = True    
            
            # display image and message[0], can be viewed again, 'complete' remains false
            elif action['action'] == 'VIEW':
                stdscr.addstr(f"{action['image']}\n")
                stdscr.addstr(f"\n  {action['message'][0]}") 

            # elif action['action'] == 'TASK':
            #     display image and message, open window, complete task
            #     close window receive prize (move to a new scene/add obj to inventory)
            else:
                error_finder(stdscr, f"action['action'] error {action['action']}")
    
        #if action is completed, display completed message
        elif action['complete'] == True:
                stdscr.addstr(f"\n\n  {action['message'][1]}") 
        else: 
            error_finder(stdscr, f"action['complete'] error {action['complete']}")
            
        # return to current scene after finishing action
        wait_for_enter(stdscr)
        curses.wrapper(main, scene_map['scene1'], inventory)
    
    else:
        error_finder(stdscr, f'option_type error {option} {option_type}')
      
# def start_screen(stdscr):
#     stdscr.erase()
# #     stdscr.addstr(f,  curses.A_BOLD)
#     # start the game!
#     # curses.wrapper(main, scene_map['scene1'], inventory)
# curses.wrapper(start_screen)

def wait_for_enter(stdscr):
    key_press = stdscr.getch()
    while key_press != 10:
        key_press = stdscr.getch()
        
def error_finder(stdscr, message):
    stdscr.erase()
    stdscr.addstr(message)
    wait_for_enter(stdscr)
        
        

# start the game!
curses.wrapper(main, scene_map['scene1'], inventory)
