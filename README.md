[Report link](https://www.overleaf.com/5613896445zbzcpyxbgbpj)

# Words and politics: how well r/politics mirrors the reality 

## Abstract
The world is becoming increasingly connected in a time of technological advancements. Phenomena that contributed in revolutionising this field are social media platforms. Indeed, in introducing easy and fast communication through virtual space, populations all around the world can address news, opinions and many more, all while surfing through a platform of near infinite knowledge.  

In this project, we will concentrate on a social news and discussion website called *Reddit*. On this platform, users post comments containing content such as images, videos, text, and so on, which are then up or down voted by other users. Posts are organised by subjects into user-created boards called *subreddits*, which cover every imaginable topic.  
This project aims at analysing one specific and major subreddit named *r/politics*.  

Focusing on a particular timespan covering the months of June 2016 to November 2016, i.e. the 6 months preceding the American election of 2016, it aims at discovering the underlying patterns that make a comment deemed good by other users and understand how they correlate with actual events. It also aims at understanding the population of this subreddit by analysing its political spectrum and see how closely it mirrors the outcome of the 2016 American election.


## Research questions
* **Are there any words that stand out as strong polarisers of opinions?**  
Looking at low/high-scoring comments, we aim to see if certain words come up regularly. Comparing word frequency distribution between low/high-scoring comments may give us clues to what topic, concept or politician generate the most controversy. 

* **How did the popularity criteria for posts evolve through the years?**  
By observing the highest-scoring comments throughout the 6 months preceding the election, we intend to see how word distributions evolve and how they correlate with real events.

* **How close to the final outcome of the American election an estimation can be made?**  
Through basic natural language processing, we plan to look for a correlation between the outcome of the American election nation-wise but also state-wise, and the overall polarity of comments (if it is positive, negative, or neutral) mentioning specific politicians.

* **How the popularity for each competing candidate evolve through the years?**  
Looking at the fluctuating overall polarity of comments throughout the 6 months preceding the election, we'd like to see if specific real events had impact on the popularity of each candidate.


## Dataset
The dataset used consists of 10 years of Reddit comments, from 2007 to 2017. It has a size of 305GB compressed ant contains about 1.7 billion JSON objects with the comment, score, author, subreddit, position in comment tree and other fields that are available through Reddit's API.  
However, like pointed out earlier, the project only makes use of the comments found in the subreddit *r/politics* between June 2016 and November 2016. Using the cluster's computing power is necessary to retrieve this particular sub-dataset. Still, further queries on it should be possible locally in a reasonable time.


## Description of the repository
* *scripts* directory  
Contains the scripts used on the cluster to perform queries on the Reddit dataset.
* *Final project.ipynb*  
Contains the whole pipeline of operations performed on the dataset, along technical explanations that cannot be found in the report.


## Group members' contribution
* **Nourchene Ben Romdhane**
* **Arnaud Hennig**
* **Arthur Vernet**  
Dataset retrieval on the cluster
