import curses
import scenes

scene_map = scenes.return_all()

def main(stdscr, scene):

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    header = scene['header']
    body = scene['body']
    # options = [option[0] for option in scene['options']]
    options = scene['options']

    chosen_option = 0
    highlighted_option_index = 0

    # while enter hasn't been clicked
    while chosen_option != 10:
        stdscr.erase()
        if len(header) > 0:
            stdscr.addstr(f'\n                      ---{header}--- \n\n', curses.A_DIM)

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
        # if you press the down key and the highlighted option is not at the bottom of the list move down
        # if you press the up key, and the highlighted is not at the top of the list move up  
        chosen_option = stdscr.getch()
        if chosen_option == curses.KEY_UP and highlighted_option_index > 0:
            highlighted_option_index -= 1
        elif chosen_option == curses.KEY_DOWN and highlighted_option_index < len(options) - 1:
            highlighted_option_index += 1

    return highlighted_option_index


choice = curses.wrapper(main, scene_map['scene1'])
print(choice)
