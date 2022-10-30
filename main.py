import curses
from curses.textpad import Textbox
import textwrap

import scenes
import inventory_helper

inventory = inventory_helper.get_inv()
scene_map = scenes.return_all()

start_message = scenes.start_scene()
end_message = scenes.end_scene()
intro = scenes.intro_scene()


def main(stdscr, scene, inventory):

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    image = scene['image']
    header = scene['header']
    body = scene['body']

    # if option is unlocked (includes True), list it as an option
    all_options = scene['options']
    
    # if the scene has conditionals, unlock those scenes
    if scene['conditionals']:
        for conditional in scene['conditionals']:
            conditional_object = conditional[0]
            conditional_scene = conditional[1]
            # if conditional_object is in inventory, find conditional scene and unlock it
            if conditional_object in inventory:
                option_to_unlock = [option for option in all_options if conditional_scene in option]
                option_to_unlock[0][3] = True
        
    options = [option for option in all_options if True in option]
    
    # will there be a time when a scene doesn't have any actions?
    actions = scene.get('actions', None)

    chosen_option = 0
    highlighted_option_index = 0

    # while enter hasn't been clicked
    while chosen_option != 10:
        # clear screen and display inventory
        reset_screen(stdscr, inventory)

        if image != None:
            stdscr.addstr(image)

        if len(header) > 0:
                format_centered_text(stdscr, header)

        stdscr.addstr(f'    {format_text(body)}\n\n',  curses.A_BOLD)

        for i in range(len(options)):
            # if the cursor is currently on this option, highlight it
            if i == highlighted_option_index:
                option_color = curses.color_pair(2)
            else:
                option_color = curses.color_pair(1)
            stdscr.addstr(f'    {i + 1}. ')
            # if last option, don't add newline
            if i != len(options) - 1:
                stdscr.addstr(f'{format_text(options[i][0])}\n', option_color)
            else:
                stdscr.addstr(f'{format_text(options[i][0])}', option_color)

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
            stdscr.addstr(f"{end_message['kult_namecard']}\n\n")
            stdscr.addstr(f"{end_message['header']}\n\n", curses.A_BOLD)
            stdscr.addstr(f"{format_text(end_message['message'])}\n\n")
            stdscr.addstr(f"{end_message['prompt']}")
            wait_for_enter(stdscr)

        # else next_scene is a named scene
        # if can_go_back, set the next scene's return instructions and move forward to that scene [option[2]]
        else:
            if scene_map[next_scene]['can_go_back'] == True:
                scene_map[next_scene]['options'].append(['go back', 'RETURN', scene['name'], True])

            curses.wrapper(main, scene_map[next_scene], inventory)

    # if RETURN, remove current return instructions (options[-1])
    # all_options and not options, because options is a generated copy of all_options
    # all_options is the true scene['options']
    # then go back to previous scene [option[2]]
    elif option_type == 'RETURN':
        all_options.pop()

        # option[2] is the previous scenes dict key/name
        curses.wrapper(main, scene_map[option[2]], inventory)

    elif option_type == 'ACTION':
        reset_screen(stdscr, inventory)
        action = actions[option[2]]
        # if action is not completed
        # complete action (add to inv, view something, a task)
        if action['complete'] == False:
            # display image and message
            if action['image'] != None:
                stdscr.addstr(f"{action['image']}\n")
                
            stdscr.addstr(f"\n      {format_text(action['message'][0])}")
            
            # display image and message[0], add to inventory, set complete to TRUE
            if action['action'] == 'ADD_TO_INV':
                inventory_helper.manage_inv(action['name'], True)
                action['complete'] = True

            # can be viewed again, 'complete' remains false
            # elif action['action'] == 'VIEW':

            elif action['action'] == 'TASK':

                # draw input box the same size as the answer
                window = curses.newwin(1, len(action['answer']) + 1, 15, curses.COLS // 2 - 10,)
                textbox = Textbox(window)
                stdscr.refresh()
                textbox.edit()
                answer = textbox.gather()
                # 
                answer = answer[:-1]

                reset_screen(stdscr, inventory)
                # if task is completed action['complete'] = True
                if answer == action['answer']:
                    action['complete'] = True
                    stdscr.addstr(f"\n\n        {format_text('Correct!')}")
                else:
                    stdscr.addstr(f"\n\n        {format_text('Your answer was incorrect.')}")

            else:
                error_finder(stdscr, f"action['action'] error {action['action']}")
            
        # if action is completed, display completed message
        elif action['complete'] == True:
            stdscr.addstr(f"\n\n        {format_text(action['message'][1])}")
        else:
            error_finder(
                stdscr, f"action['complete'] error {action['complete']}")
            
        # if action has unlocked a scene
        # find option with scene to be unlocked and set to True
        if action['complete'] and action['unlocks']:
            for unlock in action['unlocks']:
                option_to_unlock = [option for option in all_options if unlock in option]
                # access [0] because list comprehension returns a list
                option_to_unlock[0][3] = True
                
        # if action has locked a scene
        if action['complete'] and action['locks']:
            for lock in action['locks']:
                option_to_lock = [option for option in all_options if lock in option]
                # access [0] because list comprehension returns a list
                option_to_lock[0][3] = False
            
                # if conditional scene is locked, remove it from conditionals
                if scene['conditionals']:
                    for conditional in scene['conditionals']:
                        conditional_scene = conditional[1]
                        
                         # if the conditional scene is the one we want to lock
                         # get the conditional [obj, scene] pair and use them 
                         # to remove from conditional from conditionals list
                        if conditional_scene == option_to_lock[0][2]:
                            conditional_object = conditional[0]
                            conditional_scene = conditional[1]
                            scene['conditionals'].remove([conditional_object, conditional_scene])
            
        # return to current scene after finishing action
        wait_for_enter(stdscr)
        curses.wrapper(main, scene_map[scene['name']], inventory)

    else:
        error_finder(stdscr, f'option_type error {option} {option_type}')


def wait_for_enter(stdscr):
    key_press = stdscr.getch()
    while key_press != 10:
        key_press = stdscr.getch()


def error_finder(stdscr, message):
    stdscr.erase()
    stdscr.addstr(message)
    wait_for_enter(stdscr)


def format_text(text):
    return textwrap.fill(text, width=70, subsequent_indent='      ')

def format_centered_text(stdscr, text):
    text = textwrap.fill(text, width=70, subsequent_indent='      ')
    return stdscr.addstr(4, curses.COLS // 2 - len(text) // 2, f'{text}\n\n', curses.A_DIM)

def reset_screen(stdscr, inventory):
    stdscr.erase()
    if inventory:
        stdscr.addstr(f'inventory: {inventory_helper.format_inv()}\n\n')
    else:
        stdscr.addstr('inventory: \n\n')

# should start screen be a seperate screen or just a scene?


def start_scene(stdscr):
    # # display welcome screen
    # stdscr.erase()
    # stdscr.addstr(f"{start_message['kult_namecard']}\n\n")
    # stdscr.addstr(f"{format_centered_text(stdscr, start_message['header'])}", curses.A_BOLD)
    # stdscr.addstr(f"{start_message['message']}")
    # stdscr.addstr(f"{start_message['controls']}\n\n", curses.A_DIM)
    # stdscr.addstr(f"{start_message['prompt']}")
    # wait_for_enter(stdscr)

    # stdscr.erase()
    # # display intro scene
    # for line in intro:
    #     stdscr.clear()
    #     stdscr.addstr('\n\n\n')
    #     lineArr = textwrap.wrap(line, width=70, subsequent_indent='      ')
    #     for line in lineArr:
    #         stdscr.addstr(f'{line}\n')
    #     wait_for_enter(stdscr)

    # start the game!
    curses.wrapper(main, scene_map['street'], inventory)


curses.wrapper(start_scene)

# start the game!
# curses.wrapper(main, scene_map['scene1'], inventory)
