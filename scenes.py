import images

ascii_images = images.ascii_collection()


def start_scene():
    return {
        'kult_namecard': ascii_images['kult2'],
        'header': '''
                        Welcome to Kult!''',
        'message': '''
        A short text adventure made for the Major League  Hacking Agent:Hacker 2 Hackathon! View on Github: dejmedus/kult.
        ''',
        'controls': '''
        Controls:
        Please resize your terminal window to 80x20.
        > Press enter to continue
        > Use the up and down keys to navigate options
        menus''',
        'prompt': '''
        ...continue'''
    }


def intro_scene():
    return [
        '''
        The government's intelligence service has received reports that followers of the clandestine secret society: Kult av Blåhaj, will soon attempt to enslave humanity with an airborne biotoxin.''',

        '''
        It is unknown where this chemical weapon, if real, is located or who has access to its trigger. The agency has opted to conduct investigations quietly, without tipping off Kult members.''',

        # '''It's up to you to infiltrate this nefarious group, learn the truth, and save humanity.''',

        '''
        Analysts have tracked down what they believe to be an active Kult cell; including one member of particular interest due to their apparent prodigal network engineering knowledge.''',

        '''
        The agency now believes that this individual is the most likely of the cell to be trusted with supervising the toxin-release mechanism.''',

        '''
        You have been tasked with entering the residence unseen to find evidence that will stop the Kult.''',

        '''
        You have been given a dossier with the following information:''',

        '''
        Mail is delivered to the name "L Secord".''',
        '''
        They have lived in a one-bedroom bungalow on 437 Stuart Avenue NW for a year.''',
        '''
        Finally, they only leave the house once a week, at 9pm each Thursday. They return exactly 20 minutes later... This is your window of opportunity.''',

        '''
        Good luck agent''',
    ]


def end_scene():
    return {
        'kult_namecard': ascii_images['kult2'],
        'header': '''
                        Thanks for playing Kult!''',
        'message': '''
        This game was made in < 36 hours during Major League Hacking's Agent:Hacker2 Hackathon.''',
        'prompt': '''
        Press enter to quit'''
    }


def return_all():
    return {
        'street': {
            'name': 'street',
            # 'image': ascii_images['street'],
            'image': None,
            'header': 'Stuart Avenue. 8:58pm. Thursday, Oct 8th.',
            'body': 'In a few minutes, if everything goes to plan, the suspect will leave their home. Will you follow them?',
            'can_go_back': False,
            'conditionals': [],
            'options': [
                # message, ACTION, next scene, is unlocked
                ['Yes', 'ACTION', 'follow', True],
                ['No', 'NEXT', 'front_door', True],
            ],
            'actions': {
                'follow': {
                    'name': 'follow',
                    'action': 'VIEW',
                    'message': ['', 'You walk in the direction the Kult member left in. However, when you turn the corner you find the street empty. They dodged you. You should try the house.'],
                    # 'image': ascii_images[''],
                    'image': None,
                    'complete': True,
                    'unlocks': [],
                    'locks': ['follow']
                },
            }
        },
        'front_door': {
            'name': 'front_door',
            # 'image': ascii_images['front_door'],
            'image': None,
            'header': 'Front Door',
            'body': 'Its now or never. Find a way into the house that will not raise the alarm.',
            'can_go_back': True,
            'conditionals': [],
            'options': [
                    ['Break window', 'ACTION', 'break_window', False],
                    ['Enter the house', 'NEXT', 'entry_way', False],
                    ['Look around the front yard.', 'ACTION', 'search_yard', True],
                    ['Examine the lock', 'ACTION', 'pick_lock', True],
            ],
            'actions': {
                'search_yard': {
                    'name': 'rock',
                    'action': 'ADD_TO_INV',
                    'message': ['In the overgrown flowerbed you find a large rock', 'You found a rock here. There doesnt seem to be anything else of interest.'],
                    # 'image': ascii_images['search_yard'],
                    'image': None,
                    'complete': False,
                    'unlocks': ['break_window'],
                    'locks': ['search_yard']
                },
                'break_window': {
                    'action': 'VIEW',
                    'message': ['', 'The living room window is within reach, but as you move to break it you notice a blinking red light visible through the glass. An alarm system.  This reminds you that you need to be sneaky. You will have to find another way in.'],
                    # 'image': ascii_images['rock'],
                    'image': None,
                    'complete': True,
                    'unlocks': [],
                    'locks': ['break_window']
                },
                'pick_lock': {
                    'action': 'TASK',
                    'message': ['The lock seems of average make. Surprising for a cultists home. Picking it might be the best option. You determine the lock has three tumblers. Hitting a tumbler toggles it. Hitting the first or third also toggles the second.  The third must be hit last. Which order do you hit the tumblers? Answer: pin numbers in the order you will hit them', 'You expertly picked the lock in the order 123. Now you can enter the house.'],
                    # 1: YYN 2: YNN 3: YYY
                    'answer': '123',
                    # 'image': ascii_images['rock'],
                    'image': None,
                    'complete': False,
                    'unlocks': ['entry_way'],
                    'locks': ['pick_lock']
                },
            }
        },

'entry_way': {
        'name': 'entry_way',
       # 'image': ascii_images['entry_way'],
        'image': None,
        'header': 'Entry Way',
        'body': 'Youre in. But the Kultist isnt going to make this easy for you.The alarm beside the door begins to beep. You have 30 seconds to disable the alarm before it sounds.',
        'can_go_back': False,
        'conditionals': [['rock', 'smash'], ],
        'options': [
            ['Smash it with a rock', 'ACTION', 'smash', False],
            ['Explore the house', 'NEXT', 'the_kultists_lair', False],
            ['Youre a spy! Use the signal jammer.', 'ACTION', 'jammer', True],
        ],
        'actions': {
            'smash': {
                'action': 'VIEW',
                'message': ['', 'Its bright. Its loud. Its in your way of saving the WHOLE WORLD. Smashing it would be awesome, but it would get you caught... and possibly fired. Find a different way.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': ['smash']
            },
            'jammer': {
                'action': 'TASK',
                'message': ['To successfully use the jammer you must first determine the correct frequency. It is a number between 100 and 300. The last two digits are the same. You get the strange feeling that a computer would understand these two numbers.', 'You determined the frequency to be 100 and jammed the alarm system. Now you can explore the house.'],
                'answer': '100',
                # 'image': ascii_images[''],
                'image': None,
                'complete': False,
                'unlocks': ['the_kultists_lair'],
                'locks': ['smash', 'jammer']
            },
        }
    },
'the_kultists_lair': {
        'name': 'the_kultists_lair',
       # 'image': ascii_images['the_kultists_lair'],
        'image': None,
        'header': 'The Kultists Lair',
        'body': 'Now that the danger of discovery has passed you can look around without distractions. To the right is a small kitchen. To the left ais a living room devoid of furniture except for a recliner, a television, and some wall art. Ahead is two doors, one of which must lead to the bedroom.',
        'can_go_back': False,
        'conditionals': [],
        'options': [
            ['Go into the kitchen', 'NEXT', 'kitchen', True],
            ['Go into the living room', 'NEXT', 'livingroom', True],
            ['Go into the bedroom', 'NEXT', 'bedroom', True],
        ],
        'actions': {}
    },
    'kitchen': {
        'name': 'kitchen',
       # 'image': ascii_images['kitchen'],
        'image': None,
        'header': 'Kitchen',
        'body': 'The kitchen is spotless. The counters are empty save for a fruit bowl and what looks like a row of cook books. On the fridge, a color photograph of a shark and a an old grocery receipt are held on by magnets.',
        # [objInIv, unlockScene]
        'can_go_back': True,
        'conditionals': [['rock', 'plates']],
        'options': [
            ['Examine the fruit bowl', 'ACTION', 'fruitbowl', True],
            ['Look at the photograph', 'ACTION', 'photo', True],
            ['Read the grocery receipt', 'ACTION', 'receipt', True],
            ['Page through the cook books', 'ACTION', 'cookbooks', True],
            ['Smash all the plates with the rock', 'ACTION', 'plates', False],
        ],
        'actions': {
            'fruitbowl': {
                'action': 'VIEW',
                'message': ['', 'Apples and oranges sit in a white bowl. They are shiny and seemingly very fresh. There is nothing else in the bowl.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
            'photo': {
                'action': 'VIEW',
                'message': ['', 'A glossy photo of a shark jumping out of the water, jaws open. It is held up by a magnet shaped like a cat... or maybe an orca, its hard to tell.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
            'receipt': {
                'action': 'VIEW',
                'message': ['', ' '],
                'image': ascii_images['receipt'],
                # 'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
            'cookbooks': {
                'action': 'VIEW',
                'message': ['', 'The hardback cookbooks sit in a neat row. Upon perusal you find they are all empty except for one book. In it, someone has noted what seems to be the recipe for a cheese sandwich. It reads as follows: bread cheese bread'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
             'plates': {
                'action': 'VIEW',
                'message': ['', '...weve talked about this.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
        }
    },'living_room': {
        'name': 'living_room',
       # 'image': ascii_images['living_room'],
        'image': None,
        'header': 'Living Room',
        'body': 'Teh living room is sparse, but cozy. An overstuffed recliner sits facing a television. The walls feature abstract art and a poster you would expect to see at a science fair.',
        'can_go_back': True,
        # [objInIv, unlockScene]
        'conditionals': [],
        'options': [
            ['Search the recliner', 'ACTION', 'recliner', True],
            ['Look at the art', 'ACTION', 'art', True],
            ['Examine the television', 'ACTION', 'tv', True],
        ],
        'actions': {
            'tv': {
                'action': 'VIEW',
                'message': ['', 'The television looks new and quite expensive. When you try to turn it on you discover that the power cord has been cut.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': False,
                'unlocks': [],
                'locks': []
            },
            'recliner': {
                'action': 'VIEW',
                'message': ['', 'The brown recliner is worn at the edges. It is one of the few things in the house that looks like it is used regularly. The only thing you can find within is a lost pack of gum.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
            'art': {
                'action': 'VIEW',
                'message': ['', 'The oil paintings are beautiful, but feel somehow staged. Oddly, the most prominently placed wall hanging is a large poster emblazoned with the words "The blue shark can swim very far, dive really deep and hear noises from almost 250 metres away."'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
        }
    },
    'bedroom': {
        'name': 'bedroom',
       # 'image': ascii_images['bedroom'],
        'image': None,
        'header': 'Bedroom',
        'body': 'The bedroom is utilitarian. The walls and curtains are a dull white. It features a perfectly made bed, a dresser, and a nightstand. It reminds you of a hotel.',
        'can_go_back': True,
        # [objInIv, unlockScene]
        'conditionals': [],
        'options': [
            ['Look under the bed', 'ACTION', 'bed', True],
            ['Check the nightstand', 'ACTION', 'nightstand', True],
            ['Search the dresser', 'ACTION', 'dresser', True],
            ['Descend into the secret room', 'ACTION', 'secret', False],
        ],
        'actions': {
            'bed': {
                'action': 'VIEW',
                'message': ['', 'You carefully run your hands along the blankets, but feel nothing out of the ordinary. The floor beneath is empty save for dust bunnies. Lifting the mattress reveals nothing.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
            'dresser': {
                'action': 'VIEW',
                'message': ['', 'Neatly folded clothing greets you when you open the dresser drawers. You carefully search through them one stack at a time, but turn up nothing. It wasnt a complete waste of time, you now know that cult members favour cashmere.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
            'nightstand': {
                'action': 'VIEW',
                'message': ['', 'The nightstand seems like a fairly reasonable place to hide criminal documents. On your way over to check it out you trip over a previously out of sight, and incredibly orange, rug. The corner of the rug has shifted to reveal the outline of a hatch.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': ['secret'],
                'locks': []
            },
        }
    },
    'secret': {
        'name': 'secret',
       # 'image': ascii_images['secret'],
        'image': None,
        'header': 'The Inner Sanctum',
        'body': 'The bottom the ladder is dark except for the illumination of a dozen computer monitors anchored to the wall. The space hosts a single bed, a kitchenette, and a door set ajar leading to a small bathroom. A desk takes up most of the space. To the side of the desk sits a large black combination safe.',
        'can_go_back': True,
        # [objInIv, unlockScene]
        'conditionals': [],
        'options': [
            ['Search the desk', 'ACTION', 'desk', True],
            ['Leave with the evidence and save humanity', 'NEXT', 'good', False],
            ['Remain and become a card-carrying member of the Kult av Blåhaj', 'NEXT', 'kult', False],
            ['Read the documents', 'ACTION', 'documents', False], 
            ['Try to crack the safe', 'TASK', 'safe', True], 
        ],
        'actions': {
            'desk': {
                'action': 'VIEW',
                'message': ['', 'Various coffee cups and rubber ducks occupy a large portion of the desks surface. Scrap paper with vague drawings of blue hamsters are strewn around. The monitors display a log in screen, but you doubt youd be able to access the computer in your limited time.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': [],
                'locks': []
            },
            'safe': {
                'action': 'TASK',
                'message': ['You get the feeling that this safe is your last chance to find evidence that will stop the Kult. It requires a 6 digit combination. Have any numbers stuck out while exploring the house?', 'You cracked the safe with the code 250242. Now you just need to decide what to do with this knowledge.'],
                'answer': '250242',
                # 'image': ascii_images[''],
                'image': None,
                'complete': False,
                'unlocks': ['documents'],
                'locks': []
            },
            'documents': {
                'action': 'VIEW',
                'message': ['', 'You find stacks of documents inside the safe. They detail the Kult av Blåhajs plans to disburse a mind controlling toxin into the population in order to empower the entity they call Blåhaj. These documents contain everything the Agency will need to stop the plot.'],
                # 'image': ascii_images[''],
                'image': None,
                'complete': True,
                'unlocks': ['END', 'newfriends'],
                'locks': ['safe']
            },
        }
    },
    'kult': {
        'name': 'kult',
       # 'image': ascii_images['kult'],
        'image': None,
        'header': 'Become The Newest Devotee',
        'body': 'Now that you understand the great power and wonder of Blåhaj, you cant fathom returning  to your mundane life of espionage! You will use your skills to help your new Kult brethren. It doesnt matter that you are a government employee who has broken into one of their homes, they will totally understand.',
        'can_go_back': False,
        # [objInIv, unlockScene]
        'conditionals': [],
        'options': [
            ['Follow Blåhaj', 'NEXT', 'END', True],
        ],
    },
    'good': {
        'name': 'good',
       # 'image': ascii_images['good'],
        'image': None,
        'header': 'In Hopes of a Raise',
        'body': 'The Kult isnt going to succeed on your watch. Your job is busy enough without a over-lord controlling the earth. The higher-ups will be pleased to know you saved the world and displayed unquestionable professionalism while doing it. No indiscriminate smashing of windows, alarms, or plates here. You deserve a raise and a vacation.',
        'can_go_back': False,
        # [objInIv, unlockScene]
        'conditionals': [],
        'options': [
            ['Just another days work', 'NEXT', 'END', True],
        ],
    },
}