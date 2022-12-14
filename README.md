## Hello Agent 🕵️

#### The Agency has received reports that followers of the clandestine secret society: Kult av Blåhaj, will soon attempt to enslave humanity with an airborne toxin meant to control minds.

#### It's up to you to infiltrate this nefarious group, learn the truth, and save humanity.

Kult is a micro text adventure created for the Major League Hacking Agent:Hacker 2 Hackathon in one weekend.
It was built with Python (3.10.3) and the curses module. It runs in the terminal window and will likely take ~10 minutes to play through.

### Setup

Currently, Kult has only been tested on MacOS. It should run fine on Linux. 

Windows will likely require some extra steps and there may be style and color differences. 

This [article](https://www.devdungeon.com/content/curses-windows-python) recommends installing the [windows-curses package](https://pypi.org/project/windows-curses/).

### To Play the Game
1. Fork the repository
2. Clone your-github-username/kult
3. cd into the directory where you will store the game files
4. Paste clone path into your terminal
5. ```cd kult```
6. ```python3 main.py```
7. Enjoy!

### Game play examples
<details>
<summary>📷</summary>

<img width="625" alt="Living room" src="https://user-images.githubusercontent.com/59973863/198926214-6437b88d-4f2f-44b5-bd37-a38dd0d4dab0.png">
<img width="631" alt="kitchen" src="https://user-images.githubusercontent.com/59973863/198926278-b0217a87-d3fe-4381-8f8f-7635fc760606.png">

</details>

### Walkthrough
This walkthrough contains hints about how to solve the logic puzzles. It also offers the answers.
<details>
<summary>Warning: spoilers</summary>

**Pick the lock:**
- tumbler 1 toggles itself and tumbler 2
- tumbler 2 toggles itself
- tumbler 3 toggles itself and tumbler 2
- tumbler 3 must be hit last

<details>
<summary>Answer</summary>
They begin NNN

1: YYN 2: YNN 3: YYY

Answer: **123**
</details>

**Jam the alarm:**
- the number is between 100 and 300
- the last two digits are the same
- the first is unique
- computers would like these numbers

<details>
<summary>Answer</summary>
Machine language is made up of 0s and 1s

Answer: **100**
</details>

**Open the safe:**
- the safe is a combination lock which needs 6 digits to open 
- there are 3 numbers in the kitchen
- there are 3 numbers in the living room
- you may need to try the combination twice

<details>
<summary>Answer</summary>
The cookbooks provide the recipe for a cheese sandwich (bread cheese bread)

The receipt on the fridge tell us that bread costs $2 and cheese costs $4

The odd poster in the living room features the numbers 250

There are two possible combinations of these 6 numbers 250242 or 242250

As a hint, the photo of the shark is seen before the grocery receipt

Answer: **250242**
</details>
</details>


### Resources that helped me create Kult
I was inspired to create a CLI game by the fantastic [command line murder mystery.](https://github.com/veltman/clmystery)

The title and end page ascii-art was generated with this great [tool](https://ascii-generator.site/t/)

These two StackOverflow questions & answers pointed me towards the curses package. The options menu is adapted from the second.
- [How do I print colored text to the terminal](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
- [How to make a menu in python with arrow keys](https://stackoverflow.com/questions/39488788/how-to-make-a-menu-in-python-navigable-with-arrow-keys)

List comprehensions: [docs.python](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

Curses module: [docs.python](https://docs.python.org/3/library/curses.html#module-curses.textpad)
