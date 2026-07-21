# Instalación local en Positron

## Ubicación recomendada

Use una carpeta de proyectos accesible para su cuenta. Todas las instrucciones del repositorio emplean rutas relativas.

## Pasos

1. Crear o abrir la carpeta `QuantFish-LabCore`.
2. Descomprimir dentro de ella la carpeta `quant-fisheries-learning`.
3. Abrir Positron.
4. Ir a `File > Open Folder`.
5. Seleccionar `QuantFish-LabCore/quant-fisheries-learning`.
6. Abrir la terminal integrada.
7. Verificar:

```bash
quarto --version
git --version
```

## Renderizar libro

```bash
cd book
quarto render
```

## Renderizar clase

Desde la raíz del repositorio:

```bash
quarto render classes/ccpe-000/ccpe-000-clase.qmd --to revealjs
```

```bash
quarto render classes/ccpe-000/ccpe-000-clase.qmd --to pptx
```

```bash
quarto render classes/ccpe-000/ccpe-000-clase.qmd --to beamer
```
