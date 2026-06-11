import pytest
from app import areaTriangulo


def test_area_correcta():
    assert areaTriangulo(4, 5) == 10


def test_area_limite():
    assert areaTriangulo(0.1, 0.1) == pytest.approx(0.005)


def test_area_error():
    with pytest.raises(ValueError):
        areaTriangulo(-4, 5)