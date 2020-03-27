# CombineIntoCsv
Write a code in Python (ideally) to combine several (txt OR csv) file into 1 csv (1 column per file)

## Brief background about me:
Hi all, I am a Research Technician in Biology, but Covid-19 force me to work from home.
I am using that time to code Solution to process my datas.
I was all happy with my first macro, half recorded on Fiji, half written by myself. 
But I also realize how limited I am. I am learning Python (and more) using Codecademy but also want to learn by trying to apply it to a problem I have. 
I'll record here my tests/progress (if any). 
***I would be very happy to get help to learn while coding my first Python code to process my data !***
(so it won't take me a year to get there because this is a first step...)

## My current issue is:
(File CICg_03) : Ok, I somehow managed to make a data frame with 3 columns with my data in it ? But output weird... See image

## Initial idea:
I have a Folder named "Results_txt" which contain x folders which contain (1 to 3) files, as follow:
- Results
   - Folder1
     - Folder1A.txt
	 - Folder1C.txt
	 - Folder1T.txt
   - Folder2
	 - Folder2C.txt
   - Folder3
     - Folder3A.txt
	 - Folder3C.txt
	 - Folder3T.txt
	 
I also have the same files as .csv in "Results_csv" just in case it makes it easier...

***Important notes:
The txt/csv files have the same name than the folders + a letter that differenciate these (up to 3) files.
There will always be a file "C". Sometimes only "A" or only "T" with it. Sometimes all 3 "A", "C", "T".
The data in these files is just one column, with "Value" on top and then various numbers.
All (up to 3) files (A, C and T) should have the same number of rows. If not, the processing shouldn't be done.***


## The goal:
The "perfect" goal is to:
- copy the data from "Folder1C.txt", paste it as 1 column in column 1 of a new CSV file
- if any, copy the data from "Folder1A.txt", paste it as 1 column in column 2 of a new CSV file
- if any, copy the data from "Folder1T.txt", paste it as 1 column in column 3 of a new CSV file
- save the new CSV file as Folder1_combined.csv
