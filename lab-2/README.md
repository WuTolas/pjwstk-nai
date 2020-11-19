# Pentago

**Rules**: https://en.wikipedia.org/wiki/Pentago  
**Authors**: Damian Rutkowski (s16583), Piotr Krajewski (s17410)

## Example game

https://www.youtube.com/watch?v=FuAkQxNH_Bs

## Environment setup - linux

1. Make sure that you have **python3**, **python3-pip** and **python3-venv** installed
2. Download project, extract it and go to the **lab-2** folder
3. Create virtual environment: `python3 -m venv env`
4. Activate virtual environment: `source env/bin/activate`
5. Install the requirements: `python3 -m pip install -r requirements.txt`

## Playing the game

To run the game, type: `python3 pentago.py`

Game board is made of 4 quadrants, on which you need to place your choices.  
Example moves: 
- `10 3 l` - place choice on position number 10, then rotate 3rd quadrant to the left
- `29 4 r` - place choice on position number 29, then rotate 4th quadrant to the right

Positions on the board:

``` 
 1  2  3 | 10 11 12  
 4  5  6 | 13 14 15  
 7  8  9 | 16 17 18  
--------------------  
19 20 21 | 28 29 30  
22 23 24 | 31 32 33  
25 26 27 | 34 35 36
``` 

## AI

EasyAI has been used to implement AI for this game. AI works but at this moment it's really easy to
beat it (search depth is set to 3 - for higher values it takes VERY long time to perform the move).

Best possible solution, for increasing the search depth in the algorithm and making it harder to defeat, would be 
solving the game and saving the data containing all the possible situations.

The good news - it is possible to calculate the perfect play for every position.
The bad news - it would take WAY too much time for that. Source: https://perfect-pentago.net/details.html