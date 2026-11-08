"""README figure: tap in the background, take the screen only to type, scroll or drag, stop at the hard lines."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude/skills/esquadro/scripts"))
from esquadro import Drawing, hand_note, panels

OUT = Path(__file__).resolve().parent


def phone(d, x, y, w, h):
    """Front of an iPhone: body, island, home bar. Returns its centre."""
    d.rect(x, y, w, h)
    d.rect(x + w * 0.36, y + h * 0.04, w * 0.28, h * 0.035, fill="#000")
    d.line((x + w * 0.35, y + h * 0.94), (x + w * 0.65, y + h * 0.94), "thin")
    return (x + w / 2, y + h / 2)


def laptop(d, x, y, w, h):
    """Front of a Mac laptop: screen and base."""
    d.rect(x, y, w, h)
    d.polyline([(x - 3, y + h + 3), (x + w + 3, y + h + 3), (x + w, y + h), (x, y + h)], closed=True)


def main():
    d = Drawing.figure("page", 94, lang="en", title="Espelho in three rules", description="Tap in the background, take the screen only to type, scroll or drag, and stop where the person decides.")
    d.text((5, 9), "Espelho in three rules", "heading")
    f1, f2, f3 = panels(
        d, 3, area=(5.0, 14.0, 160.0, 74.0),
        titles=["1. Tap in the background", "2. Full screen to type", "3. Stop and hand over"],
        verdicts=[True, None, False], colored=True, arrows=False, gap=10.0,
    )

    # 1: the person's own window stays in front; the phone window gets the taps.
    sx, sy = f1.x + 5, f1.y + 8
    laptop(d, sx, sy, 36, 24)
    d.rect(sx + 3, sy + 4, 18, 15)
    for i in range(3):
        d.line((sx + 5, sy + 8 + i * 3.5), (sx + 18, sy + 8 + i * 3.5), "thin")
    tap = phone(d, sx + 25, sy + 3, 8, 17)
    hand_note(d, tap, (f1.x + 2, f1.y + 46), "taps and the View menu work; the person keeps working", 42, bend=0.2, ink="blue")

    # 2: the phone fills the screen; typing, scrolling and dragging need it.
    sx = f2.x + 5
    laptop(d, sx, sy, 36, 24)
    big = phone(d, sx + 12, sy + 1, 11, 22)
    hand_note(d, big, (f2.x + 2, f2.y + 46), "type, scroll, drag: only after a yes, when the Mac is free", 42, bend=-0.2)

    # 3: a passcode screen is the person's step.
    px, py = f3.x + 15, f3.y + 5
    c = phone(d, px, py, 16, 32)
    for i in range(6):
        d.circle((px + 3 + i * 2, py + 9), 0.7)
    for r in range(3):
        for k in range(3):
            d.circle((px + 4 + k * 4, py + 15 + r * 4.5), 1.4)
    hand_note(d, (px + 16, py + 9), (f3.x + 2, f3.y + 46), "passcodes, privacy prompts, the Share sheet: the person decides", 42, bend=0.25, ink="red")
    return d.save(OUT / "espelho.svg")


if __name__ == "__main__":
    print(main())
