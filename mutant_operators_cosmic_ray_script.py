import os
import re
import csv
from collections import defaultdict
from pathlib import Path

files_list_path = "files-full.txt"

# Regex para identificar blocos com operador e resultado
pattern = re.compile(
    r"\[job-id\].*?\n"                                # pula a linha do job-id
    r".*?core/([A-Za-z0-9_]+)\s+\d+\n"                # extrai o operador
    r"worker outcome: .*?, test outcome: (\w+)",      # extrai o resultado (killed/survived)
    re.MULTILINE
)

with open(files_list_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        base_key = line.split(":")[0]
        base_dir = os.path.join(base_key, "ALL-SMART-GPT-MUTPY")
        output_dir = Path(base_key) / "mutant_operators_report"
        output_dir.mkdir(parents=True, exist_ok=True)

        # Percorre os diretórios buscando por report_cosmicray.txt
        for root, dirs, files in os.walk(base_dir):
            if "report_cosmicray.txt" in files:
                report_path = os.path.join(root, "report_cosmicray.txt")
                nome_subpasta = os.path.basename(root)

                with open(report_path, "r", encoding="utf-8") as report_file:
                    content = report_file.read()

                operadores = defaultdict(lambda: {"mortos": 0, "vivos": 0})

                for operador, resultado in pattern.findall(content):
                    if resultado.lower() == "survived":
                        operadores[operador]["vivos"] += 1
                    else:
                        operadores[operador]["mortos"] += 1

                output_path = output_dir / f"{nome_subpasta}.csv"
                with open(output_path, "w", newline='', encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Operador", "Mortos", "Vivos"])
                    for op, dados in sorted(operadores.items()):
                        writer.writerow([op, dados["mortos"], dados["vivos"]])
