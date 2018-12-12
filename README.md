[Report link](https://www.overleaf.com/5613896445zbzcpyxbgbpj)

# The power of words: how to influence people

# Abstract

The world is becoming increasingly connected in a time of technological advancements. Phenomena that contributed in revolutionizing this field are social media platforms. Indeed, in introducing easy and fast communication through virtual space, populations all around the world can address news, opinions and many more, all while surfing through a platform of near infinite knowledge.

In this project, we will concentrate on a social news and discussion website, Reddit. On this platform, members submit content such as images, text posts, etc, which are then voted up or down by other members. Posts are organized by subjects into user-created boards called "subreddits", which cover every imaginable topic. In gaining popularity in terms of votes (Reddit uses the term karma here), Reddit has been a platform for many to raise awareness for a number of causes ; members can now use one of the largest communities on the Internet for new and influential purposes.

Using specific periods of Reddit comments history and focusing on the "politics" subreddit, this project aims to discover the underlying patterns that make a comment/review deemed good by other users. More specifically, we will try to find a pattern that is recurrent in order to predict the score of a political review during the 3 latest American presidential elections, and develop a political profile of reddit.

# Research questions

* Are there any words that stand out as strong polarizers of opinions ?
We can see the posts with the highest or lowest score and find if they treat of the same thing, contain similar words.

* Are users with strong votes (karma) more likely to generate popular comments ? Are scores independent of previous ones ?
This will be treated in user influence.

* How did the popularity criteria for posts evolve through the years ?  
We will study the different patterns of the most popular politic comments throughout the three American elections, and see if it evolved throughout the years.

# Dataset

We want to use the Reddit comments dataset from academictorrents.com. It has a size of 305GB compressed.
The dataset consists of ~1.7 billion JSON objects complete with the comment, score, author, subreddit, position in comment tree and other fields that are available through Reddit's API.

We chose to work with the politics subreddit, more specifically just before the American presidential election period, i.e during October 2008, October 2012 and October 2016.

# Description of the repository :

* report directory : will contain the final report project.
* scripts directory : contains the scripts used on the cluster to perform queries on the data set.
* Milestone 2.ipynb : contains data analysis and visualization for milestone 2.

# Action plan and ideas for Milestone 3 :

* Exploratory Data Analysis

There seems to be a lot of data features not necessarily useful for our research, so we can use cross validation and backward selection to remove unnecessary features in our selected parts of the data, or see if there are other techniques that work faster. Moreover, we can create more features by using natural language processing on the "body" attribute corresponding to the comments.

* Model selection :

We will also need to do a model selection to choose the model that predicts best the score : we can compute the accuracy and the mean square error when applying a certain model to our data set and choose the best from various ones (Logistic regression, Decision trees, Random forest, ...). We can then also tune the hyper parameters of these models if they have ones for optimality.

* User Influence :

In order to observe specific users and their influence, we will have to compute their karma by aggregating their complete post history. As it'll probably be an expensive operation, we still have to see its viability.
