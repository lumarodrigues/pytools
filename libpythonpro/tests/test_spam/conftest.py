import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')  # 'module', 'session'
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj  # yield significa 'produz'
    # Tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()