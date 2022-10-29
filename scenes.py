import images

ascii_images = images.ascii_collection()

def start_scene():
    return {
        'kult_namecard': ascii_images['kult2'],
        'header': '''
        Welcome to Kult!''',
        'message': '''
        A short text adventure made to be played in < 20 minutes.
        ''',
        'controls': '''
        Controls: 
        > Press enter to continue 
        > Use the up and down keys to navigate options menus''',
        'prompt': '''
        ...continue'''
    }
def intro_scene():
    return [
        '''The government's intelligence service has received reports that followers of the clandestine secret society: Kult av Blåhaj, will soon attempt to enslave humanity with an airborne biotoxin.''',
        
        '''It is unknown where this chemical weapon, if real, is located or who has access to its trigger. The agency has opted to conduct investigations quietly, without tipping off Kult members.''',
        
        # '''It's up to you to infiltrate this nefarious group, learn the truth, and save humanity.''',
        
        '''Analysts have tracked down what they believe to be an active Kult cell; including one member of particular interest due to their apparent prodigal network engineering knowledge.''',
        
        '''The agency now believes that this individual is the most likely of the cell to be trusted with supervising the toxin-release mechanism.''',
        
        '''You have been tasked with entering the residence unseen to find evidence that will stop the Kult.''',
        
        '''You have been given a dossier with the following information:''',
        '''Mail is delivered to the name "L Secord".''',
        '''They have lived in a brick townhouse on 437 Stuart Avenue NW for a year.''',
        '''Finally, they only leave the house once a week, at 9pm each Thursday. They return exactly 20 minutes later... This is your window of opportunity.''',
            

        
        '''Good luck agent''', 
    ]

def end_scene():
    return {
        'kult_namecard': ascii_images['kult2'],
        'header': '''
        Thanks for playing Kult!''',
        'message': '''
        This game was made in < 36 hours during Major League Hacking's 
        Agent:Hacker2 Hackathon.''',
        'prompt': '''
        Press enter to quit'''
    }
    
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
                ['find KULT', 'ACTION', 'findKULT'],
                ['find KULT4', 'ACTION', 'findKULT4'],
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
                #VIEWS cannot be marked complete
                # you can view them multiple times
                # doesnt need a completed message message[1]
                'findKULT4': {
                    'name': 'findKULT4',
                    'action': 'VIEW',
                    'message': ['you view a kult', ''],
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
