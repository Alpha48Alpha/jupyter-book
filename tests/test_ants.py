import pytest

from jupyter_book.ants import ANT_CARDS, card_by_code, match_cards, render_card, render_cards


def test_card_by_code_case_insensitive():
    card = card_by_code("ant-03")
    assert card.title == "Peace Beyond Understanding → Garden of Eden Mode"


def test_card_by_code_unknown():
    with pytest.raises(KeyError, match="Unknown ANT card code"):
        card_by_code("ANT-99")


def test_match_cards_returns_ordered_matches():
    text = "I choose shielded presence and welcome instant download clarity."
    matches = match_cards(text)
    assert [card.code for card in matches] == ["ANT-06", "ANT-07"]


def test_match_cards_limit():
    text = "no more doubt and reality compliance and speech shapes reality"
    matches = match_cards(text, limit=2)
    assert [card.code for card in matches] == ["ANT-01", "ANT-06"]


def test_render_card_format():
    rendered = render_card(ANT_CARDS[0])
    assert rendered.startswith("ANT-01 — Heal Split Mind")
    assert "A: My awareness rests in Divine Truth" in rendered
    assert "  1. 4–2–6 breath ×7" in rendered


def test_render_cards_separates_with_blank_lines():
    rendered = render_cards(ANT_CARDS[:2])
    assert "\n\nANT-02" in rendered
