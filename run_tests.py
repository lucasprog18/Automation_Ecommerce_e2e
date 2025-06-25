import pytest
import os
import sys

# Garante que o diretório raiz do projeto está no path, evitando erros de importação
sys.path.insert(0, os.path.abspath("."))

# Executa todos os testes da suíte por padrão.
# Para rodar um teste isolado, passe o caminho como argumento, por exemplo:
# pytest.main(["tests/test_login_success.py"])
pytest.main()

