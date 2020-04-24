# oneFCAssignment

This is a repo is for the oneFc assignment probs:

## Probs:
1. SQL: 


One Championship conducts events in a stadium, each event many people visit it and the stats are saved as these columns: id, event_name, people_count
Take leverage in adding sample data yourself.
Please write a query to display the records which have 3 or more consecutive events and the amount of people more than 100(inclusive).

2. Data Parsing: 
Write code to extract data from **data.csv**.


The data contains four columns. The first column is the person identifier. The second column is the datetime the person entered the floor. The third column is the floor the person accessed. The fourth column specifies the building the floor is in.



Each row is considered a floor access event. Your task it to output each floor access event in json format. Each event should comply with the schema located in **schema.json**.


## How To Access Results:

- The data files are available on the directory "data"
- For the first problem(sql) the sql query is added as a sql file inside results folder , the file name is : porb_1_sql_query.sql
- For the second problem(data parsing) find run the python file inside results folder, the file name is : prob_2_data_parsing.py , it will give you some sample records as well as it will dump the entire json results into the file json_output_floor_event.json inside data folder
