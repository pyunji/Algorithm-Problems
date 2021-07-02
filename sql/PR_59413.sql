with recursive rowgen(h) as (
    select 0
    union all
    select h + 1
    from rowgen
    where h < 23
)

select h, count(datetime)
from rowgen 
    left join animal_outs on h = HOUR(datetime)
group by h
order by h;