#fuction file for the csv interaction 
import csv

def save_csv_file_func(array_of_data_point,file_name):

    # writing csv file
    # https://www.youtube.com/watch?v=q5uM4VKywbA&ab_channel=CoreySchafer

    with open(file_name,'w') as output_file:      # output_file is a variable for the file being exported w means write
        csv_writer = csv.writer(output_file, delimiter=',')  # assigning a variable to control the format of the file exported

        csv_writer.writerow(['X Coordinate','Y Coordinate','Measurement Value','Measurement Units','Percentage Remaining'])
        for line in array_of_data_point:                      # looping through the lines in the test matrix
            csv_writer.writerow([line.x_coordinate,line.y_coordinate,line.measurement, line.units,line.percentage])                       # writing rows into the csv file 
