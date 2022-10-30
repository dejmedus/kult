## Hello Agent 🕵️

#### The Agency has received reports that followers of the clandestine secret society: Kult av Blåhaj, will soon attempt to enslave humanity with an airborne toxin meant to control minds.

#### It's up to you to infiltrate this nefarious group, learn the truth, and save humanity.

Kult is a micro text adventure created for the Major League Hacking Agent:Hacker 2 Hackathon.
It was built with Python (3.10.3) and the curses module. It runs in the terminal window.

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

These two StackOverflow questions & answers pointed me towards the curses package. The options menu is adapted from the second.
- [How do I print colored text to the terminal](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
- [How to make a menu in python with arrow keys](https://stackoverflow.com/questions/39488788/how-to-make-a-menu-in-python-navigable-with-arrow-keys)

List comprehension: [docs.python](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

Curses Module: [docs.python](https://docs.python.org/3/library/curses.html#module-curses.textpad)
