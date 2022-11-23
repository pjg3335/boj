-- 코드를 입력하세요
SELECT 
    A.ANIMAL_ID, 
    A.NAME
FROM ANIMAL_OUTS A
    LEFT OUTER JOIN ANIMAL_INS B
    USING(ANIMAL_ID)
WHERE B.INTAKE_CONDITION IS NULL
ORDER BY A.ANIMAL_ID;