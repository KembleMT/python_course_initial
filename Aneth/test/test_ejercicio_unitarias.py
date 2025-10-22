import pytest
from src.ejercicio_unitarias import Cliente, IRepositorioDB, Repositorio

def test_validar_email_success():
    #Arrange
    cliente test = Cliente ("Jona","email@test.com)

    #Assert 
    assert cliente_test.validar_email()is True

def test_abstractmethod():
    with pytest.raises(TypeError):
        IRepositorioDB()

def test_repositorio_guardar(capfd):
    repo = RepositorioBD()
    repo.guardar("tacos")

    out,_= capfd.readouterr()
    assert"Pedido taco almacenado exitosamente" in out 

def test_service_pedido_con_adapter(capfd):
    #Arrange
    repo_mock = ApiTercerosAdapter()
    service = ServicePedido(repo_mock)

    # Act
    service.crear_pedido("enchiladas")

    # Assert
    out, _ = capfd.readouterr()
    assert "Guardado pero de forma distinta: enchiladas" in out
    assert "Notificación de almacenado" in out