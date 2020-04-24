DELETE FROM championship_table WHERE people_count<100;
SELECT DISTINCT(event_name) FROM(
  (SELECT *
     , row_number() OVER (PARTITION BY event_name) AS rn
FROM  (
   SELECT *
        , row_number() OVER ()
       -  row_number() OVER (PARTITION BY event_name) AS grp
   FROM championship_table))) WHERE rn > 2
