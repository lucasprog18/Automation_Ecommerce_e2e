import os
import sys
import pytest
import datetime

# Garante que o diretório raiz do projeto está no path, evitando erros de importação
sys.path.insert(0, os.path.abspath("."))

# Garante que a pasta 'reports/' existe
os.makedirs("reports", exist_ok=True)

# Gera um nome de arquivo único com timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_path = os.path.join("reports", f"report_{timestamp}.html")

# Executa o teste de checkout com relatório HTML gerado
pytest.main([
    "tests/test_login_failure.py",
    f"--html={report_path}",
    "--self-contained-html",
    "--capture=tee-sys",
    "-v"
])
