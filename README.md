# Flujos digitales para la ciencia pesquera y la ecología cuantitativa

**Datos, código, reproducibilidad, automatización, colaboración e inteligencia artificial para la investigación científica.**

Repositorio del libro web y sus materiales de aprendizaje, clases reproducibles y futuros posts sobre herramientas y flujos digitales para la ciencia pesquera y la ecología cuantitativa.

[![Leer libro en línea](https://img.shields.io/badge/Leer_libro-en_l%C3%ADnea-1B5E75?style=for-the-badge&logo=quarto)](https://qselmer.github.io/fisheries-research-workflows-book/)

[![Ver repositorio](https://img.shields.io/badge/Ver_repositorio-GitHub-24292F?style=for-the-badge&logo=github)](https://github.com/qselmer/fisheries-research-workflows-book)

## Estado y propósito

El proyecto está en desarrollo incremental. Su propósito es enseñar a diseñar flujos de investigación digitales portables, auditables, seguros y sostenibles. No desarrolla teoría estadística avanzada.

## Estructura

```text
book/         fuentes del libro Quarto
classes/      clases reproducibles
posts/        borradores posteriores a la evaluación
data/         datos separados por procedencia y estado
scripts/      código reutilizable en R, Python y SQL
exercises/    prácticas
solutions/    solucionarios
references/   bibliografía y estilos de citación
docs/         sitio HTML generado para GitHub Pages
```

## Requisitos e instalación

Se requiere Git y [Quarto](https://quarto.org/docs/get-started/). Positron es el entorno principal recomendado, pero el proyecto no depende de un IDE concreto.

```bash
git clone https://github.com/qselmer/fisheries-research-workflows-book.git
cd fisheries-research-workflows-book
quarto check
```

No se declaran entornos de R o Python hasta que existan dependencias ejecutables verificadas.

## Previsualización y renderización

Desde la raíz del repositorio:

```bash
quarto preview book --to html
quarto render book --to html
quarto render classes/ccpe-000/ccpe-000-clase.qmd --to revealjs
quarto render classes/ccpe-023/ccpe-023-class.qmd --to revealjs
quarto render classes/ccpe-024/ccpe-024-class.qmd --to revealjs
```

El libro se genera en `docs/`. Los archivos HTML de esa carpeta no se editan manualmente.

## Política de datos

- `data/raw/` y `data/external/` no se publican.
- Los datos institucionales, credenciales, conexiones y rutas locales quedan fuera del repositorio.
- Los ejemplos públicos deben ser abiertos, sintéticos o anonimizados.
- Los datos originales nunca se modifican; las transformaciones producen archivos derivados.

## Publicación y contribución

La publicación usa GitHub Pages mediante GitHub Actions desde la rama `main`. Consulte [PUBLISHING.md](PUBLISHING.md) antes de publicar.

Las contribuciones deben mantener el español editorial, usar rutas relativas, preservar la separación entre libro, clase y post, y adjuntar los resultados de renderización y validación.

## Licencia y autor

Contenido: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es). El código deberá incorporar una licencia explícita antes de recibir contribuciones externas.

**Autor:** Elmer Quispe-Salazar.
