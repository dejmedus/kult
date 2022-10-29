import images

ascii_images = images.ascii_collection()

def return_all():
    return {
        'scene1': {
            'name': 'scene1',
            'image': ascii_images['scene1'],
            'header': 'scene 1',
            'body': 'this is the body text',
            'options': [
                ['option A1(s2)', 'NEXT', 'scene2'],
                ['option B1(s3)', 'NEXT', 'scene3'],
                ['act:findKULT', 'ACTION' 'findKult'],
                ['option C1(e)', 'NEXT', 'END'],
            ],
            'actions': {
                # display image and message, add to inventory
                'findKULT': {
                    'name': 'findKULT',
                    'action': 'ADD_TO_INV',
                    'message': ['add kult1 to inventory', 'you found a findKULT here previously'],
                    'image': ascii_images['kult1'],
                    'complete': False
                },
                # display image and message
                'findKULT4': {
                    'name': 'findKULT4',
                    'action': 'VIEW',
                    'message': ['you view a kult',],
                    'image': ascii_images['kult4'],
                    'complete': False
                },
                # display image and message, open window, complete task
                # close window receive prize (move to a new scene/add obj to inventory)
                'puzzleExample': {
                    'name': 'puzzleExample',
                    'action': 'TASK',
                    'message': ['TASK: task instructions','you discovered a secret TASKPRIZE'],
                    'image': ascii_images['kult4'],
                    'func': '!!!!!!!WINDOW HERE!!!!!!',
                    'complete': False
                },
            },
        },
        'scene2': {
            'name': 'scene2',
            'image': ascii_images['kult2'],
            'header': 'scene 2',
            'body': 'this is the body text',
            'options': [
                ['option A2(s3)', 'NEXT', 'scene3'],
                ['option B2(s3)', 'NEXT', 'scene3'],
                ['option C2(e)', 'NEXT', 'END'],
                # ['go back to scene1', 'RETURN' 'scene2']
            ],
            'actions': {'action' : '2'}
        },
        'scene3': {
            'name': 'scene3',
            'image': None,
            'header': 'scene 3',
            'body': 'this is the body text',
            'options': [
                ['option A2(e)''NEXT', 'END'],
                ['option B2(e)''NEXT', 'END'],
                ['option C2(e)''NEXT', 'END'],
            ],
            'actions': {'action' : '3'}
        },
    }
