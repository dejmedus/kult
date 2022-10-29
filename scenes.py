
def return_all():
    return {
        'scene1': {
            'header': 'scene 1',
            'body': 'this is the body text',
            'options': [
                ['option A1', 'scene2'],
                ['option B1', 'next_scene'],
                ['option C1', 'next_scene'],
                ['...return', 'prev_scene']
            ]
        },
        'scene2': {
            'header': 'scene 2',
            'body': 'this is the body text',
            'options': [
                ['option A2', 'next_scene'],
                ['option B2', 'next_scene'],
                ['option C2', 'next_scene'],
                ['...return', 'prev_scene']
            ]
        },
    }
