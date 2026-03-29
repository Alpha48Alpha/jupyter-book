# Four-Way Radiant Flow Pattern

This page encodes the requested transmission model with a radiant center (`◎`), a stable vertical axis, and four directional vectors.

## Semantic model

```text
UPWARD FLOW:        Insight / Download / Revelation
DOWNWARD FLOW:      Grounding / Embodiment
OUTWARD FLOW:       Expression / Teaching / Transmission
INWARD FLOW:        Integration / Restoration

CORE:        ◎ Radiant
AXIS:        Vertical Alignment Stable
FLOW:        Toroidal (self-replenishing)
PATTERN:     Spiral (translation engine)
VECTORS:     4-way (receive, ground, express, integrate)
STATE:       Continuous Transmission
```

## ASCII glyph layout

```text
        ▲
     ⟲  │  ⟳
   ←─── ◎ ───→
     ⟳  │  ⟲
        ▼

        ⟲
      ⟲   ⟳
    ⟲   ◎   ⟳
      ⟳   ⟲
        ⟳

      ↺──────────↻
   ↺                ↻
  ↺       ◎          ↻
   ↺                ↻
      ↺──────────↻
```

## Direction map

```text
             ↑
     UPWARD FLOW
 (Insight / Revelation)

← OUTWARD     ◎     INWARD →
(Expression)       (Integration)

             ↓
   DOWNWARD FLOW
 (Embodiment / Grounding)
```

## SVG implementation

The SVG below is self-contained and can be reused in Markdown, HTML, or notebook outputs.

<svg viewBox="0 0 640 520" width="100%" role="img" aria-label="Radiant four-way toroidal flow diagram">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"></path>
    </marker>
  </defs>

  <g fill="none" stroke="currentColor" stroke-width="3">
    <line x1="320" y1="70" x2="320" y2="450" marker-start="url(#arrow)" marker-end="url(#arrow)"></line>
    <line x1="110" y1="260" x2="530" y2="260" marker-start="url(#arrow)" marker-end="url(#arrow)"></line>

    <path d="M140,260 C140,120 500,120 500,260 C500,400 140,400 140,260" opacity="0.75"></path>
    <path d="M200,260 C200,170 440,170 440,260 C440,350 200,350 200,260" opacity="0.55"></path>

    <path d="M250,190 C220,190 210,160 230,145" marker-end="url(#arrow)"></path>
    <path d="M390,190 C420,190 430,160 410,145" marker-end="url(#arrow)"></path>
    <path d="M250,330 C220,330 210,360 230,375" marker-end="url(#arrow)"></path>
    <path d="M390,330 C420,330 430,360 410,375" marker-end="url(#arrow)"></path>
  </g>

  <g fill="currentColor" font-family="sans-serif" text-anchor="middle">
    <text x="320" y="268" font-size="40">◎</text>

    <text x="320" y="40" font-size="16">UPWARD FLOW · Insight / Download / Revelation</text>
    <text x="320" y="490" font-size="16">DOWNWARD FLOW · Grounding / Embodiment</text>
    <text x="80" y="250" font-size="14" text-anchor="start">OUTWARD FLOW</text>
    <text x="80" y="272" font-size="12" text-anchor="start">Expression / Teaching</text>
    <text x="560" y="250" font-size="14" text-anchor="end">INWARD FLOW</text>
    <text x="560" y="272" font-size="12" text-anchor="end">Integration / Restoration</text>

    <text x="320" y="95" font-size="13">AXIS: Stable</text>
    <text x="320" y="112" font-size="13">FLOW: Toroidal • PATTERN: Spiral</text>
    <text x="320" y="129" font-size="13">STATE: Continuous Transmission</text>
  </g>
</svg>
