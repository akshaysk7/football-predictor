## IDEA


A supervised classification model predicting Premier League match outcomes
— home win, draw, or away win — from historical match data.

The pipeline covers data cleaning, feature engineering from match history
(rolling form, goal difference, home/away splits, rest days), chronological
train/test splitting to avoid data leakage, and evaluation against a
majority-class baseline using confusion matrices and log loss.

Models: logistic regression, then random forest for comparison.

`Python` `pandas` `scikit-learn` `NumPy`

## Data dictionary

Source: football-data.co.uk, Premier League (E0). 380 matches, 132 columns.
~110 of those are bookmaker odds — dropped (see Design decisions).

### Match identifiers
- Div — league division
- Date — match date
- HomeTeam / AwayTeam

### Result
- FTHG / FTAG — full-time goals, home / away
- FTR — full-time result (H / D / A)  ← this is the target
- HTHG / HTAG / HTR — half-time equivalents

### Match statistics
- Referee
- HS / AS — shots
- HST / AST — shots on target
- HC / AC — corners
- HF / AF — fouls committed
- HY / AY — yellow cards
- HR / AR — red cards


## TARGET 
**Target (what the model predicts):**
FTR = Full Time Result (H = Home Win, D = Draw, A = Away Win)


## Pre-match vs post-match

**Post-match (not usable for this match — but the raw material for historical features):**
HS = Home Team Shots
AS = Away Team Shots
HST = Home Team Shots on Target
AST = Away Team Shots on Target
HHW = Home Team Hit Woodwork
AHW = Away Team Hit Woodwork
HC = Home Team Corners
AC = Away Team Corners
HF = Home Team Fouls Committed
AF = Away Team Fouls Committed
HFKC = Home Team Free Kicks Conceded
AFKC = Away Team Free Kicks Conceded
HO = Home Team Offsides
AO = Away Team Offsides
HY = Home Team Yellow Cards
AY = Away Team Yellow Cards
HR = Home Team Red Cards
AR = Away Team Red Cards
HBP = Home Team Bookings Points (10 = yellow, 25 = red)
ABP = Away Team Bookings Points (10 = yellow, 25 = red)
FTHG and HG = Full Time Home Team Goals
FTAG and AG = Full Time Away Team Goals
HTHG = Half Time Home Team Goals
HTAG = Half Time Away Team Goals
HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

**Pre-match (available before kickoff):**
Div = League Division
Date = Match Date (dd/mm/yy)
Time = Time of match kick off
HomeTeam = Home Team
AwayTeam = Away Team

## Design decisions

- Dropped ~110 bookmaker odds columns from features. Using them would mean
  learning to decode the bookmaker's prediction rather than building one.
  Kept aside as a benchmark to compare against.
- Leakage rule: a column is only usable if it was known before kickoff.
  Half-time columns would be valid features if predicting from half-time —
  the classification depends on the prediction moment, not the column.
  
