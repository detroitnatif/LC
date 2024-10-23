select contest_id, 
ROUND(COUNT(distinct user_id) / (SELECT COUNT(*) from Users) * 100, 2)
as percentage
from Register
group by contest_id
order by percentage DESC, contest_id ASC