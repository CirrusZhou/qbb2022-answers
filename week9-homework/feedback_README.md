This is a really great start! A few comments, and some things we need before this is complete:
1. In your clustermap, I don't think you want to include the zscore argument, as it normalizes the data in a way that makes the patterns a little harder to see. You can also use `leaves_list` to reorganize your data manually (no points deducted).
2. I have you dendrogram for transcript clustering, but not for sample. You should be able to run `linkage` on the transpose of your expression array, and plot the dendrogram from that. BUT it's in your clustermap, so not a big deal (no points deducted)
3. We still need your code for the regression (both models), the QQ plot for the model without sex, the volcano plot for the model with sex, and a comparison of the significant (10% FDR) transcripts between the two models (-5 points)

Let us know if you have any questions!

(5/10)
