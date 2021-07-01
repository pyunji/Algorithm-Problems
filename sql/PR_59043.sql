-- 코드를 입력하세요
SELECT o.animal_id, o.name
from animal_outs as o, animal_ins as i
where o.animal_id = i.animal_id and i.datetime > o.datetime
order by i.datetime;