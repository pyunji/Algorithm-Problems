-- 코드를 입력하세요
# GROUP BY가 SELECT 보다 먼저 실행 되지만, SELECT의 alias를 사용할 수 있다. (DBMS가 알아서 해줌. mysql 기준)
# GROUP BY, HAVING, ORDER BY에서 SELECT의 alias를 사용할 수 있다.

select HOUR(datetime) as c, COUNT('c') as COUNT
from animal_outs
group by c
HAVING c BETWEEN 9 AND 19
order by c;