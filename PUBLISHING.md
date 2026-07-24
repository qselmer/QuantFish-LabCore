# Publicación del libro

El libro se publica mediante GitHub Actions. Los archivos HTML generados no se editan manualmente: toda corrección se realiza en los archivos fuente y se vuelve a renderizar.

## Previsualizar y generar

Desde la raíz del repositorio:

```bash
quarto preview book --to html
quarto render book --to html
```

Antes de confirmar cambios, compruebe que existen `docs/index.html` y `docs/.nojekyll`, que la navegación y la búsqueda funcionan y que no aparecen rutas locales ni información restringida.

## Validar las clases disponibles

```bash
quarto render classes/ccpe-000/ccpe-000-clase.qmd --to revealjs
quarto render classes/ccpe-023/ccpe-023-class.qmd --to revealjs
quarto render classes/ccpe-024/ccpe-024-class.qmd --to revealjs
```

## Registrar y enviar cambios

```bash
git status -sb
git diff
git add book README.md PUBLISHING.md references .github
git diff --staged
git commit -m "Update Quarto book"
git push origin main
```

Incluya únicamente los archivos que pertenecen al cambio. No utilice `git add -A` cuando el directorio de trabajo contenga modificaciones no relacionadas.

## Configuración de GitHub Pages

En el repositorio remoto:

```text
GitHub
→ Settings
→ Pages
→ Build and deployment
→ Source
→ GitHub Actions
```

El workflow `.github/workflows/quarto-pages.yml` renderiza el libro, carga `docs/` como artefacto y despliega el sitio.

URL oficial:

<https://qselmer.github.io/fisheries-research-workflows-book/>

## Lista de verificación

- El workflow de validación termina correctamente.
- El workflow de Pages termina correctamente.
- `docs/index.html` se genera durante el workflow.
- `docs/.nojekyll` está incluido en el sitio renderizado.
- CSS, JavaScript y tipografías locales cargan sin errores.
- La navegación entre capítulos y la búsqueda responden.
- Los enlaces al libro y al repositorio usan `fisheries-research-workflows-book`.
- No hay rutas absolutas, secretos ni datos institucionales.
- El libro y las clases RevealJS se renderizaron correctamente.

La publicación depende de que GitHub Pages esté configurado con **GitHub Actions** como fuente de despliegue.
