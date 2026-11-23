Zomato Restaurant Data Analysis

Exploratory data analysis of Zomato restaurant listings to understand ratings, customer votes, online ordering, table booking and pricing, and to turn those patterns into business recommendations.

Objective

Understand customer preferences and restaurant performance, and identify where a restaurant platform can grow.

Tools
Python (pandas, NumPy)
Matplotlib and Seaborn for visualisation
Jupyter / any Python environment
Dataset

zomato_data.csv has 148 listings (145 unique restaurants) with these columns:

Column	Meaning
Restaurant Name	Name of the restaurant
Online_Order	Whether online ordering is available (Yes/No)
Book_Table	Whether table booking is available (Yes/No)
Rate	Rating out of 5 (stored as text, e.g. 4.1/5)
Votes	Number of customer votes
Approx_Cost(For Two People)	Approximate cost for two people
Listed_In(Type)	Restaurant type: Buffet, Cafes, Dining, other
Data cleaning
Converted Rate from text (4.1/5) to a numeric value
Standardised column names
Checked for missing values (none found)
Checked for duplicates. No exact duplicate rows, but Onesta, San Churro Cafe and Cafe Nova appear under two restaurant types, so unique restaurants were counted by name (145)
Questions explored
How many votes does each restaurant type receive?
How many restaurants offer table booking?
Which five restaurants have the most votes?
Is there a relationship between rating and votes?
What is the average rating for each restaurant type?
Which rating is most common?
What is the highest cost for two?
Which restaurant types lack online ordering?
Key findings
Online ordering matters most. Only 39% of restaurants offer it, yet they hold 81% of all votes. They average about 517 votes and a 3.85 rating, against about 76 votes and 3.49 without it.
Dining has the biggest gap. It makes up 75% of listings, and 76 of the 89 restaurants without online ordering are Dining outlets.
Engagement is concentrated. The top five restaurants hold 43% of all votes. 33 restaurants (23%) have zero votes.
Table booking is rare but premium. Only 7 restaurants (5%) offer it, and they average about 710 votes and a 4.1 rating.
Ratings are tightly bunched. Average 3.63, most common 3.8, range 2.6 to 4.6. Rating and votes are moderately correlated (about 0.5).
Higher price goes with higher engagement. Restaurants above ₹600 for two average 505 votes, against 54 for those at ₹300 or less.
Type	Restaurants	Share of votes	Avg votes	Online ordering
Dining	109	57%	187	30%
Cafes	22	15%	251	64%
Buffet	7	8%	433	57%
Other	7	19%	973	71%
Recommendations
Prioritise online-ordering onboarding for Dining outlets.
Feature well-rated, high-vote restaurants in trending placements.
Promote table booking to premium, well-rated restaurants.
Support zero-vote restaurants with visibility and review prompts.
Limitations
One-time snapshot of 145 restaurants, so no trends over time
Votes measure engagement, not orders or revenue
Online ordering and votes are associated, but the data cannot show cause and effect




Author

Krithiga Sai P
