import pytest
from io import BytesIO
from pathlib import Path


@pytest.fixture
def input_directory() -> Path:
    """Directory containing our input images"""
    input_directory = Path(__file__).parent.joinpath("inputs")
    return input_directory


@pytest.fixture
def png(input_directory: Path) -> BytesIO:
    path = input_directory.joinpath("panto.png")
    return BytesIO(path.read_bytes())