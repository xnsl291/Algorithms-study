-- https://school.programmers.co.kr/learn/courses/30/lessons/144856
SELECT A.AUTHOR_ID	,A.AUTHOR_NAME,	B.CATEGORY, SUM(SALES * PRICE) AS TOTAL_SALES
FROM AUTHOR AS A 
JOIN BOOK AS B ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN BOOK_SALES AS S ON B.BOOK_ID = S.BOOK_ID
WHERE S.SALES_DATE like "2022-01-%"
GROUP BY A.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID , B.CATEGORY DESC


