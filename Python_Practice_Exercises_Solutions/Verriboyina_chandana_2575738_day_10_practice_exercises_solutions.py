#!/usr/bin/env python
# coding: utf-8

# # EXERCISE - 1

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[ ]:


from IPython.core.display import HTML
css = open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# In[4]:


titles = pd.read_csv('titles.csv')
titles.head()


# In[5]:


cast = pd.read_csv('cast.csv', index_col = None)
cast.head()


# # 1. How many movies are listed in the titles dataframe?

# In[6]:


num_movies = len(titles)
print('The number of movies listed in the titles dataframe is:', num_movies)


# # 2. What are the earliest two films listed in the titles dataframe?

# In[8]:


# Sort the DataFrame by the 'year' column in ascending order
sorted_titles = titles.sort_values(by='year')

# Select the first two rows i.e., earliest two films
earliest_two_films = sorted_titles.head(2)

print('The earliest two films listed in the titles dataframe are:\n\n', earliest_two_films)


# # 3. How many movies have the title "Hamlet"?

# In[9]:


hamlet_count = len(titles[titles['title'] == 'Hamlet'])
print('The number of movies with the title "Hamlet" is:', hamlet_count)


# # 4. How many movies are titled "North by Northwest"?

# In[10]:


north_by_northwest_count = len(titles[titles['title'] == 'North by Northwest'])
print('The number of movies titled "North by Northwest" is:', north_by_northwest_count)


# # 5. When was the first movie titled "Hamlet" made?

# In[11]:


# Filtering the DataFrame for movies titled "Hamlet" and finding the earliest release year
earliest_hamlet_movie_year = titles[titles['title'] == 'Hamlet']['year'].min()
print('The first movie titled "Hamlet" was made in the year:', earliest_hamlet_movie_year)


# # 6. List all of the "Treasure Island" movies from earliest to most recent.

# In[13]:


# Filtering the DataFrame for movies titled "Treasure Island" and sorting them by release year
treasure_island_movies = titles[titles['title'] == 'Treasure Island'].sort_values(by='year')
print('The list of all "Treasure Island" movies from earliest to most recent are:\n\n',treasure_island_movies[['title','year']])


# # 7. How many movies were made in the year 1950?

# In[15]:


movies_in_1950 = titles[titles['year'] == 1950]
num_movies_in_1950 = len(movies_in_1950)
print('The number of movies made in the year 1950 are:', num_movies_in_1950)


# # 8. How many movies were made in the year 1960?

# In[16]:


movies_in_1960 = titles[titles['year'] == 1960]
num_movies_in_1960 = len(movies_in_1960)
print('The number of movies made in the year 1960 are:', num_movies_in_1960)


# # 9. How many movies were made from 1950 through 1959?

# In[17]:


# Filtering the DataFrame for movies released from 1950 to 1959 (inclusive)
movies_in_1950s = titles[(titles['year'] >= 1950) & (titles['year'] <= 1959)]

num_movies_in_1950s = len(movies_in_1950s)
print('The number of movies made from 1950 through 1959 are:', num_movies_in_1950s)


# # 10. In what years has a movie titled "Batman" been released?

# In[18]:


batman_movies = titles[titles['title'] == 'Batman']
batman_release_years = batman_movies['year'].unique()
print('Years in which a movie titled "Batman" has been released:', sorted(batman_release_years))


# # 11. How many roles were there in the movie "Inception"?

# In[19]:


inception_roles = cast[cast['title'] == 'Inception']
num_roles_in_inception = len(inception_roles)
print('The number of roles there in the movie "Inception" is:', num_roles_in_inception)


# # 12. How many roles in the movie "Inception" are NOT ranked by an "n" value?

# In[22]:


# Filtering the DataFrame for roles in the movie "Inception" without a numeric "n" value
inception_roles_without_n_rank = cast[(cast['title'] == 'Inception') & ~cast['n'].astype(str).str.isnumeric()]

# Counting the number of roles in "Inception" without an "n" value
num_roles_in_inception_without_n_rank = len(inception_roles_without_n_rank)

print('The number of roles in the movie "Inception" without an "n" rank are:', num_roles_in_inception_without_n_rank)


# # 13. But how many roles in the movie "Inception" did receive an "n" value?

# In[24]:


# Converting the "n" column to numeric (ignore errors for non-numeric values)
cast['n'] = pd.to_numeric(cast['n'], errors='coerce')

# Filtering the DataFrame for roles in the movie "Inception" with a numeric "n" value
inception_roles_with_n_rank = cast[(cast['title'] == 'Inception') & ~cast['n'].isna()]

# Counting the number of roles in "Inception" with an "n" value
num_roles_in_inception_with_n_rank = len(inception_roles_with_n_rank)

print('The number of roles in the movie "Inception" with an "n" rank is:', num_roles_in_inception_with_n_rank)


# # 14. Display the cast of "North by Northwest" in their correct "n" -value order, ignoring roles that did not earn a numeric "n" value.

# In[29]:


cast = pd.read_csv('cast.csv')
filtered_cast = cast[(cast['title'] == 'North by Northwest') & cast['n'].notna()]
sorted_cast = filtered_cast.sort_values(by='n')
print('The cast of "North by Northwest" in their correct "n" -value order are:\n\n', sorted_cast[['name', 'n']])


# # 15. Display the entire cast, in "n"-order, of the 1972 film "Sleuth".

# In[31]:


sleuth_1972_cast = cast[(cast['title'] == "Sleuth") & (cast['year'] == 1972)]
sleuth_1972_cast = sleuth_1972_cast.sort_values(by='n')
print('The entire cast, in "n"-order, of the 1972 film "Sleuth" are:\n\n', sleuth_1972_cast[['name', 'n']])


# # 16. Now display the entire cast, in "n"-order, of the 2007 version of "Sleuth".

# In[33]:


sleuth_2007_cast = cast[(cast['title'] == "Sleuth") & (cast['year'] == 2007)]
sleuth_2007_cast = sleuth_2007_cast.sort_values(by='n')
print('The entire cast, in "n"-order, of the 2007 version of "Sleuth" are:\n\n', sleuth_2007_cast[['name', 'n']])


# # 17. How many roles were credited in the silent 1921 version of Hamlet?

# In[34]:


hamlet_1921_roles = cast[(cast['title'] == "Hamlet") & (cast['year'] == 1921)]
num_credited_roles_in_hamlet_1921 = len(hamlet_1921_roles[hamlet_1921_roles['n'].notnull()])
print('The number of credited roles in the silent 1921 version of "Hamlet" are:', num_credited_roles_in_hamlet_1921)


# # 18. How many roles were credited in Branagh's 1996 Hamlet?

# In[36]:


# Filtering the DataFrame for roles in the movie "Hamlet" (1996)
branagh_hamlet_roles = cast[(cast['title'] == "Hamlet") & (cast['year'] == 1996)]

# Counting the number of credited roles in Branagh's 1996 Hamlet
num_credited_roles_in_branagh_hamlet = len(branagh_hamlet_roles[branagh_hamlet_roles['n'].notnull()])

print("The number of credited roles in Branagh's 1996 Hamlet are:", num_credited_roles_in_branagh_hamlet)


# # 19. How many "Hamlet" roles have been listed in all film credits through history?

# In[38]:


hamlet_roles = cast[cast['title'] == 'Hamlet']
num_hamlet_roles = len(hamlet_roles)
print('The number of "Hamlet" roles that have been listed in all film credits through history are:', num_hamlet_roles)


# # 20. How many people have played an "Ophelia"?

# In[39]:


ophelia_roles = cast[cast['character'] == 'Ophelia']
num_ophelia_actors = len(ophelia_roles['name'].unique())
print('The number of people who have played the role "Ophelia" are:', num_ophelia_actors)


# # 21. How many people have played a role called "The Dude"?

# In[40]:


the_dude_roles = cast[cast['character'] == 'The Dude']
num_the_dude_actors = len(the_dude_roles['name'].unique())
print('The number of people who have played the role of "The Dude" are:', num_the_dude_actors)


# # 22. How many people have played a role called "The Stranger"?

# In[41]:


the_stranger_roles = cast[cast['character'] == 'The Stranger']
num_the_stranger_actors = len(the_stranger_roles['name'].unique())
print('The number of people who have played the role of "The Stranger" are:', num_the_stranger_actors)


# # 23. How many roles has Sidney Poitier played throughout his career?

# In[42]:


sidney_poitier_roles = cast[cast['name'] == 'Sidney Poitier']
num_sidney_poitier_roles = len(sidney_poitier_roles)
print('Sidney Poitier has played',num_sidney_poitier_roles,'roles throughout his career.')


# # 24. How many roles has Judi Dench played?

# In[43]:


judi_dench_roles = cast[cast['name'] == 'Judi Dench']
num_judi_dench_roles = len(judi_dench_roles)
print('Judi Dench has played',num_judi_dench_roles,'roles throughout her career.')


# # 25. List the supporting roles (having n=2) played by Cary Grant in the 1940s, in order by year.

# In[45]:


# Filtering the DataFrame for Cary Grant's supporting roles (n=2) in the 1940s
cary_grant_supporting_roles_1940s = cast[(cast['name'] == 'Cary Grant') & (cast['n'] == 2) & (cast['year'] >= 1940) & (cast['year'] < 1950)]

# Sorting the resulting DataFrame by year
cary_grant_supporting_roles_1940s = cary_grant_supporting_roles_1940s.sort_values(by='year')

print('The supporting roles played by Cary Grant in the 1940s are:\n\n',cary_grant_supporting_roles_1940s[['year','character']])


# # 26. List the leading roles that Cary Grant played in the 1940s in order by year.

# In[46]:


# Filtering the DataFrame for Cary Grant's leading roles (n=1) in the 1940s
cary_grant_leading_roles_1940s = cast[(cast['name'] == 'Cary Grant') & (cast['n'] == 1) & (cast['year'] >= 1940) & (cast['year'] < 1950)]

# Sorting the resulting DataFrame by year
cary_grant_leading_roles_1940s = cary_grant_leading_roles_1940s.sort_values(by='year')

print('The leading roles that Cary Grant played in the 1940s are:\n\n', cary_grant_leading_roles_1940s[['year', 'character']])


# # 27. How many roles were available for actors in the 1950s?

# In[47]:


roles_in_1950s = cast[(cast['year'] >= 1950) & (cast['year'] < 1960)]
num_roles_in_1950s = len(roles_in_1950s)
print('The number of roles available for actors in the 1950s were:', num_roles_in_1950s)


# # 28. How many roles were available for actresses in the 1950s?

# In[48]:


actress_roles_in_1950s = cast[(cast['type'] == 'actress') & (cast['year'] >= 1950) & (cast['year'] < 1960)]
num_actress_roles_in_1950s = len(actress_roles_in_1950s)
print('The number of roles available for actresses in the 1950s were:', num_actress_roles_in_1950s)


# # 29. How many leading roles (n=1) were available from the beginning of film history through 1980?

# In[49]:


# Filtering the DataFrame for leading roles (n=1) from the beginning of film history through 1980
leading_roles_through_1980 = cast[(cast['n'] == 1) & (cast['year'] <= 1980)]

# Counting the number of leading roles available from the beginning of film history through 1980
num_leading_roles_through_1980 = len(leading_roles_through_1980)

print('The number of leading roles available from the beginning of film history through 1980 is:',num_leading_roles_through_1980)


# # 30. How many non-leading roles were available through from the beginning of film history through 1980?

# In[50]:


# Filtering the DataFrame for non-leading roles (n values other than 1) from the beginning of film history through 1980
non_leading_roles_through_1980 = cast[(cast['n'] != 1) & (cast['year'] <= 1980)]

# Counting the number of non-leading roles available from the beginning of film history through 1980
num_non_leading_roles_through_1980 = len(non_leading_roles_through_1980)

print('The number of non-leading roles available from the beginning of film history through 1980 is:',num_non_leading_roles_through_1980)


# # 31. How many roles through 1980 were minor enough that they did not warrant a numeric "n" rank?

# In[51]:


# Converting the 'n' column to a string and then filter the DataFrame
cast['n'] = cast['n'].astype(str)
roles_through_1980_without_numeric_n = cast[(cast['year'] <= 1980) & (~cast['n'].str.isnumeric())]

# Counting the number of such roles
num_roles_without_numeric_n_through_1980 = len(roles_through_1980_without_numeric_n)

print('The number of roles through 1980 without a numeric "n" rank is:', num_roles_without_numeric_n_through_1980)


# # EXERCISE - 2

# In[52]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[ ]:


from IPython.core.display import HTML
css = open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# In[53]:


titles = pd.read_csv('titles.csv', index_col = None)
titles.head()


# In[54]:


cast = pd.read_csv('cast.csv', index_col = None)
cast.head()


# # 1. What are the ten most common movie names of all time?

# In[57]:


# Counting the occurrences of each movie title and get the top 10 most common titles
top_10_common_titles = titles['title'].value_counts().head(10)
print('The ten most common movie names of all time are: \n', top_10_common_titles)


# # 2. Which three years of the 1930s saw the most films released?

# In[58]:


# Filter the DataFrame for movies released in the 1930s
movies_in_1930s = titles[(titles['year'] >= 1930) & (titles['year'] <= 1939)]

# Count the number of movies released each year in the 1930s and get the top 3 years
movie_counts_by_year = movies_in_1930s['year'].value_counts()
top_3_years = movie_counts_by_year.head(3)

print('The three years of the 1930s with the most films released are:')
print(top_3_years)


# # 3. Plot the number of films that have been released each decade over the history of cinema.

# In[59]:


import pandas as pd
import matplotlib.pyplot as plt

# Creating a new DataFrame to count films by decade
decade_counts = titles['year'] // 10 * 10

# Plotting the number of films released each decade
decade_counts.value_counts().sort_index().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Decade')
plt.ylabel('Number of Films')
plt.title('Number of Films Released Each Decade')
plt.xticks(rotation=45)
plt.show()


# # 4. Plot the number of "Hamlet" films made each decade.

# In[61]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for movies titled "Hamlet"
hamlet_movies = titles[titles['title'] == 'Hamlet'].copy()

# Calculate the decade for each "Hamlet" film using .loc
hamlet_movies['decade'] = (hamlet_movies['year'] // 10) * 10

# Group the data by decade and count the number of "Hamlet" films in each decade an plot them
hamlet_decade_counts = hamlet_movies['decade'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(hamlet_decade_counts.index, hamlet_decade_counts.values, width=5, align='center')
plt.xlabel('Decade')
plt.ylabel('Number of "Hamlet" Films')
plt.title('Number of "Hamlet" Films Made Each Decade')
plt.xticks(hamlet_decade_counts.index, rotation=45)
plt.show()


# # 5. Plot the number of "Rustler" characters in each decade of the history of film.

# In[62]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for characters with the name "Rustler"
rustler_characters = cast[cast['character'] == 'Rustler'].copy()

# Calculate the decade for each film with a "Rustler" character using .loc
rustler_characters.loc[:, 'decade'] = (rustler_characters['year'] // 10) * 10

# Group the data by decade and count the number of "Rustler" characters in each decade and plot them
rustler_decade_counts = rustler_characters['decade'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(rustler_decade_counts.index, rustler_decade_counts.values, width=5, align='center')
plt.xlabel('Decade')
plt.ylabel('Number of "Rustler" Characters')
plt.title('Number of "Rustler" Characters in Each Decade')
plt.xticks(rustler_decade_counts.index, rotation=45)
plt.show()


# # 6. Plot the number of "Hamlet" characters each decade.

# In[63]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for characters in the movie "Hamlet"
hamlet_characters = cast[cast['title'] == 'Hamlet'].copy()

# Calculate the decade for each "Hamlet" character using .loc
hamlet_characters.loc[:, 'decade'] = (hamlet_characters['year'] // 10) * 10

# Group the data by decade and count the number of "Hamlet" characters in each decade and plot them
hamlet_decade_counts = hamlet_characters['decade'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(hamlet_decade_counts.index, hamlet_decade_counts.values, width=5, align='center')
plt.xlabel('Decade')
plt.ylabel('Number of "Hamlet" Characters')
plt.title('Number of "Hamlet" Characters Each Decade')
plt.xticks(hamlet_decade_counts.index, rotation=45)
plt.show()


# # 7. What are the 11 most common character names in movie history?

# In[64]:


top_11_common_characters = cast['character'].value_counts().head(11)
print("The 11 most common character names in movie history are:")
print(top_11_common_characters)


# # 8. Who are the 10 people most often credited as "Herself" in film history?

# In[65]:


herself_characters = cast[cast['character'] == 'Herself']
top_10_herself_actors = herself_characters['name'].value_counts().head(10)
print("The 10 people most often credited as 'Herself' in film history are:")
print(top_10_herself_actors)


# # 9. Who are the 10 people most often credited as "Himself" in film history?

# In[66]:


himself_characters = cast[cast['character'] == 'Himself']
top_10_himself_actors = himself_characters['name'].value_counts().head(10)
print("The 10 people most often credited as 'Himself' in film history are:")
print(top_10_himself_actors)


# # 10. Which actors or actresses appeared in the most movies in the year 1945? 

# In[70]:


# Filter the DataFrame for movies released in the year 1945
movies_1945 = cast[cast['year'] == 1945]

# Count the appearances of each actor/actress in 1945 and get the top actor/actress
top_actor_1945 = movies_1945['name'].value_counts().idxmax()

# Get the number of movies in which the top actor/actress appeared in 1945
num_movies_1945 = movies_1945['name'].value_counts().max()

print('The actor or actress who appeared in the most movies in 1945 is',top_actor_1945,'with',num_movies_1945,'movies.')


# # 11. Which actors or actresses appeared in the most movies in the year 1985?

# In[71]:


# Filter the DataFrame for movies released in the year 1985
movies_1985 = cast[cast['year'] == 1985]

# Count the appearances of each actor/actress in 1985 and get the top actor/actress
top_actor_1985 = movies_1985['name'].value_counts().idxmax()

# Get the number of movies in which the top actor/actress appeared in 1985
num_movies_1985 = movies_1985['name'].value_counts().max()

print('The actor or actress who appeared in the most movies in 1985 is',top_actor_1985,'with',num_movies_1985,'movies.')


# # 12. Plot how many roles Mammootty has played in each year of his career.

# In[72]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for roles played by Mammootty
mammootty_roles = cast[cast['name'] == 'Mammootty']

# Group the data by year and count the number of roles played by Mammootty in each year and plot them
roles_per_year = mammootty_roles['year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.plot(roles_per_year.index, roles_per_year.values, marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Number of Roles')
plt.title('Number of Roles Played by Mammootty Each Year')
plt.grid(True)
plt.show()


# # 13. What are the 10 most frequent roles that start with the phrase "Patron In"?

# In[73]:


# Filter the DataFrame for roles that start with "Patron In"
patron_in_roles = cast[cast['character'].str.startswith('Patron In')]

# Count the occurrences of each "Patron In" role and get the top 10 most frequent roles
top_10_patron_in_roles = patron_in_roles['character'].value_counts().head(10)

print("The 10 most frequent roles that start with 'Patron In' are:")
print(top_10_patron_in_roles)


# # 14. What are the 10 most frequent roles that start with the word "Science"?

# In[74]:


# Filter the DataFrame for roles that start with "Science"
science_roles = cast[cast['character'].str.startswith('Science')]

# Count the occurrences of each "Science" role and get the top 10 most frequent roles
top_10_science_roles = science_roles['character'].value_counts().head(10)

print("The 10 most frequent roles that start with 'Science' are:")
print(top_10_science_roles)


# # 15. Plot the n-values of the roles that Judi Dench has played over her career.

# In[75]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for roles played by Judi Dench
judi_dench_roles = cast[cast['name'] == 'Judi Dench'].copy()

# Convert the 'n' column to strings
judi_dench_roles['n'] = judi_dench_roles['n'].astype(str)

# Filter out rows where 'n' is numeric (exclude non-numeric values)
judi_dench_roles = judi_dench_roles[~judi_dench_roles['n'].str.isnumeric()]

# Convert the 'n' column back to numeric
judi_dench_roles['n'] = pd.to_numeric(judi_dench_roles['n'], errors='coerce')

# Plot the n-values of the roles played by Judi Dench
plt.figure(figsize=(12, 6))
plt.plot(judi_dench_roles['year'], judi_dench_roles['n'], marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('n-value')
plt.title('n-values of Roles Played by Judi Dench Over Her Career')
plt.grid(True)
plt.show()


# # 16. Plot the n-values of Cary Grant's roles through his career.

# In[76]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the cast dataset (assuming you have it in a file named 'cast.csv')
cast = pd.read_csv('cast.csv')

# Filter the 'cast' DataFrame to select only roles played by "Cary Grant"
cary_grant_roles = cast[cast['name'] == 'Cary Grant']

# Create a new DataFrame with valid 'n' values
cary_grant_roles_with_n = cary_grant_roles[cary_grant_roles['n'].notna()].copy()

# Convert the 'n' column to numeric (in case it's not already)
cary_grant_roles_with_n['n'] = pd.to_numeric(cary_grant_roles_with_n['n'], errors='coerce')

# Plot the 'n' values of the roles played by Cary Grant over his career
plt.figure(figsize=(10, 6))
plt.plot(cary_grant_roles_with_n['year'], cary_grant_roles_with_n['n'], marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('n-Value')
plt.title('n-Values of Roles Played by Cary Grant Over His Career')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# # 17. Plot the n-value of the roles that Sidney Poitier has acted over the years.

# In[77]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the cast dataset (assuming you have it in a file named 'cast.csv')
cast = pd.read_csv('cast.csv')

# Filter the 'cast' DataFrame to select only roles played by "Sidney Poitier"
sidney_poitier_roles = cast[cast['name'] == 'Sidney Poitier']

# Create a new DataFrame with valid 'n' values
sidney_poitier_roles_with_n = sidney_poitier_roles[sidney_poitier_roles['n'].notna()].copy()

# Convert the 'n' column to numeric (in case it's not already)
sidney_poitier_roles_with_n['n'] = pd.to_numeric(sidney_poitier_roles_with_n['n'], errors='coerce')

# Plot the 'n' values of the roles played by Sidney Poitier over the years
plt.figure(figsize=(10, 6))
plt.plot(sidney_poitier_roles_with_n['year'], sidney_poitier_roles_with_n['n'], marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('n-Value')
plt.title('n-Values of Roles Played by Sidney Poitier Over His Career')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# # 18. How many leading (n=1) roles were available to actors, and how many to actresses, in the 1950s?

# In[78]:


# Filter the DataFrame for roles in the 1950s
roles_in_1950s = cast[(cast['year'] >= 1950) & (cast['year'] <= 1959)]

# Count the number of leading roles (n=1) for actors and actresses separately
leading_roles_actors = len(roles_in_1950s[(roles_in_1950s['n'] == 1) & (roles_in_1950s['type'] == 'actor')])
leading_roles_actresses = len(roles_in_1950s[(roles_in_1950s['n'] == 1) & (roles_in_1950s['type'] == 'actress')])

print("The number of leading roles for actors in the 1950s:", leading_roles_actors)
print("The number of leading roles for actresses in the 1950s:", leading_roles_actresses)


# # 19. How many supporting (n=2) roles were available to actors, and how many to actresses, in the 1950s?

# In[79]:


# Filter the DataFrame for roles in the 1950s
roles_in_1950s = cast[(cast['year'] >= 1950) & (cast['year'] <= 1959)]

# Count the number of supporting roles (n=2) for actors and actresses separately
supporting_roles_actors = len(roles_in_1950s[(roles_in_1950s['n'] == 2) & (roles_in_1950s['type'] == 'actor')])
supporting_roles_actresses = len(roles_in_1950s[(roles_in_1950s['n'] == 2) & (roles_in_1950s['type'] == 'actress')])

print("The number of supporting roles for actors in the 1950s:", supporting_roles_actors)
print("The number of supporting roles for actresses in the 1950s:", supporting_roles_actresses)


# # EXERCISE - 3

# In[80]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[ ]:


from IPython.core.display import HTML
css open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# In[81]:


titles = pd.read_csv('titles.csv', index_col = None)
titles.head()


# In[82]:


cast = pd.read_csv('cast.csv', index_col = None)
cast.head()


# # 1. Using groupby(), plot the number of films that have been released each decade in the history of cinema.

# In[83]:


import pandas as pd
import matplotlib.pyplot as plt

# Group the DataFrame by decade and count the number of films in each decade
decade_counts = titles.groupby((titles['year'] // 10) * 10)['title'].count()

# Create a bar plot to visualize the number of films released each decade
plt.figure(figsize=(12, 6))
decade_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Decade')
plt.ylabel('Number of Films')
plt.title('Number of Films Released Each Decade in the History of Cinema')
plt.xticks(rotation=45)
plt.show()


# # 2. Use groupby() to plot the number of "Hamlet" films made each decade.

# In[84]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for "Hamlet" films
hamlet_movies = titles[titles['title'] == 'Hamlet']

# Group the filtered DataFrame by decade and count the number of "Hamlet" films in each decade
hamlet_decade_counts = hamlet_movies.groupby((hamlet_movies['year'] // 10) * 10)['title'].count()

# Create a bar plot to visualize the number of "Hamlet" films made each decade
plt.figure(figsize=(12, 6))
hamlet_decade_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Decade')
plt.ylabel('Number of "Hamlet" Films')
plt.title('Number of "Hamlet" Films Made Each Decade')
plt.xticks(rotation=45)
plt.show()


# # 3. How many leading (n=1) roles were available to actors, and how many to actresses, in each year of the 1950s?

# In[85]:


# Filter the DataFrame for roles in the 1950s
roles_in_1950s = cast[(cast['year'] >= 1950) & (cast['year'] <= 1959)]

# Create a DataFrame to count leading roles for actors and actresses separately
leading_roles_counts = roles_in_1950s[(roles_in_1950s['n'] == 1)].groupby(['year', 'type'])['n'].count().unstack(fill_value=0)

print("Leading roles (n=1) for actors and actresses in each year of the 1950s:")
print(leading_roles_counts)


# # 4. In the 1950s decade taken as a whole, how many total roles were available to actors, and how many to actresses, for each "n" number 1 through 5?

# In[87]:


# Convert the "year" column to numeric
cast['year'] = pd.to_numeric(cast['year'], errors='coerce')

# Filter the DataFrame for roles in the 1950s decade (1950-1959)
roles_in_1950s = cast[(cast['year'] >= 1950) & (cast['year'] <= 1959)]

# Filter roles for "n" values 1 through 5
roles_n_1_to_5 = roles_in_1950s[roles_in_1950s['n'].isin([1, 2, 3, 4, 5])]

# Group the roles by gender (actor/actress) and "n" number and count the occurrences
roles_count_by_gender_n = roles_n_1_to_5.groupby(['type', 'n']).size().unstack(fill_value=0)

# Extract the counts for actors and actresses
actors_count_by_n = roles_count_by_gender_n.loc['actor']
actresses_count_by_n = roles_count_by_gender_n.loc['actress']

print("Total roles available to actors and actresses for each 'n' number 1 through 5 in the 1950s:")
print("n=1:", actors_count_by_n[1], "roles for actors and", actresses_count_by_n[1], "roles for actresses")
print("n=2:", actors_count_by_n[2], "roles for actors and", actresses_count_by_n[2], "roles for actresses")
print("n=3:", actors_count_by_n[3], "roles for actors and", actresses_count_by_n[3], "roles for actresses")
print("n=4:", actors_count_by_n[4], "roles for actors and", actresses_count_by_n[4], "roles for actresses")
print("n=5:", actors_count_by_n[5], "roles for actors and", actresses_count_by_n[5], "roles for actresses")


# # 5. Use groupby() to determine how many roles are listed for each of the Pink Panther movies.

# In[91]:


# Filter the DataFrame for movies with "Pink Panther" in the title
pink_panther_movies = cast[cast['title'].str.contains('Pink Panther', case=False)]

# Group the data by movie title and count the number of roles for each movie
roles_count_by_movie = pink_panther_movies.groupby('title')['character'].count().reset_index()

print("Roles listed for each of the Pink Panther movies:")
print(roles_count_by_movie)


# # 6. List, in order by year, each of the films in which Frank Oz has played more than 1 role.

# In[92]:


# Filter the DataFrame for roles played by Frank Oz
frank_oz_roles = cast[cast['name'] == 'Frank Oz']

# Group the roles by movie title and year and count the number of roles in each group
roles_count_by_movie_year = frank_oz_roles.groupby(['title', 'year']).size().reset_index(name='role_count')

# Filter for movies where Frank Oz played more than one role
movies_with_multiple_roles = roles_count_by_movie_year[roles_count_by_movie_year['role_count'] > 1]

# Sort the result by year
movies_with_multiple_roles_sorted = movies_with_multiple_roles.sort_values(by='year')

print("Films in which Frank Oz has played more than 1 role, sorted by year:")
print(movies_with_multiple_roles_sorted)


# # 7. List each of the characters that Frank Oz has portrayed at least twice.

# In[94]:


# Filter the DataFrame for roles played by Frank Oz
frank_oz_roles = cast[cast['name'] == 'Frank Oz']

# Group the roles by character and count the number of times each character appears
character_counts = frank_oz_roles['character'].value_counts()

# Filter for characters that Frank Oz has portrayed at least twice
characters_at_least_twice = character_counts[character_counts >= 2]

print("Characters portrayed by Frank Oz at least twice:")
print(characters_at_least_twice)


# # EXERCISE - 4

# In[95]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[ ]:


from IPython.core.display import HTML
css open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# In[97]:


titles = pd.read_csv('titles.csv', index_col = None)
titles.head()


# In[98]:


cast = pd.read_csv('cast.csv', index_col = None)
cast.head()


# # 1. Define a year as a "Superman year" whose films feature more Superman characters than Batman. How many years in film history have been Superman years?

# In[100]:


# Filter the DataFrame for roles related to both Superman and Batman characters
superman_batman_roles = cast[cast['character'].str.contains('Superman|Batman', case=False, regex=True)]

# Group the data by year and count the number of Superman and Batman characters in each year
character_counts_by_year = superman_batman_roles.groupby(['year', 'character']).size().unstack(fill_value=0)

# Determine which years have more Superman characters than Batman characters
superman_years = character_counts_by_year[character_counts_by_year['Superman'] > character_counts_by_year['Batman']]

# Count the number of years meeting the criteria
num_superman_years = len(superman_years)

print('Number of "Superman year" in film history:', num_superman_years)


# # 2. How many years have been "Batman years", with more Batman characters than Superman characters?

# In[102]:


# Filter the DataFrame for roles related to both Superman and Batman characters
superman_batman_roles = cast[cast['character'].str.contains('Superman|Batman', case=False, regex=True)]

# Group the data by year and count the number of Superman and Batman characters in each year
character_counts_by_year = superman_batman_roles.groupby(['year', 'character']).size().unstack(fill_value=0)

# Determine which years have more Batman characters than Superman characters
batman_years = character_counts_by_year[character_counts_by_year['Batman'] > character_counts_by_year['Superman']]

# Count the number of years meeting the criteria
num_batman_years = len(batman_years)

print('Number of "Batman years" in film history:', num_batman_years)


# # 3. Plot the number of actor roles each year and the number of actress roles each year over the history of film.

# In[103]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for actor and actress roles
actor_roles = cast[cast['type'] == 'actor']
actress_roles = cast[cast['type'] == 'actress']

# Group the data by year and count the number of actor and actress roles in each year
actor_counts_by_year = actor_roles.groupby('year').size()
actress_counts_by_year = actress_roles.groupby('year').size()

# Create a plot
plt.figure(figsize=(12, 6))
plt.plot(actor_counts_by_year.index, actor_counts_by_year.values, label='Actor Roles', marker='o', linestyle='-', color='blue')
plt.plot(actress_counts_by_year.index, actress_counts_by_year.values, label='Actress Roles', marker='o', linestyle='-', color='red')

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('Number of Roles')
plt.title('Number of Actor and Actress Roles Each Year')
plt.legend()
plt.grid(True)
plt.show()


# # 4. Plot the number of actor roles each year and the number of actress roles each year, but this time as a kind='area' plot.

# In[104]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for actor and actress roles
actor_roles = cast[cast['type'] == 'actor']
actress_roles = cast[cast['type'] == 'actress']

# Group the data by year and count the number of actor and actress roles in each year
actor_counts_by_year = actor_roles.groupby('year').size()
actress_counts_by_year = actress_roles.groupby('year').size()

# Create an area plot
plt.figure(figsize=(12, 6))
plt.fill_between(actor_counts_by_year.index, actor_counts_by_year.values, alpha=0.5, label='Actor Roles', color='blue')
plt.fill_between(actress_counts_by_year.index, actress_counts_by_year.values, alpha=0.5, label='Actress Roles', color='red')

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('Number of Roles')
plt.title('Number of Actor and Actress Roles Each Year (Area Plot)')
plt.legend()
plt.grid(True)
plt.show()


# # 5. Plot the difference between the number of actor roles each year and the number of actress roles each year over the history of film.

# In[109]:


import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'cast' is your DataFrame
# Assuming your DataFrame has a 'year' column representing release years
# and a 'type' column representing actor or actress

# Filter the DataFrame for actor and actress roles
actor_roles = cast[cast['type'] == 'actor']
actress_roles = cast[cast['type'] == 'actress']

# Group the data by year and count the roles for actors and actresses separately
actor_roles_by_year = actor_roles.groupby('year')['type'].count()
actress_roles_by_year = actress_roles.groupby('year')['type'].count()

# Calculate the difference between actor and actress roles each year
role_difference = actor_roles_by_year - actress_roles_by_year

# Create a plot
plt.figure(figsize=(12, 6))

# Plot the role difference
plt.plot(role_difference.index, role_difference.values, label='Actor Roles - Actress Roles', color='green')

# Add labels and a legend
plt.xlabel('Year')
plt.ylabel('Difference in Number of Roles')
plt.title('Difference Between Actor and Actress Roles Over the Years')
plt.legend()

# Show the plot
plt.grid()
plt.show()


# # 6. Plot the fraction of roles that have been 'actor' roles each year in the history of film.

# In[105]:


import pandas as pd
import matplotlib.pyplot as plt

# Group the data by year and calculate the fraction of 'actor' roles each year
total_roles_by_year = cast.groupby('year').size()
actor_roles_by_year = cast[cast['type'] == 'actor'].groupby('year').size()
fraction_actor_roles_by_year = actor_roles_by_year / total_roles_by_year

# Create a plot
plt.figure(figsize=(12, 6))
plt.plot(fraction_actor_roles_by_year.index, fraction_actor_roles_by_year.values, marker='o', linestyle='-', color='blue')

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('Fraction of Actor Roles')
plt.title('Fraction of Actor Roles Each Year in Film History')
plt.grid(True)
plt.show()


# # 7. Plot the fraction of supporting (n=2) roles that have been 'actor' roles each year in the history of film.

# In[106]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for supporting roles (n=2)
supporting_roles = cast[cast['n'] == 2]

# Group the data by year and calculate the fraction of 'actor' supporting roles each year
total_supporting_roles_by_year = supporting_roles.groupby('year').size()
actor_supporting_roles_by_year = supporting_roles[supporting_roles['type'] == 'actor'].groupby('year').size()
fraction_actor_supporting_roles_by_year = actor_supporting_roles_by_year / total_supporting_roles_by_year

# Create a plot
plt.figure(figsize=(12, 6))
plt.plot(fraction_actor_supporting_roles_by_year.index, fraction_actor_supporting_roles_by_year.values, marker='o', linestyle='-', color='blue')

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('Fraction of Actor Supporting Roles (n=2)')
plt.title('Fraction of Actor Supporting Roles (n=2) Each Year in Film History')
plt.grid(True)
plt.show()


# # 8. Build a plot with a line for each rank n=1 through n=3, where the line shows what fraction of that rank's roles were 'actor' roles for each year in the history of film.

# In[107]:


import pandas as pd
import matplotlib.pyplot as plt

# Define a list of ranks (n=1, n=2, n=3)
ranks = [1, 2, 3]

# Create a plot for each rank
plt.figure(figsize=(12, 6))

for rank in ranks:
    # Filter the DataFrame for roles with the specified rank
    roles = cast[cast['n'] == rank]

    # Group the data by year and calculate the fraction of 'actor' roles for each year
    total_roles_by_year = roles.groupby('year').size()
    actor_roles_by_year = roles[roles['type'] == 'actor'].groupby('year').size()
    fraction_actor_roles_by_year = actor_roles_by_year / total_roles_by_year

    # Plot the line for the current rank
    plt.plot(fraction_actor_roles_by_year.index, fraction_actor_roles_by_year.values, marker='o', label=f'n={rank}')

# Set plot labels and title
plt.xlabel('Year')
plt.ylabel('Fraction of Actor Roles')
plt.title('Fraction of Actor Roles for Ranks n=1, n=2, and n=3 Each Year in Film History')
plt.legend()
plt.grid(True)
plt.show()


# # EXERCISE - 5

# In[108]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[ ]:


from IPython.core.display import HTML
css open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# In[109]:


cast = pd.read_csv('cast.csv', index_col = None)
cast.head()


# In[110]:


release_dates = pd.read_csv('release_dates.csv', parse_dates=['date'], infer_datetime_format=True)
release_dates.head()


# # 1. Make a bar plot of the months in which movies with "Christmas" in their title tend to be released in the USA.

# In[116]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for movies with "Christmas" in their title and released in the USA
christmas_movies_usa = release_dates[(release_dates['title'].str.contains('Christmas', case=False)) & (release_dates['country'] == 'USA')].copy()

# Extract the release month from the 'date' column and create a new 'month' column
christmas_movies_usa['month'] = christmas_movies_usa['date'].dt.month

# Count the number of movies released in each month
monthly_counts = christmas_movies_usa['month'].value_counts().sort_index()

# Define the month names for labeling the x-axis
month_names = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 
               'October', 'November', 'December' ]

# Create a bar plot with all twelve months
plt.figure(figsize=(10, 6))
plt.bar(month_names, [monthly_counts.get(month, 0) for month in range(1, 13)], color='skyblue')
plt.xlabel('Month')
plt.ylabel('Number of Christmas Movies')
plt.title('Number of Christmas Movies Released Each Month in the USA')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# # 2. Make a bar plot of the months in which movies whose titles start with "The Hobbit" are released in the USA.

# In[122]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for movies whose titles start with "The Hobbit" and were released in the USA
hobbit_movies_usa = release_dates[(release_dates['title'].str.startswith('The Hobbit')) & (release_dates['country'] == 'USA')].copy()

# Extract the release month from the 'date' column and create a new 'month' column
hobbit_movies_usa['month'] = hobbit_movies_usa['date'].dt.month

# Count the number of movies released in each month
monthly_counts = hobbit_movies_usa['month'].value_counts().sort_index()

# Define the month names for labeling the x-axis
month_names = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
               'October', 'November', 'December']

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(month_names, monthly_counts, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Number of "The Hobbit" Movies')
plt.title('Number of "The Hobbit" Movies Released Each Month in the USA')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# # 3. Make a bar plot of the day of the week on which movies with "Romance" in their title tend to be released in the USA.

# In[127]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for movies with "Romance" in their title and released in the USA
romance_movies_usa = release_dates[(release_dates['title'].str.contains('Romance', case=False)) & (release_dates['country'] == 'USA')].copy()

# Extract the day of the week from the 'date' column and create a new 'day_of_week' column (0=Monday, 1=Tuesday, ..., 6=Sunday)
romance_movies_usa['day_of_week'] = romance_movies_usa['date'].dt.dayofweek

# Count the number of movies released on each day of the week
day_counts = romance_movies_usa['day_of_week'].value_counts().sort_index()

# Define the day of the week names for labeling the x-axis
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(day_names, day_counts, color='pink')
plt.xlabel('Day of the Week')
plt.ylabel('Number of "Romance" Movies')
plt.title('Number of "Romance" Movies Released on Each Day of the Week in the USA')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# # 4. Make a bar plot of the day of the week on which movies with "Action" in their title tend to be released in the USA.

# In[135]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter the DataFrame for movies with "Action" in their title and released in the USA
action_movies_usa = release_dates[(release_dates['title'].str.contains('Action', case=False)) & (release_dates['country'] == 'USA')].copy()

# Extract the day of the week from the 'date' column and create a new 'day_of_week' column (0=Monday, 1=Tuesday, ..., 6=Sunday)
action_movies_usa['day_of_week'] = action_movies_usa['date'].dt.dayofweek

# Count the number of movies released on each day of the week
day_counts = action_movies_usa['day_of_week'].value_counts().sort_index()

# Define the day of the week names for labeling the x-axis
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create a bar plot with reduced bar width
plt.figure(figsize=(10, 6))
plt.bar(day_names, day_counts, color='skyblue', width=0.4)  # Adjust the width here
plt.xlabel('Day of the Week')
plt.ylabel('Number of "Action" Movies')
plt.title('Number of "Action" Movies Released on Each Day of the Week in the USA')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# # 5. On which date was each Judi Dench movie from the 1990s released in the USA?

# In[141]:


# Filter movies starring Judi Dench in the 1990s
judi_dench_movies_1990s = cast[(cast['name'] == 'Judi Dench') & (cast['year'] >= 1990) & (cast['year'] <= 1999)]

# Merge with release_dates to get the release date in the USA
judi_dench_movies_1990s_usa = pd.merge(judi_dench_movies_1990s, release_dates[release_dates['country'] == 'USA'], on=['title', 'year'])

# Extract relevant columns and display the result
result = judi_dench_movies_1990s_usa[['title', 'year', 'date']]
print(result)


# # 6. In which months do films with Judi Dench tend to be released in the USA?

# In[152]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter movies starring Judi Dench
judi_dench_movies = cast[cast['name'] == 'Judi Dench']

# Merge with release_dates to get the release month
judi_dench_movies = pd.merge(judi_dench_movies, release_dates, on=['title', 'year'])

# Filter for movies released in the USA
judi_dench_movies_usa = judi_dench_movies[judi_dench_movies['country'] == 'USA']

# Create a copy of the DataFrame and extract the release month from the date
judi_dench_movies_usa = judi_dench_movies_usa.copy()
judi_dench_movies_usa['release_month'] = judi_dench_movies_usa['date'].dt.month

# Group by release month and count the number of movies released in each month
release_month_counts = judi_dench_movies_usa['release_month'].value_counts().sort_index()

# Plot the results as a bar chart
plt.figure(figsize=(10, 6))
release_month_counts.plot(kind='bar', color='skyblue')
plt.title("Judi Dench Movies Released in the USA by Month")
plt.xlabel("Month")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.show()


# # 7. In which months do films with Tom Cruise tend to be released in the USA?

# In[156]:


import pandas as pd
import matplotlib.pyplot as plt

# Filter movies starring Tom Cruise
tom_cruise_movies = cast[cast['name'] == 'Tom Cruise']

# Merge with release_dates to get the release month
tom_cruise_movies = pd.merge(tom_cruise_movies, release_dates, on=['title', 'year'])

# Filter for movies released in the USA
tom_cruise_movies_usa = tom_cruise_movies[tom_cruise_movies['country'] == 'USA']

# Create a copy of the DataFrame and extract the release month from the date
tom_cruise_movies_usa = tom_cruise_movies_usa.copy()

# Extract the release month from the date
tom_cruise_movies_usa['release_month'] = tom_cruise_movies_usa['date'].dt.month

# Group by release month and count the number of movies released in each month
release_month_counts = tom_cruise_movies_usa['release_month'].value_counts().sort_index()

# Plot the results as a bar chart
plt.figure(figsize=(10, 6))
release_month_counts.plot(kind='bar', color='orange')
plt.title("Tom Cruise Movies Released in the USA by Month")
plt.xlabel("Month")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.show()

