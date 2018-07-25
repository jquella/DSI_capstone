<img src="https://i.imgur.com/hXvwPlG.png">

# Best of the Best: 
## Predicting and Analyzing the All-NBA Team Awards


_Jamie Quella - 7/17/18_

**Goal:** The primary goal of this project was to predict a year’s All-NBA team from that season’s player stats and team information. The secondary goal was to use the predictive model as a starting point for further player analysis, for example, in examining where the model and reality differed.


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
- Clean team names due to city moves and expansion teams
	- This may upset some people but I used the most current team that inherits the franchise's history as the guide. For example, the Seattle Supersonics were mapped to the Oklahoma City Thunder (sorry, Seattleites!)
- **Merge player data with web-scraped award and team data into final dataset**

Lastly, I spent some time look at feature distributions to ensure there were not any stats I shouldn't use: either because they had values but those values acted like nulls, or because the distribution was so skewed the data became unhelpful. 

I didn't find much there to indicate that, so tht led us to the next step!


<a id='model_data'></a>
## Model Data.

Before building my model, there were two main items I had to tackle: **cross validation** and **model selection**.






## Further Reading
In addition to the above post, please peruse the following presentations and technical notebooks (with code) if you'd like more information!

### Presentations
1. Technical (longer): https://goo.gl/T3f4Uh
2. Non-technical (shorter): https://goo.gl/qG9LKY

### Technical Notebooks
1. [eda_v1.ipynb](https://github.com/jquella/DSI_capstone/blob/master/eda_v1.ipynb) - Initial data gathering, cleaning and prep notebook. 
	- Link at bottom to:
2. [model_v1.ipynb](https://github.com/jquella/DSI_capstone/blob/master/model_v1.ipynb) - Feature engineering, modeling process and results, model evaluation. 
	- [model_v2.ipynb](https://github.com/jquella/DSI_capstone/blob/master/model_v2.ipynb) - Same as above, but with augmented dataset containing player's team information (e.g. Wins, Strength of Schedule)
	- Link at bottom to:
3. [Analysis and Takeaways](https://github.com/jquella/DSI_capstone/blob/master/Analysis%20and%20Takeaways.ipynb) - Further analysis based on model results.
	- [Analysis and Takeaways_v2](https://github.com/jquella/DSI_capstone/blob/master/Analysis%20and%20Takeaways_v2.ipynb) - Same as above with second model containing team information.

