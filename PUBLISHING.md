# Publicación del libro

La primera etapa publica el contenido versionado de `docs/` mediante GitHub Pages. No se edita el HTML generado: toda corrección se realiza en los archivos fuente y se vuelve a renderizar.

## Previsualizar y generar

Desde la raíz del repositorio:

```bash
quarto preview book --to html
quarto render book --to html
```

Antes de confirmar cambios, compruebe que existen `docs/index.html` y `docs/.nojekyll`, que la navegación y la búsqueda funcionan y que no aparecen rutas locales ni información restringida.

## Registrar y enviar cambios

```bash
git add book docs
git commit -m "Update Quarto book"
git push
```

Incluya también otros archivos fuente modificados, como `README.md`, `PUBLISHING.md` o una clase, cuando corresponda. Revise siempre `git diff --staged` antes del commit.

## Configuración inicial de GitHub Pages

En el repositorio remoto:

```text
GitHub
→ Settings
→ Pages
→ Deploy from a branch
→ main
→ /docs
```

Tras guardar, compruebe la URL oficial:

<https://qselmer.github.io/quant-fisheries-learning/>

## Lista de verificación

- `docs/index.html` abre bajo `/quant-fisheries-learning/`.
- `docs/.nojekyll` está versionado.
- CSS, JavaScript y tipografías locales cargan sin errores.
- La navegación entre capítulos y la búsqueda responden.
- Los enlaces al libro y al repositorio son correctos.
- No hay rutas absolutas, secretos ni datos institucionales.
- El libro y la clase RevealJS se renderizaron localmente.

El workflow del repositorio valida la renderización, pero no reemplaza el despliegue inicial desde `main/docs`.
