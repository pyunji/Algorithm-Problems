-- 코드를 입력하세요
with recursive rowgen(h) as(
    select 0
    union all
    select h + 1
    from rowgen
    where h < 23
)

select h, count(datetime)
from rowgen
    left join animal_outs on rowgen.h=hour(animal_outs.datetime)
group by rowgen.h
order by rowgen.h