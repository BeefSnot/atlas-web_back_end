-- Lists all bands with Glam rock as their main style, ranked by longevity
SELECT
    band_name, 
    IFNULL(split, 2024) - formed as lifespan
FROM
    metal_bands
WHERE
    FIND_IN_SET('Glam rock', style)
ORDER BY
    lifespan DESC;