# ACME_ioet_excersice
Exercise developed for the recruitment process of the vacancy for Python Developer at IOET


#### GOAL
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

#### INPUT DATA
It is a _file.txt_ with this structure for every line: </br>
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00

#### OUTPUT
After compare schedules and days of work the output must be like that: </br>
RENE-SOMEONE: 2 _It means that they worked together 2 days_ </br>

#### APROACH AND SOLUTION
1. Read input data file </br>
2. Select the correct structure considering the next tasks such us: possible combinations beteween workers, compare equal days and compare if the schedule it's equal or is overleap in any range. </br>
3. Get and show the results </br>

For the purpose of this excercise I developed 3 functions: </br>
**open_txt_file** and **set_range_schedules** : in order to set the input data into a dictionary </br>
**is_overleap** : in order to compare schedules and get how many days a couple of workers worked at the same day and the same time</br>

Because the information is an heterogenous string it was necesary to personalize the functions to structure the info in a best way and olso I couldn't use external libraries for this excercise.

### How It Works
For testing the excersice we have 3 files: </br>
1. input_data_ACME_1.txt  _file for first suggested example_
2. input_data_ACME_2.txt _file for second suggested example_
3. input_data_ACME_3.txt _file with minimum sets of data required_

The solution was developed using Python v3.10.0 and there are two files to test the code:
1. **ioet_exercise_Lara.ipynb**: It is a notebook Jupyter that includes the functions already specifieds.
2. **ioet_excercise_Lara.py**: It is a python script with the same code as the first

If you will use the first option, make sure you have Jupyter installed. To get started, all you need to do is open up your terminal application start Jupyter enviroment go to folder where you downloaded the files and open the .ipynb file. Another way to work with this option is upload the corresponding files to [Google Colab](https://colab.research.google.com/?hl=es) and there you can test online.

For the second option, make sure that you have all files in one directory, next open your terminal application and go to the folder where you downloaded the files. Write `ioet_excercise_Lara.py` press Enter et voilà.

To upload a different file, go to the end of either file and rename the file you are going to work with, for example: </br>
`'''Change file name for another test'''` </br>
`file = "input_data_ACME_3.txt"` </br>
`data = open_txt_file(file)` </br>
`result =is_overleap(data)` </br>
`print(result)`

