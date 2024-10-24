select start.machine_id,
ROUND(AVG(end.timestamp - start.timestamp), 3) 
AS processing_time
from Activity start 
join Activity end
on start.machine_id = end.machine_id
and start.process_id = end.process_id
and start.activity_type = 'start'
and end.activity_type = 'end'
group by start.machine_id