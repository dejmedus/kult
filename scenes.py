
def return_all():
    return {
        'scene1': {
            'name': 'scene1',
            'header': 'scene 1',
            'body': 'this is the body text',
            'options': [
                ['option A1(s2)', 'scene2'],
                ['option B1(s3)', 'scene3'],
                ['option C1(e)', 'END'],
            ]
        },
        'scene2': {
            'name': 'scene2',
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
            'header': 'scene 3',
            'body': 'this is the body text',
            'options': [
                ['option A2(e)', 'END'],
                ['option B2(e)', 'END'],
                ['option C2(e)', 'END'],
            ]
        },
    }
