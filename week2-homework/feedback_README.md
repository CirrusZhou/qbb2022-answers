This is really great! You jsut about nailed needleman-wunsch.

One very small thing: When you're checking for leading gaps in your last while loop, make sure you also increment the number of gaps (no points deducted)

Also, the way your building your alignments, they actually end up being backwards. You can either modify traceback so that it adds characters onto the beginning of each alignment, rather than the end (remember, we're moving backwards through the sequences), or you can just reverse the alignments at the end of traceback (-0.25)

Really awesome work though.

9.75/10
