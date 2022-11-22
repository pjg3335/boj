SELECT
    DATE_FORMAT(T.SALES_DATE, '%Y-%m-%d') as SALES_DATE,
    T.PRODUCT_ID,
    T.USER_ID,
    T.SALES_AMOUNT
FROM (
    SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    FROM ONLINE_SALE
    UNION ALL
    SELECT SALES_DATE, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT
    FROM OFFLINE_SALE) T
WHERE YEAR(T.SALES_DATE)=2022 and MONTH(T.SALES_DATE)=3
ORDER BY T.SALES_DATE, T.PRODUCT_ID, T.USER_ID
