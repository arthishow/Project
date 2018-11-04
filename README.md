# The power of words: how to influence people

# Abstract

The world is becoming increasingly connected in a time of technological advancements. Phenomena that contributed in revolutionizing this field are social media platforms. Indeed, in introducing easy and fast communication through virtual space, populations all around the world can address news, opinions and many more, all while surfing through a platform of near infinite knowledge. 

In this project, we will concentrate on a social news and discussion website, Reddit. On this platform, members submit content such as images, text posts, etc, which are then voted up or down by other members. Posts are organized by subjects into user-created boards called "subreddits", which cover every imaginable topic. In gaining popularity in terms of votes (Reddit uses the term karma here), Reddit has been a platform for many to raise awareness for a number of causes ; members can now use one of the largest communities on the Internet for new and influential purposes.

Using 12 years of Reddit comments history, this project aims to discover the underlying patterns that make a comment/review deemed good by other users, and the subjects dealt with. 

# Research questions 

* Are there any words that stand out as strong polarizers of opinions ? 

* To what extent can words affect people psychologically ?

* Are users with strong votes (karma) more likely to generate popular comments ? Are scores independent of previous ones ? 

* How did the popularity criteria for posts evolve through the years ?  

# Dataset

We want to use the Reddit comments dataset from academictorrents.com. It has a size of 305GB compressed. 
The dataset consists of ~1.7 billion JSON objects complete with the comment, score, author, subreddit, position in comment tree and other fields that are available through Reddit's API.
Splitting the data along carefully selected popular subreddits might be relevant as using the entire dataset may not be productive or necessary.
Also, in order to observe specific users and their influence, we will have to compute their karma by aggregating their complete post history. As it'll probably be an expensive operation, we still have to see its viability. 


# A list of internal milestones up until project milestone 2

* Exploratory data analysis : data cleaning if needed, partitioning, ...
* Find useful algorithms for all this data processing.
* Find the best data visualization that suits our data set.

# Questions for TAs

* Do you think that natural language processing will be needed for data analysis ? 
