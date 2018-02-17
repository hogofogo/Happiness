# SF_Trees

Data is from Kaggle, is simplistic and really not the point here.

Here, I simply wanted to experiment whether a Python script would run from RMarkdown, which it did, and to show graphical representation of the results. 

Python_markdown runs Python script from R Markdown.
- It takes 3 files with world population data (happiness index, GDP per capita, corruption index, etc) for 2015, 2016 and 2017
- Cleans data and makes it internally consistent
- Saves clean data file as ?happiness_data.csv?
- Aggregates average GDP per capita and happiness index and groups is by region
- Creates and saves graphs
- Creates a markdown *.html file

Happiness_2d_density_plots takes output from the Python_markdown and builds additional graphs in R

For results, see .html and .pdf files.