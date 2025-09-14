import os
import re
import csv
from collections import defaultdict
from pathlib import Path

# Caminho do arquivo que lista os diretórios base
files_list_path = "files-full.txt"

# Regex para extrair operador e resultado
pattern = re.compile(
    r"<td>.*?</td>\s*"
    r"<td>.*?</td>\s*"
    r"<td>([^<]+)</td>\s*"
    r"<td>.*?</td>\s*"
    r"<td>.*?</td>\s*"
    r"<td>.*?label.*?>([^<]+)</span>"
)

# Lê cada linha do arquivo files.txt
with open(files_list_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # pula linhas vazias ou comentadas

        base_key = line.split(":")[0]  # ex: 'bfs'
        base_dir = os.path.join(base_key, "ALL-SMART-GPT-MUTPY", "mutpy")
        output_dir = Path(base_key) / "mutant_operators_report"
        output_dir.mkdir(parents=True, exist_ok=True)

        # Percorre os diretórios recursivamente procurando por index.html
        for root, dirs, files in os.walk(base_dir):
            if "index.html" in files:
                index_path = os.path.join(root, "index.html")
                nome_subpasta = os.path.basename(root)

                with open(index_path, "r", encoding="utf-8") as html_file:
                    html = html_file.read()

                operadores = defaultdict(lambda: {"mortos": 0, "vivos": 0})

                for match in pattern.finditer(html):
                    operador_bruto = match.group(1).strip()
                    resultado = match.group(2).strip().lower()
                    operador = operador_bruto.split()[0]

                    if resultado == "survived":
                        operadores[operador]["vivos"] += 1
                    else:
                        operadores[operador]["mortos"] += 1

                output_path = output_dir / f"{nome_subpasta}.csv"
                with open(output_path, "w", newline='', encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Operador", "Mortos", "Vivos"])
                    for op, dados in sorted(operadores.items()):
                        writer.writerow([op, dados["mortos"], dados["vivos"]])
