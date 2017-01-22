# The Billionaire's Challenge

Multibillionare Mike McHack has just died, leaving an estate valued at several
million Bitcoin. A lifelong hacker, in his will, he left his entire estate to
the first person who can solve his series of technical challenges.

This is where you come in. As a keen Hacker, you're up to the challenge, and
are itching to begin.

Before we go any further, some rules and information:
- The game is divided into a series of levels, with each level having a particular
  random string key associated with it (Eg.
  `7d97e98f8af710c7e7fe703abc8f639e0ee507c4`). To access a level, append its key to
  the base URL (Eg. http://localhost:5000/7d97e98f8af710c7e7fe703abc8f639e0ee507c4),
- The clues for each level are always sent via HTTP on port 5000
- Each level will lead you to the key for the next one, keep going until you
  reach the end
- The levels will get progressively more and more difficult
- Do not look in the static or challenges directories during or before the game
  (They contain the answers.)
- You may use any web browser or Curl to retrieve information from a URL
- If you're stuck, the level you're on may have a hint (or more than one). You
  can append `/hint/<hint_num>` to the level's URL to view the hint with the
  specified hint number.
  (Eg. http://localhost:5000/7d97e98f8af710c7e7fe703abc8f639e0ee507c4/hint/1)
  to view the first hint.

## Starting the game

Ready to begin? Ensure that you have Python3 and Flask installed, then run.

`python3 main.py`

Then connect to:

`http://localhost:5000/f6fd1656d79b06918bb5cf85c8bae58c3884deaf`

GOODLUCK
