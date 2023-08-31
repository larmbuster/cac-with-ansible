#!/usr/bin/python

################################################################
# STIG ID Scraper                                              #
################################################################
# Purpose:                                                     #
# This script loops through each line in a main.yml tasks file #
# and finds each unique STIG ID that it then writes to a file. #
################################################################

def main():

    def stigID_scraper():
        ###variables used by script
        #path to task file
        ansible_task_file = open('./main.yml', 'r')
        #script writes results to file
        stigID_list_file = open('./stigID_list.txt', 'w+')
        #empty list for STIG IDs
        stigID_list = []
        #string used for matching correct line
        line_matcher = "DISA-STIG-RHEL-08-"

        #loop through each line
        for line in ansible_task_file:
            if line_matcher in line:
                #remove leading dash from line
                stigID_line_clean= line.replace('-', '',1)
                #remove spaces from line
                stigID_line_clean = stigID_line_clean.strip()
                #add STIG ID only if it is not already in stigID_list
                if stigID_line_clean not in stigID_list:
                    stigID_list.append(stigID_line_clean)
                else:
                    continue
            else:
                continue
        #write all STIG IDs in stigID_list to file
        for stigID in stigID_list:
            stigID_list_file.write(stigID)
            #adds a new line
            stigID_list_file.write('\n')

    #call function
    stigID_scraper()

if __name__ == "__main__":
    main()