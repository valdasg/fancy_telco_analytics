CREATE EXTENSION IF NOT EXISTS tablefunc;

-- Creating enriched full data report

CREATE TEMP TABLE cell_data AS (
    SELECT s.site_id site_id, s.year , s.month, s.day, c.cell_identity cell_identity, c.frequency_band frequency_band, c.technology technology
    FROM (
        SELECT * FROM gsm
        UNION ALL 
        SELECT * FROM umts
        UNION ALL 
        SELECT * FROM lte
    ) c
    RIGHT JOIN site s
    ON c.site_id = s.site_id
    );

-- Display the report
SELECT
    *
FROM cell_data;

-- Display cells per technology on each site in pivotted format
SELECT
    *
FROM  crosstab(
    'SELECT 
        site_id, technology, count(1)
    FROM cell_data
    GROUP BY 1, 2
    ORDER BY 1'
   ) 
AS (
    site_id int,
    site_GSM_cnt bigint,
    site_UMTS_cnt bigint,
    site_LTE_cnt bigint
    );


-- Number of cells per frequency band on a particular site
SELECT *
FROM crosstab(
    'SELECT 
        site_id, frequency_band, count(cell_identity)
    FROM cell_data
    GROUP BY 1, 2
    ORDER BY 1'
   ) 
AS (
    site_id int,
    frequency_band_G700_by_site bigint,
    frequency_band_G800_by_site bigint,
    frequency_band_G900_by_site bigint,
    frequency_band_G1800_by_site bigint,
    frequency_band_G2100_by_site bigint,
    frequency_band_G2600_by_site bigint
    );

