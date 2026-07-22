-- Resumen portable una vez cargado synthetic_landings en el motor elegido.
-- El control CHECK y la consulta excluyen registros marcados como inválidos.
CREATE TABLE synthetic_landings (
  date TEXT NOT NULL,
  port TEXT NOT NULL,
  fleet TEXT NOT NULL,
  species TEXT NOT NULL,
  landings_t REAL NOT NULL,
  source_id TEXT PRIMARY KEY,
  quality_flag TEXT NOT NULL CHECK (quality_flag IN ('ok', 'review', 'invalid')),
  CHECK (landings_t >= 0 OR quality_flag = 'invalid')
);

SELECT
  species,
  ROUND(SUM(landings_t), 1) AS landings_t
FROM synthetic_landings
WHERE quality_flag <> 'invalid'
GROUP BY species
ORDER BY species;
