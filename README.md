# Multi language rock/scissors/paper game!
Our motto is play rock/scissors/paper in your native language!
(Provided that your language supported by terminal unlike Persian 😑)

# Run game
NOTE: Terminal used to refer to CMD or Console or command prompt

To run the game first install Python programming language.

Python is installed on Ubuntu by my experience (When you can't speak English as well I promise you nobody wants bother you)
but if python don't installed in you system visit <https://python.org> and acquire python last version.

Then open terminal and go to where you cloned this repository.

as you are in GNU/Linux put following command in terminal if python installed as `python3`:
```
./game.py
```
else if you are not in GNU/Linux or python do not installed as `python3` put python name in a variable called `PYTHON`. Python name is often `python`|`py`|`python3`:
```
PYTHON=python3 # for me it is python3
$PYTHON game.py
```

# set for your language
Check lines 5 to 20 and change following variables
```
R"""Define alternative of following objects
in a particular language. Perisan by default
"""
rock = "سنگ"
paper = "کاغذ"
scissors = "قیچی"
selections = [rock, paper, scissors]

r"""Define alternative of game states (
equal,user won, system won) in a specifc
language. Persian by default
"""
user_won = "کاربر برد"
system_won = "سیستم برد"
equal_wonno = "برابر"
```
to your language substitute.
$acute{a}$

TODO
=====
- [ ] Ranking system
