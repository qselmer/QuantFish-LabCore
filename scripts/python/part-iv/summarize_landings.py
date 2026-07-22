"""Valida y resume el caso sintético con la biblioteca estándar de Python."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import date
from pathlib import Path

REQUIRED = {"date", "port", "fleet", "species", "landings_t", "source_id", "quality_flag"}
VALID_FLAGS = {"ok", "review", "invalid"}


def read_landings(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if set(reader.fieldnames or []) != REQUIRED:
            raise ValueError(f"Esquema inesperado: {reader.fieldnames}")
        return list(reader)


def validate(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for number, row in enumerate(rows, start=2):
        try:
            date.fromisoformat(row["date"])
            value = float(row["landings_t"])
        except ValueError as exc:
            errors.append(f"fila {number}: tipo inválido ({exc})")
            continue
        if row["source_id"] in seen:
            errors.append(f"fila {number}: source_id duplicado")
        seen.add(row["source_id"])
        if row["quality_flag"] not in VALID_FLAGS:
            errors.append(f"fila {number}: quality_flag desconocido")
        if value < 0 and row["quality_flag"] != "invalid":
            errors.append(f"fila {number}: valor negativo sin marca invalid")
    return errors


def summarize(rows: list[dict[str, str]]) -> dict[str, float]:
    totals: defaultdict[str, float] = defaultdict(float)
    for row in rows:
        if row["quality_flag"] != "invalid":
            totals[row["species"]] += float(row["landings_t"])
    return dict(sorted(totals.items()))


def write_summary(summary: dict[str, float], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.writer(target)
        writer.writerow(["species", "landings_t"])
        writer.writerows((species, f"{value:.1f}") for species, value in summary.items())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        rows = read_landings(args.input)
    except (OSError, ValueError) as exc:
        raise SystemExit(f"Validación fallida: {exc}") from exc
    errors = validate(rows)
    if errors:
        raise SystemExit("Validación fallida:\n- " + "\n- ".join(errors))
    summary = summarize(rows)
    write_summary(summary, args.output)
    excluded = sum(row["quality_flag"] == "invalid" for row in rows)
    print(
        f"Validación superada: {len(rows)} registros leídos, "
        f"{excluded} excluidos y {len(summary)} especies resumidas."
    )
    print(f"Salida escrita: {args.output}")


if __name__ == "__main__":
    main()
