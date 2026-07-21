# Instrucciones persistentes del repositorio

- Todo el contenido editorial se escribe en español.
- Los nombres técnicos de carpetas y archivos permanecen en inglés abreviado cuando sea razonable.
- Los títulos visibles de los capítulos no muestran códigos administrativos `CCPE`; las clases sí los muestran.
- Este proyecto enseña herramientas e infraestructura digital: no desarrolla teoría estadística avanzada.
- No se modifican archivos de `data/raw/` ni se publican datos institucionales.
- No se agregan credenciales, secretos, nombres de servidores ni rutas locales absolutas.
- Se prefieren formatos abiertos, portables y rutas relativas.
- HTML es la salida editorial principal.
- Positron es el entorno principal y Quarto el sistema editorial del proyecto.
- El libro debe admitir ejemplos reproducibles en R, Python, SQL y terminal sin inventar dependencias.
- Toda modificación se valida mediante renderización; no se afirma que funciona sin ejecutar la validación.
- Los HTML generados en `docs/` no se editan manualmente. Los cambios editoriales se hacen en `.qmd`, `.scss` o `.yml` y luego se renderizan.
- Se preserva la separación entre aprendizaje personal, libro, clase y post. Un post definitivo solo se redacta después de evaluar el aprendizaje.
- Las decisiones importantes se documentan en el repositorio.
- Cada entrega incluye un resumen del diff y de las validaciones ejecutadas.
