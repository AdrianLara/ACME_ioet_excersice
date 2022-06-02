# ACME_ioet_excersice
Exercise developed for the recruitment process of the vacant Python Developer at IOET


#### GOAL
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

#### INPUT DATA
It is a _file.txt_ with this structure for every line: </br>
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00

#### OUTPUT
After compare schedules and days of work the output must be like that:
RENE-SOMEONE: 2 _It means that they worked together 2 days_

For the purpose of this excercise I developed 3 functions:
**open_txt_file* and *set_range_schedules*: in order to set the input data into a dictionary
**is_overleap**: in order to compare schedules and get how many days a couple of workers worked at the same day and the same time

#### APROACH AND SOLUTION
1. Read input data file
2. Select the correct structure considering the next tasks such us: possible combinations beteween workers, compare equal days and compare if the schedule it's equal or is overleap in any range.
3. Get and show the results

Because the information is a heterogenous string it was necesary to personalize the functions to structure the info in a best way and olso I couldn't use external libraries for this excercise.

### How It Works
You Have
