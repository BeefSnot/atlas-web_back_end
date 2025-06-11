-- A list of all bands with Glam rock as their main style
SELECT
    band_name, 
    IFNULL(split, 2022) - formed as lifespan
FROM
    metal_bands
WHERE
    FIND_IN_SET('Glam rock', style)
ORDER BY
    lifespan DESC;