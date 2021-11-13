# PMGchallenge
CSV Combiner
Write a command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. Your script should output a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path). Use filename as the header for the additional column.

Input & Output
We will run your code as follows

$ ./csv_combiner.php ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
However, the CSV files inside the fixtures are not the only files we will run through. We will run your code through files > 2 GB to see if you hit memory limits.

Example
Given two input files named clothing.csv and accessories.csv.

