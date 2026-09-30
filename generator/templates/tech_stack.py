"""SVG template for a qualitative capability radar.

The card deliberately avoids language percentages or invented skill scores.
It shows the four capability areas as an equal-weight map.
"""

import math

from generator.utils import esc


WIDTH = 850
HEIGHT = 250


def _point(cx, cy, radius, angle_degrees):
    angle = math.radians(angle_degrees - 90)
    return cx + radius * math.cos(angle), cy + radius * math.sin(angle)


def render(
    languages=None,
    galaxy_arms=None,
    theme=None,
    exclude=None,
    max_display=None,
) -> str:
    """Render a four-axis capability radar using the configured theme."""
    theme = theme or {}
    bg = theme.get("nebula", "#101722")
    border = theme.get("star_dust", "#24343c")
    text_bright = theme.get("text_bright", "#f1ead9")
    text_dim = theme.get("text_dim", "#9fb8b7")
    text_faint = theme.get("text_faint", "#6e8589")
    amber = theme.get("axon_amber", "#d7b56e")
    cyan = theme.get("synapse_cyan", "#71c9c2")
    violet = theme.get("dendrite_violet", "#a48bce")

    labels = [
        ("Protein & Enzyme Design", amber, 0),
        ("Frontier Models", cyan, 90),
        ("Atom-Level Tools", violet, 180),
        ("Wet–Dry R&D Systems", amber, 270),
    ]
    cx, cy, radius = 650, 128, 78
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
        '<title id="title">Qualitative capability radar</title>',
        '<desc id="desc">An equal-weight map of protein and enzyme design, frontier models, atom-level tools, and wet-dry research systems.</desc>',
        '<style>@media (prefers-reduced-motion: reduce) { .motion { display: none; } }</style>',
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{HEIGHT - 1}" rx="16" fill="{bg}" stroke="{border}" stroke-width="1"/>',
        f'<text x="30" y="42" fill="{text_faint}" font-size="11" font-family="monospace" letter-spacing="3">CAPABILITY RADAR</text>',
        f'<text x="30" y="78" fill="{text_bright}" font-size="22" font-family="Georgia,serif">A reusable research stack</text>',
        f'<text x="30" y="112" fill="{text_dim}" font-size="13" font-family="sans-serif">Four connected areas, shown as a map</text>',
        f'<text x="30" y="134" fill="{text_dim}" font-size="13" font-family="sans-serif">rather than a ranked scorecard.</text>',
        f'<path d="M30 165H370" stroke="{border}" stroke-width="1"/>',
        f'<text x="30" y="192" fill="{text_faint}" font-size="11" font-family="monospace">DESIGN · MODELS · ATOMS · LOOP</text>',
        f'<g fill="none" stroke="{text_faint}" stroke-width="1" opacity=".4"><circle cx="{cx}" cy="{cy}" r="26"/><circle cx="{cx}" cy="{cy}" r="52"/><circle cx="{cx}" cy="{cy}" r="{radius}"/></g>',
    ]

    axis_points = []
    for _, color, angle in labels:
        x, y = _point(cx, cy, radius, angle)
        axis_points.append((x, y))
        parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{border}" stroke-width="1"/>')
        parts.append(f'<circle class="motion" cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{color}"><animate attributeName="r" values="4;7;4" dur="6s" begin="{angle / 90:.1f}s" repeatCount="indefinite"/></circle>')

    polygon = " ".join(f"{x:.1f},{y:.1f}" for x, y in axis_points)
    parts.append(f'<polygon points="{polygon}" fill="{cyan}" fill-opacity=".10" stroke="{cyan}" stroke-width="1.5"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="{bg}" stroke="{amber}" stroke-width="1.5"/>')
    parts.append(f'<text x="{cx}" y="{cy + 4}" text-anchor="middle" fill="{text_bright}" font-family="monospace" font-size="9" letter-spacing="1">R&amp;D</text>')

    label_lines = [
        (["Protein & Enzyme", "Design"], cx + 86, cy - 5, "start", amber),
        (["Frontier Models"], cx + 13, cy - radius - 13, "middle", cyan),
        (["Atom-Level", "Tools"], cx - 86, cy - 5, "end", violet),
        (["Wet–Dry R&D", "Systems"], cx + 13, cy + radius + 18, "middle", amber),
    ]
    for lines, x, y, anchor, color in label_lines:
        for line_index, line in enumerate(lines):
            parts.append(
                f'<text x="{x}" y="{y + line_index * 12}" text-anchor="{anchor}" '
                f'fill="{color}" font-family="monospace" font-size="9">{esc(line)}</text>'
            )

    parts.append(f'<path class="motion" d="M560 220H760" stroke="{cyan}" stroke-width="1" stroke-dasharray="3 8"><animate attributeName="stroke-dashoffset" from="0" to="-90" dur="7s" repeatCount="indefinite"/></path>')
    parts.append("</svg>")
    return "\n".join(parts)
