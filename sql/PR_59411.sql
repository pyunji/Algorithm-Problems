-- 코드를 입력하세요
SELECT o.animal_id, o.name
from animal_outs as o
    left join animal_ins as i using(animal_id)
order by o.datetime - i.datetime desc
limit 2;