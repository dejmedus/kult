scene_name = input("scene name\n")

default_header = input("set scene name as header? y/n\n")

while default_header != 'n' and default_header != 'y':
    default_header = input("set scene name as header? y/n\n")

if default_header == 'n':
    header = input("header\n")
else:
    header = scene_name

scene_name = scene_name.lower()
scene_name = scene_name.replace(" ", "_")

body = input("body\n")

# options ['message', NEXT, 'scene/action Name', isUnlocked]
new_scene = f"""'{scene_name}': {{
        'name': '{scene_name}',
       # 'image': ascii_images['{scene_name}'],
        'image': None,
        'header': '{header}',
        'body': '{body}',
        'can_go_back': False,
        # [objInIv, unlockScene]
        'conditionals': [],
        'options': [
            ['', 'NEXT', '', True],
            ['', 'NEXT', '', True],
            ['', 'ACTION', '', True],
            ['', 'TASK', '', True], 
        ],
        'actions': {{
            '': {{
                'name': '',
                'action': 'ADD_TO_INV',
                'message': ['', ''],
                # 'image': ascii_images[''],
                'image': None,
                'complete': False,
                'unlocks': [],
                'locks': []
            }},
            '': {{
                'action': 'VIEW',
                'message': ['', 'only this'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            }},
            '': {{
                'action': 'TASK',
                'message': ['', ''],
                'answer': '',
                # 'image': ascii_images[''],
                'image': None,
                'complete': False,
                'unlocks': [],
                'locks': []
            }},
        }}
    }},"""

f = open("scenes.py", "a")
f.write(new_scene)
f.close()
