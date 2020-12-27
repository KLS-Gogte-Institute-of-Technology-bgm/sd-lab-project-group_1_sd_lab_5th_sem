# Proposal - Movie Recommender System
A recommender system, or a recommendation system (sometimes replacing 'system' with a synonym such as platform or engine), is a subclass of information filtering system that seeks to predict the "rating" or "preference" a user would give to an item. They are primarily used in commercial applications.

Recommender systems have also been developed to explore research articles and experts, collaborators,  and financial services.
One of the main advantages of using recommendation systems is that users get broader exposure to many different products they might be interested in. This exposure encourages users towards the continual usage or purchase of their products. Not only does this provide a better experience for the user but it benefits the service provider, as well, with increased potential revenue and better security for its customers.

## Overview

1. **Content Based** - *“Show me more of the same of what I’ve liked before.”*
2. **Collabatory Filtering** - *“Tell me what’s popular among my neighbours because I might like it too.”*
3. **Hybrid Model** - Combination of various mechanisms.

**We will be building using Collaboratory Filtering to build a MOVIE RECOMMENDER SYSTEM!**

## Intuition
Collaborative filtering has basically two approaches:
1. **User-based** (and)
 User-based collaborative filtering is based on the user similarity or neighborhood.
2. **Item-based**
Item-based collaborative filtering is based on similarity among items.

In this we will be approaching user-based filtering and the intuition behind it is-
In user-based collaborative filtering, we have an active user for whom the recommendation is aimed at. The collaborative filtering engine first looks for users who are similar to that particular active user, that is, users who share the active user’s rating patterns. Collaborative filtering bases this similarity on things like history, preference, and choices that users make when buying, watching, or enjoying something, for example, movies that similar users have rated highly. Then it uses the ratings from these similar users to predict the possible ratings by the active user for a movie that they had not previously watched. For instance, if two users are similar or, are neighbors in terms of their interested movies, we can recommend a movie to the active user that their neighbor has already seen.

## Build with
* Python

## Authors
* **Nikita Kodkany** - *Machine Learning Practioner*
* **Nischal Kanishk** - *Full-Stack Developer*
* **Prathamesh Koranne** - *Machine Learning Practioner*
* **Prithvi Gudodagi** - *Aspiring Cyber Security Practioner*

## Reference
* Andrew Ng
