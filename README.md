# Utilize data within 2014-2017 for main statistics
# Backtest against 2018 data *Game by game*
^^Step1 import data from 2013 2017
    needs more player based data
    Need WAR for players 2014-2018 and LOB for Teams 2014-2018
    MMR and ELO system
        *   ^different aspects
Defense strength and offense strength stats weighted into determining win%
overall strength = defense strength + offense strength
    >>Create function to determine weight for home advantage and 
    away advantage for TEAM based on

    >>Convert decimal odds to probability odds function and
    base bet predictor on kelly criterion


$$ Ratings tend to converge on a team's true strength relative to its competitors after about 30 matches. Ratings for teams with fewer than 30 matches should be considered provisional.

The ratings are based on the following formulas:
Rn = Ro + K × (W - We)

Rn is the new rating, Ro is the old (pre-match) rating.

K is the weight constant for the tournament played:

    60 for World Cup finals;
    50 for continental championship finals and major intercontinental tournaments;
    40 for World Cup and continental qualifiers and major tournaments;
    30 for all other tournaments;
    20 for friendly matches.

K is then adjusted for the goal difference in the game. It is increased by half if a game is won by two goals, by 3/4 if a game is won by three goals, and by 3/4 + (N-3)/8 if the game is won by four or more goals, where N is the goal difference.

W is the result of the game (1 for a win, 0.5 for a draw, and 0 for a loss).

We is the expected result (win expectancy), either from the chart or the following formula:
We = 1 / (10(-dr/400) + 1)

dr equals the difference in ratings plus 100 points for a team playing at home. 
$$

Strengths of model:
    Takes into account:
        Home and away factor
        Win Streak/Loss Streak
        ELO and MMR system based around streaks
        Based on strength of starting pitcher and lineup
            -roster changes and injuries taken into account if lineup known
        Trained based on inputs of previous seasons
        
Weaknesses:
    No Batter vs pitcher 
    Weather/ Location not taken into account 
    Walks and other indepth fielding stats left out
    Tedious to input info to train and backtest



