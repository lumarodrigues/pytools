import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario', ['rdsluma@gmail.com', 'foo@bar.com.br'])
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'msndaluma@hotmail.com',
        'Curso Python Pro',
        'TDD e Baby steps'
    )
    assert destinatario in resultado


@pytest.mark.parametrize('destinatario', ['', 'luma'])
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            destinatario,
            'msndaluma@hotmail.com',
            'Curso Python Pro',
            'TDD e Baby steps'
        )
