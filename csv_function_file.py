#fuction file for the csv interaction 
import csv

def save_csv_file_func(array_of_data_point,file_name):

    # writing csv file
    # https://www.youtube.com/watch?v=q5uM4VKywbA&ab_channel=CoreySchafer

    with open(file_name,'w') as output_file:      # output_file is a variable for the file being exported w means write
        csv_writer = csv.writer(output_file, delimiter=',')  # assigning a variable to control the format of the file exported

        csv_writer.writerow(['scan_area','gate_start','Gate Width','X Coordinate','Y Coordinate','Voltage Reading','Measurement Value','Measurement Units']) # this info needs to be lower case for the open saved data function to work properly
        for line in array_of_data_point:                      # looping through the lines in the test matrix
            csv_writer.writerow([line.scan_file_name, line.gate_start_value, line.gate_width_value, line.x_coordinate, line.y_coordinate, line.voltage_data, line.measurement_thickness, line.units])   # writing rows into the csv file 
