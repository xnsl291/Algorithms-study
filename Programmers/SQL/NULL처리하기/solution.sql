-- https://school.programmers.co.kr/learn/courses/30/lessons/59410
SELECT ANIMAL_TYPE, 
    CASE WHEN NAME IS NULL THEN "No name"
    ELSE NAME END AS NAME
    , SEX_UPON_INTAKE FROM ANIMAL_INS 
