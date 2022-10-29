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
                ['option A1(s2)', 'scene2'],
                ['option B1(s3)', 'scene3'],
                ['option C1(e)', 'END'],
            ],
            'actions': {
                # action, message, 
                # pick_up(message, obj name, obj image)
                # display message and image, add image name to inventory
                'findKULT': {
                    'name': 'findKULT',
                    'add_to_inv': True,
                    'message': 'you have found a WILD KULT',
                    'image': ascii_images['kult1']
                },
                'findOTHERKULT': {
                    'name': 'findKULT4',
                    'add_to_inv': False,
                    'message': 'you see a KULT staring at you out of the corner of your eye',
                    'image': ascii_images['kult4']
                }
                
            },
        },
        'scene2': {
            'name': 'scene2',
            'image': ascii_images['kult2'],
            'header': 'scene 2',
            'body': 'this is the body text',
            'options': [
                ['option A2(s3)', 'scene3'],
                ['option B2(s3)', 'scene3'],
                ['option C2(e)', 'END'],
            ]
        },
        'scene3': {
            'name': 'scene3',
            'image': 'NONE',
            'header': 'scene 3',
            'body': 'this is the body text',
            'options': [
                ['option A2(e)', 'END'],
                ['option B2(e)', 'END'],
                ['option C2(e)', 'END'],
            ]
        },
    }
