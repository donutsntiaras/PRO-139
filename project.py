# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:48:12 2022

@author: Vedgunika
"""

import pandas as pd
shared_articles = pd.read_csv('shared_articles.csv')
user_int = pd.read_csv("users_interactions.csv")
print(shared_articles.head(5))
print(user_int.head(5))

print(shared_articles.columns)
print(user_int.columns)

shared_articles =shared_articles[shared_articles["eventType"] == 'CONTENT SHARED']
shared_articles.head()

def find_total_events(sa_rows):
    total_likes = user_int[(user_int["contentId"] == sa_rows["contentId"]) &(user_int["eventType"] == "LIKE")].shape(0)
    total_views =  user_int[(user_int["contentId"] == sa_rows["contentId"]) &(user_int["eventType"] == "VIEW")].shape(0)
    total_bookmarks =  user_int[(user_int["contentId"] == sa_rows["contentId"]) &(user_int["eventType"] == "BOOKMARK")].shape(0)
    total_follows =  user_int[(user_int["contentId"] == sa_rows["contentId"]) &(user_int["eventType"] == "FOLLOW")].shape(0)
    total_comments =  user_int[(user_int["contentId"] == sa_rows["contentId"]) &(user_int["eventType"] == "COMMENT CREATED")].shape(0)
    return total_likes + total_views + total_bookmarks + total_follows + total_comments 

shared_articles["total_events"] =  shared_articles.apply(find_total_events, axis =1)


shared_articles.sort_values(['total_events'], ascending=[False])
shared_articles.head()
 







