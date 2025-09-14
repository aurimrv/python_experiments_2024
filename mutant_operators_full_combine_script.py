import os
import csv
from collections import defaultdict
from pathlib import Path

files_list_path = "files.txt"

# Dicionário acumulador de operadores
operadores_acumulados = defaultdict(lambda: {"mortos": 0, "vivos": 0})

with open(files_list_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        base_key = line.split(":")[0]
        compiled_csv_path = Path(base_key) / "compiled_operator_report_cosmicray.csv"

        if compiled_csv_path.exists():
            with open(compiled_csv_path, "r", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Pula o cabeçalho
                for row in reader:
                    operador = row[0]
                    mortos = int(row[1])
                    vivos = int(row[2])
                    operadores_acumulados[operador]["mortos"] += mortos
                    operadores_acumulados[operador]["vivos"] += vivos
        else:
            print(f"Aviso: {compiled_csv_path} não encontrado. Pulando...")

# Caminho do arquivo final compilado
output_path = Path("compiled_full_operator_report_cosmicray.csv")

# Escrita do CSV consolidado
with open(output_path, "w", newline='', encoding="utf-8") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["Operador", "Mortos", "Vivos"])
    for operador, dados in sorted(operadores_acumulados.items()):
        writer.writerow([operador, dados["mortos"], dados["vivos"]])
