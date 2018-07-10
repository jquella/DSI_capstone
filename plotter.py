##### PLOTS!!! Good ones I saved from other people (or made for myself)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn.metrics as metrics

def plot_pairtriangle(df):
    """Seaborn pairplot with just the bottom triangle"""
    g = sns.pairplot(df)
    for i, j in zip(*np.triu_indices_from(g.axes, 1)):
        g.axes[i, j].set_visible(False);



def plot_groupby(df, column, grouping, summary='mean'):
    """Barplots the summary statistic of choice (default=mean) for a specific grouping, for a specific column.
    """
    
    test = np.ndarray.tolist(df[grouping].unique())
    
    for i in test:
        try:
            if math.isnan(float(i)):
                test.remove(i)
        except:
            pass

    # sns.barplot(x=sorted(test), y=[i for i in df.groupby(grouping)[column].agg(summary)]);
    plt.bar(x=sorted(test), height=[i for i in df.groupby(grouping)[column].agg(summary)]);


'''
def plot_residuals(df, feature, )
    fig = plt.figure(figsize = (15,7));
    ax = fig.gca();

    ax.scatter(df['sq_ft'], df['price'], color='k');

    ax.plot(df['sq_ft'], df['Linear_yhat'], color='k', zorder=10);

    for _, row in df.iterrows():
        ax.plot((row['sq_ft'], row['sq_ft']), (row['price'], row['Linear_yhat']), color='r');
'''

def plot_corrtriangle(df):
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})




def plot_cv(alphas, cv_means, optimal_alpha, lr_mse, log=False):
    """Takes in args to show plot of optimal alpha for Ridge/Lasso/Elastic Net compared to base LR.
    alphas = list of alphas
    cv_means = list of CV mean MSE
    optimal_alpha
    lr_mse
    """
    
    fig = plt.figure(figsize=(12,8))
    ax = plt.gca()

    if log:
        ax.semilogx(alphas, cv_means, lw=2)
    else:
        ax.plot(alphas, cv_means, lw=2)
    ax.axvline(optimal_alpha)
    ax.axhline(lr_mse)
    ax.set_xlabel('alpha')
    ax.set_ylabel('Mean Squared Error')
    
    #plot_cv(ridge_model.alphas, ridge_cv_means, ridge_optimal_alpha, lr_cv_mean_mse, log=True)

def plot_auc(estimator, X, y_true):
	threshold = np.arange(0, 1.01, .01)
	scores_rc = []
	scores_sp = []
	yprob = estimator.predict_proba(X)[:,1]

	for i in threshold:
		probas = (yprob > i).astype(int)
		rc = metrics.recall_score(y_true, probas)

		tn, fp, fn, tp = metrics.confusion_matrix(y_true, probas).ravel()
		sp = tn / (tn+fp)

		scores_rc.append(rc)
		scores_sp.append(sp)

	plt.plot([1-i for i in scores_sp], scores_rc);


def plot_nn(history, metric):

	train_loss = history.history[metric]
	test_loss = history.history['val_'+metric]
	plt.plot(train_loss, label='Training '+metric);
	plt.plot(test_loss, label='Test '+metric);

	plt.legend();