*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     Direction   StartingMoveCount     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     5             4             WEST        18                    4           4           19
Move N the edge of the board        3             0             NORTH       5                     3           0           6
Move S the edge of the board        5             9             SOUTH       14                    5           9           15
Move E the edge of the board        9             3             EAST        7                     9           3           8
Move W the edge of the board        0             2             WEST        6                     0           2           7
Move to nowhere                     0             2             NOWHERE     6                     0           2           7
Invalid results                     0             0             SOUTH       56                    0           0           57
Invalid move results                0             0             SOUTH       3                     0           1           7

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}