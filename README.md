<img src="https://i.imgur.com/hXvwPlG.png">

# Best of the Best: 
## Predicting and Analyzing the All-NBA Team Awards


_Jamie Quella - 7/17/18_

**Goal:** The primary goal of this project was to predict a year’s All-NBA team from that season’s player stats and team information. This is a classification problem! The secondary goal was to use the predictive model as a starting point for further player analysis, for example, in examining where the model and reality differed.


**Process:** 
1. [Define Question.](#define_question)
2. [Gather Data.](#gather_data)
3. [Explore Data.](#explore_data)
4. [Model Data.](#model_data)
5. [Evaluate Model.](#evaluate_model)
6. [Additional Analysis.](#further_analysis)
7. [Answer Question.](#answer_question)

<a id='define_question'></a>
## Define the Question.
**Can we predict who gets on the three All-NBA teams based on their season stats, and information about their team?**

*Additional background and motivation*
------
**What is the All-NBA Award / what are we predicting?**
Three teams - 1st, 2nd, 3rd - of five players are voted on by the sports media from these positions types:

<img src="https://i.imgur.com/BIyliKP.png">

These players are honored as the best at their respective positions.

**So why should we care?**
1. *It can affect NBA contracts:* Award winners can command a higher salary.
2. *It can help a player's chance at getting into the Hall of Fame*: These accolades are often brought up when reviewing a player's HOF resume.
3. *You could bet on it in Vegas if you believe in your model:* You'd need to find good odds, too.
4. *I love NBA basketball and though it would be a neat project*

<a id='gather_data'></a>
## Gather Data.
NBA player data from 1989-2017 was collected from a subset of the data found [on Kaggle](https://www.kaggle.com/drgilermo/nba-players-stats/data). 

In addition, I scraped the [Basketball-Reference site](http://www.basketball-reference.com/) -- an invaluable resource -- for further information on the All-NBA awards, All-Star Awards, and team information for the 1989-2017 time period.

I used the `requests` and `BeautifulSoup` libraries to scrape the data, dynamically inserting each year necessary based on the URL structure.

This process was a bit more difficult than anticipated as the data tables were not consistent from year to year. After some trial and error, I implemented control flow around the requests and was able to pull all necessary data:
- All-Star teams by conference, starters / reserves flagged
- Team records by conference, including strength of schedule


*Note:* The reason I chose the 1989 onward time period was two-fold:
1. That was the year the league changed from two (2) to three (3) All-NBA teams, so predicting the same number of winners (15) for every year simplified the process.
2. There was an added side benefit of being after 1979, which was the first year the three point line existed. This allowed me to use all stats equally across players, since they all had the same court and scoring opportunities.

*In the end, the data looked like:*
- 28 NBA seasons (1989-2017), which at 30 teams in the NBA and approx. 14 players per team, was...
- 12K+ individual player-seasons, each with...
- 50+ player statistics, and on top of that...
- 20+ engineered features

Then it was time for the next task!

<a id='explore_data'></a>
## Explore Data.

**Data Cleaning**  
Since the player dataset was from Kaggle, it was pretty clean. I did have to do a few null cleanings, which was mostly dropping players who only played in one or two games and recorded next to no stats and so had `NaN` values in many columns.

Here is a list of some important model preparation I did (though not exhaustive):
- Map listed positions to 'award position' (e.g. PG/SG -> G)
- Clean player names where necessary (e.g. Ron Artest / Metta World Peace)
- Merge into one row data for players who were traded mid-season (and thus played for multiple teams)
- Clean team names due to city moves and expansion teams
	- This may upset some people but I used the most current team that inherits the franchise's history as the guide. For example, the Seattle Supersonics were mapped to the Oklahoma City Thunder (sorry, Seattleites!)
- **Merge player data with web-scraped award and team data into final dataset**

Lastly, I spent some time look at feature distributions to ensure there were not any stats I shouldn't use: either because they had values but those values acted like nulls, or because the distribution was so skewed the data became unhelpful. 

Example feature distribution below.

<img src="https://i.imgur.com/pB7aklJ.png">

I didn't find much there to indicate that there were any distribution issues, so onto the next step!


<a id='model_data'></a>
## Model Data.

Before building my model, there were two main items I had to tackle: **cross validation** and **model selection**. Then we could get into our **model predictions.**

**Cross Validation:** As with all data science problems, we want to ensure we are not creating something that only works on the one dataset we are working with, or in other words, overfitting. The problem with the normal train-test-split process in this case is two-fold:
1. We cannot use the normal process since we need all of any given year's player data to stay together (to predict on that year)
2. We want to control for statistical changes by era, as styles of play have evolved

To handle this, I manually chose the Train, Validation and Test (holdout) sets roughly according to quartets of years, picking three (3) train years for each (1) test year. See below for how they were apportioned.

<img src="https://i.imgur.com/0PbR9zu.png">


**Model Selection:** Analysis was a goal of the project, and understanding which features (stats) are important in determining award winners and losers is paramount. 

**_INTERPRETABILITY IS KEY!_**

In terms of model selection, that pointed me toward considering Logistic Regression and the Decision Tree model families for this classification problem, as they return feature importance.

In the end, I chose Logistic Regression (see example below).
- For its accuracy score (results in the next section) 
- And because it gives _direction of feature importance_, i.e., whether a stat helps or hurts a player's cause for winning the award, and by how much relative to the other stats.

<img src="https://i.imgur.com/obTT8gG.png">


**Model Predictions:** How did the prediction process go?
1. Predict each player’s probability of getting award 
2. Select top probabilities by position until award team is filled
3. Assign all of those players to target = 1, else 0
4. Calculate accuracy based on 15 predicted players
5. Repeat for each year


Now it's time to see how the model did!

<a id='evaluate_model'></a>
## Evaluate Model.

Because there are between 350-400 players in the league in any given year, most players don't win the award. Choosing those 15 players in our *target* out of 400 means we have very *imbalanced classes*. 

Hence our *baseline accuracy* is 96.6%. In this case, our baseline is how many total predictions (award/no award) we get correct if we just guess that NOBODY gets it, since that's the overwhelming majority.

Improving on that is hard! But the *model achieved 98.8% accuracy*. Not bad!

We want to dig a little deeper into our classification accuracy, though. Was the model better at getting it right for players who *would* make it, or who *wouldn't* make it?

<img src="https://i.imgur.com/r8K0iwC.png">

Unsurprisingly, it's a little harder to get the smaller target category correct, but 83% is not bad, either!

We also wanted to examine some of those top (and bottom) predictive features, which is why we chose this model type to begin with. Let's take a a look.

<img src="https://i.imgur.com/2BJIlvL.png">

**Most Positive Features**
- Team wins
	- Being on a good team helps your cause!
- Win Shares (Total, Offensive, Defensive). [Reference info](https://www.basketball-reference.com/about/ws.html) on this stat, which approximates an individual players contribution to a win.
	- These make sense since they are derived from multiple other stats (though not directly colinear) and attempt to capture a player's overall perforamnce.

**Most Negative Features**
- Personal Fouls (total and per game)
	- This one makes sense intuitively (I hope to everyone else too!).
- 3 point Attempt Rate (3P attempts / total shot attempts)
	- Likely due to those having a high 3PAR being either inefficient chuckers, or on really bad teams with a really green light.

Let's find out a little bit more about what the model can help us learn.

<a id='further_analysis'></a>
## Additional Analysis.
- What can we learn from the predicted probabilities?
- Where do the predictions and true values diverge?

These two questions drove me to create a few different kind of awards...

**1. Biggest Snub - James Harden, 2016**

<!---
<img style="float: left; width: 153px; height: 250px; margin:20px" src="https://i.imgur.com/13Bue3Z.png">
--->
![James Harden](https://i.imgur.com/13Bue3Z.png?classes=float-right)


**What Happened?**
- Model gave 98.2% prob. of getting award
- Team success for other guards 
- ¯\\_(ツ)/\_/¯  didn’t even make sense at the time

**Who Should’ve Been Left Off**
- Klay Thompson (36% probability)



<a id='answer_question'></a>
## Answer Question.

**Q: Were we able to predict who makes the All-NBA team based on his stats?** 

**A:** Yes! But there will likely always be some error due to the human judgment and bias that goes into the award selection.

**Next steps**
1. Add more features to improve model
	- Ex: previous winner count
2. More model tuning
	- Secondary model for “toss ups”
	- More bootstrapping
	- GridSearch may improve accuracy
3. Further analysis for more insight
	- Salary info for “best value” 
	- Forecast next year’s winners


## Further Reading
In addition to the above post, please peruse the following presentations and technical notebooks (with code) if you'd like more information!

### Presentations
1. Technical (longer): https://goo.gl/T3f4Uh
2. Non-technical (shorter): https://goo.gl/qG9LKY

### Technical Notebooks
1. [EDA notebook](https://github.com/jquella/DSI_capstone/blob/master/eda_v1.ipynb "eda_v1.ipynb") - Initial data gathering, cleaning and prep notebook. 
	- Link at bottom to:
2. [Model Notebook - v1](https://github.com/jquella/DSI_capstone/blob/master/model_v1.ipynb "model_v1.ipynb") - Feature engineering, modeling process and results, model evaluation. 
	- [Model Notebook - v2](https://github.com/jquella/DSI_capstone/blob/master/model_v2.ipynb "model_v2.ipynb") - Same as above, but with augmented dataset containing player's team information (e.g. Wins, Strength of Schedule)
	- Link at bottom to:
3. [Analysis and Takeaways - v1](https://github.com/jquella/DSI_capstone/blob/master/Analysis%20and%20Takeaways.ipynb "Analysis and Takeaways") - Further analysis based on model results.
	- [Analysis and Takeaways - v2](https://github.com/jquella/DSI_capstone/blob/master/Analysis%20and%20Takeaways_v2.ipynb "Analysis and Takeaways_v2") - Same as above with second model containing team information.

