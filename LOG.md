## Day 0
- Set up project folder
- ## Day 1
- df.shape → 380 rows, 132 cols. Most of the columns are bookmaker odds.
- Decided to drop odds from features (would just be copying Bet365's prediction),
  keeping them as a benchmark instead.
- Sorted columns into target (FTR) / pre-match / post-match.
- Realised pre-match columns alone are useless — features have to be
  engineered from past matches. That's v1.
  ## day whatever
  Added points column with apply(axis=1) + lambda. Learned: map sees one value, apply(axis=1) sees a whole row; row is a parameter that gets its value when apply calls the lambda. Verified: 276/276/208. Next: re-sort team_matches by date, then last-5 form.
