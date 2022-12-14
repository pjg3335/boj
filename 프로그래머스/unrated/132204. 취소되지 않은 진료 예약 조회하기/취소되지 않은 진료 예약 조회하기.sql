-- 코드를 입력하세요
SELECT
    A.APNT_NO,
    B.PT_NAME,
    A.PT_NO,
    A.MCDP_CD,
    C.DR_NAME,
    A.APNT_YMD
FROM (
    SELECT MCDP_CD, APNT_NO, PT_NO, APNT_YMD, MDDR_ID
    FROM APPOINTMENT 
    WHERE MCDP_CD='CS' and APNT_CNCL_YN='N' and DATE_FORMAT(APNT_YMD, '%Y-%m-%d')='2022-04-13') A
    JOIN PATIENT B
    ON A.PT_NO = B.PT_NO
    JOIN DOCTOR C
    ON A.MDDR_ID = C.DR_ID
ORDER BY A.APNT_YMD;
