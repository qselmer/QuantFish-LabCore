# CCPE-022 · Solución orientativa

La solución ejecutable no se duplica aquí. Se conserva en:

- `scripts/python/part-iv/summarize_landings.py`
- `scripts/r/part-iv/summarize_landings.R`
- `scripts/sql/part-iv/summarize_landings.sql`

Las tres alternativas comparten el contrato descrito en el capítulo. Una solución se considera suficiente cuando valida la entrada antes de resumir, excluye explícitamente registros `invalid`, no modifica la fuente, recibe la salida como parámetro y deja un estado interpretable. No se exige que las implementaciones tengan la misma estructura sintáctica.

La revisión debe valorar la relación `riesgo → decisión → comprobación → evidencia`, no la cantidad de funciones o archivos.
