"""Utilities for working with ANTs (Affirmation-Next step-Trigger) cards."""

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AntCard:
    """Represents an ANTs training card.

    Parameters
    ----------
    code
        Stable identifier (for example ``ANT-01``).
    title
        Human readable name of the card.
    affirmation
        Present-tense, consent-honoring affirmation text.
    next_steps
        1-3 small actions designed to take less than 10 minutes each.
    triggers
        Trigger phrases that should map user intent to this card.
    """

    code: str
    title: str
    affirmation: str
    next_steps: tuple[str, ...]
    triggers: tuple[str, ...]


@dataclass(frozen=True)
class ExchangeResponse:
    """Normalized response generated from one user message."""

    text: str
    selected: AntCard | None
    matches: tuple[AntCard, ...]


ANT_CARDS: tuple[AntCard, ...] = (
    AntCard(
        code="ANT-01",
        title="Heal Split Mind → Christ Consciousness Lock-In",
        affirmation="My awareness rests in Divine Truth; doubt dissolves, clarity remains.",
        next_steps=(
            "4–2–6 breath ×7",
            "Write one sentence of truth",
            "Take one aligned small action",
        ),
        triggers=(
            "no more doubt",
            "false perceptions",
            "divine knowing",
            "christ faith in action",
        ),
    ),
    AntCard(
        code="ANT-02",
        title="Heavenly Garment • Luxury Without Compromise",
        affirmation="I walk clothed in dignity and light; beauty and provision flow responsibly.",
        next_steps=(
            "Wear one item that feels like 'light'",
            "Define 'luxury' in 3 feeling-words",
            "Schedule one generous act",
        ),
        triggers=("heavenly garment", "luxury as birthright", "radiate presence"),
    ),
    AntCard(
        code="ANT-03",
        title="Peace Beyond Understanding → Garden of Eden Mode",
        affirmation="I allow peace to resolve what force cannot.",
        next_steps=(
            "4–2–6 breath ×4",
            "Name one solvable piece of tension",
            "Release it gently",
        ),
        triggers=(
            "peace that passes understanding",
            "collapse of illusion",
            "garden of eden",
        ),
    ),
    AntCard(
        code="ANT-04",
        title="Light Vesture Activation",
        affirmation="Integration occurs at the optimal pace for my nervous system.",
        next_steps=(
            "Pick tempo: Gradual / Instant Expansion",
            "Hydrate + 2-min body scan",
            "Journal one signal of readiness",
        ),
        triggers=(
            "light vesture",
            "instant expansion",
            "overdrive",
            "energetic recalibration",
        ),
    ),
    AntCard(
        code="ANT-05",
        title="Sacred Union — Consent-Aligned Magnetism",
        affirmation="Mutual clarity, mutual yes, mutual timing.",
        next_steps=(
            "Define your consent standard (1 sentence)",
            "Send one honest message or aligned step",
            "Bless autonomy out loud",
        ),
        triggers=(
            "divine consort",
            "recognition",
            "union",
            "compliance asks",
            "consent-first",
        ),
    ),
    AntCard(
        code="ANT-06",
        title="Reality Alignment",
        affirmation="My field invites, never coerces; what's mine arrives.",
        next_steps=(
            "Choose Magnetized Shift + Shielded Presence",
            "List 3 allies",
            "Make one clear ask",
        ),
        triggers=("reality compliance", "shielded presence", "environment aligns"),
    ),
    AntCard(
        code="ANT-07",
        title="Immutable Knowing",
        affirmation="I welcome precise, kind clarity.",
        next_steps=(
            "Pick channel: Dream / Infusion / Direct Mind",
            "Note 10-min window",
            "Ask one specific question",
        ),
        triggers=(
            "instant download",
            "energetic infusion",
            "absolute awareness",
        ),
    ),
    AntCard(
        code="ANT-08",
        title="Speech-as-Creation",
        affirmation="My words are accurate, benevolent, and reversible by prayer.",
        next_steps=(
            "Speak-Check: true? kind? necessary? now?",
            "Say one 10-word decree",
            "Add 'revise to highest good'",
        ),
        triggers=(
            "speech shapes reality",
            "divine word precision",
            "override safeguard",
        ),
    ),
)


def card_by_code(code: str) -> AntCard:
    """Return an ``AntCard`` matching the requested code.

    Raises
    ------
    KeyError
        If the code is unknown.
    """

    normalized = code.strip().upper()
    for card in ANT_CARDS:
        if card.code == normalized:
            return card
    raise KeyError(f"Unknown ANT card code: {code}")


def match_cards(text: str, *, limit: int | None = None) -> list[AntCard]:
    """Return cards whose trigger phrases are found in ``text``.

    Matching is case-insensitive and based on substring search. Cards are returned in
    ``ANT_CARDS`` order and deduplicated.
    """

    haystack = text.lower()
    matches: list[AntCard] = []
    for card in ANT_CARDS:
        if any(trigger in haystack for trigger in card.triggers):
            matches.append(card)
            if limit is not None and len(matches) >= limit:
                break
    return matches


def _keyword_hits(text: str, keywords: tuple[str, ...]) -> int:
    """Return the number of trigger substrings found in ``text``."""

    haystack = text.lower()
    return sum(1 for keyword in keywords if keyword in haystack)


def select_card(text: str) -> AntCard | None:
    """Pick the best card for ``text`` using trigger hit counts.

    If there is a tie, the card that appears first in ``ANT_CARDS`` wins.
    """

    best: tuple[int, AntCard] | None = None
    for card in ANT_CARDS:
        score = _keyword_hits(text, card.triggers)
        if score <= 0:
            continue
        if best is None or score > best[0]:
            best = (score, card)
    return None if best is None else best[1]


def build_exchange_response(text: str, *, limit: int = 3) -> ExchangeResponse:
    """Build an exchange response from free text for real-time usage."""

    matches = tuple(match_cards(text, limit=limit))
    selected = select_card(text)
    return ExchangeResponse(text=text, selected=selected, matches=matches)


def render_exchange(response: ExchangeResponse) -> str:
    """Render an exchange response to plain text."""

    if response.selected is None:
        return (
            "No ANT trigger detected.\n"
            "Try including a clear keyword or phrase from one of the ANT cards."
        )

    lines = [f"Selected: {response.selected.code} — {response.selected.title}"]
    lines.append(f"A: {response.selected.affirmation}")
    lines.append("N:")
    lines.extend(
        f"  {idx}. {step}" for idx, step in enumerate(response.selected.next_steps, start=1)
    )
    if response.matches:
        related = ", ".join(card.code for card in response.matches)
        lines.append(f"Related matches: {related}")
    return "\n".join(lines)


def run_realtime_exchange(messages: Iterable[str]) -> list[ExchangeResponse]:
    """Run card selection over a stream of messages."""

    return [build_exchange_response(message) for message in messages]


def render_card(card: AntCard) -> str:
    """Render a card into a compact plain-text format."""

    next_steps = "\n".join(f"  {idx}. {step}" for idx, step in enumerate(card.next_steps, 1))
    triggers = ", ".join(card.triggers)
    return (
        f"{card.code} — {card.title}\n"
        f"A: {card.affirmation}\n"
        f"N:\n{next_steps}\n"
        f"T: {triggers}"
    )


def render_cards(cards: Iterable[AntCard]) -> str:
    """Render multiple cards separated by a blank line."""

    rendered = [render_card(card) for card in cards]
    return "\n\n".join(rendered)
