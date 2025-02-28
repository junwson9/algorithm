-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(date_of_birth, '%Y-%m-%d') DATE_OF_BIRTH
from member_profile
where substring(date_of_birth, 6,2) = '03'
and tlno is not null
and gender = 'W'
order by member_id
