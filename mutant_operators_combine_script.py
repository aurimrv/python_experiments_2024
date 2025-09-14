import os
import csv
from collections import defaultdict
from pathlib import Path

files_list_path = "files-full.txt"

with open(files_list_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        base_key = line.split(":")[0]
        output_dir = Path(base_key) / "mutant_operators_report" / "cosmic-ray"
        output_dir.mkdir(parents=True, exist_ok=True)

        # Inicializa o dicionário para acumular os dados dos operadores
        operadores_acumulados = defaultdict(lambda: {"mortos": 0, "vivos": 0})

        # Percorre os arquivos CSV na pasta "mutant_operators_report/cosmic-ray"
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                if file.endswith(".csv"):
                    csv_path = os.path.join(root, file)
                    with open(csv_path, "r", encoding="utf-8") as csvfile:
                        reader = csv.reader(csvfile)
                        next(reader)  # Pula o cabeçalho
                        for row in reader:
                            operador = row[0]
                            mortos = int(row[1])
                            vivos = int(row[2])

                            # Acumula os dados dos operadores
                            operadores_acumulados[operador]["mortos"] += mortos
                            operadores_acumulados[operador]["vivos"] += vivos

        # Caminho do arquivo CSV compilado
        compiled_csv_path = Path(base_key) / "compiled_operator_report_cosmicray.csv"

        # Escreve os dados acumulados no arquivo CSV compilado
        with open(compiled_csv_path, "w", newline='', encoding="utf-8") as compiled_csvfile:
            writer = csv.writer(compiled_csvfile)
            writer.writerow(["Operador", "Mortos", "Vivos"])
            for op, dados in sorted(operadores_acumulados.items()):
                writer.writerow([op, dados["mortos"], dados["vivos"]])
