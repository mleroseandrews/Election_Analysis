# Election_Analysis
The purpose of the election was to find the winning candidate and winning county for the Colorado election.  There were only 3 candidates in the election race from 3 difference counties.   Overall there were 369,711 votes cast.   

## Project Overview
There has been a recent local congressional election in Colorado and a Colorado Board of Elections Office employee has requested an audit be done using python as the analysis tool of choice. The requested audit details are as follows:

1. Calculate the total number of votes cast.
2. Obtain a list of all of the candidates who received votes.
3. Calculate the total number of votes each of the candidates received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Format a text document which can be delivered to the Election Commission summarizing the results.  

## Resources
-election_results.csv
-Software - Python 3.7

## Election Audit Results
The analysis of the election show that 
-There were 369,711 total votes cast
-There were 3 candidates: Raymon Anthony Doane, Diana DeGette, & Charles Casper Stockham
The candidate results were:
-Charles Casper Stockham: received 23.0% of the vote - 85,213 votes
-Diana DeGette: received 73.8% of the vote - 272,892 votes
-Raymon Anthony Doane: received 3.1% of the vote - 11,606 votes
## The winner of the election was Diana Degette with 73.8% of the vote and 272,892 total votes

There were 3 counties
-Jefferson with 38,855 votes at 10.5%
-Denver with 306,055 votes at 82.8%
-Arapahoe with 24,801 at 6.7%
## The winning county was Denver county with 82% of the votes and 306,055 total votes 

## Challenge Overview
The election commission can use this script to produce results for any election on a county level.  Multiple elections can not be ran simultaneously, each election would have to be ran independently.  This means that if there was more than one election file or multiple election results within one file the results could not be produced. Adding additional for loops could step through each file to generate results from multiple elections within one data file.  This tool with also not run a national level audit as it is currently written to report data on counties and not states.   National level results could be produced by substituting "county" with "state" in the script.   


