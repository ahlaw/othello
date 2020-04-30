import pytest

from othello.game.player import Player
from othello.game.stone import BLACK_STONE, BLANK_STONE, WHITE_STONE
from othello.game.stone import StoneFactory


@pytest.fixture
def stone_factory() -> StoneFactory:
    """Returns a StoneFactory instance."""
    return StoneFactory()


def test_blank_stone(stone_factory: StoneFactory) -> None:
    assert stone_factory() == BLANK_STONE


def test_black_stone(stone_factory: StoneFactory) -> None:
    assert stone_factory(Player.BLACK) == BLACK_STONE


def test_white_stone(stone_factory: StoneFactory) -> None:
    assert stone_factory(Player.WHITE) == WHITE_STONE
