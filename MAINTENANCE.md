# Profile maintenance

The profile keeps the original star-chart/protein artwork in `assets/hero-archive.png` and uses two self-hosted SVG layers for the motion treatment: `hero-archive-animated.svg` and `hero-archive-animated-mobile.svg`. The static PNG variants are selected when reduced motion is requested. The animated SVGs embed an optimized copy of the same artwork, so the README does not depend on an image-generation service.

The hero startup sequence is an 8 second loop: brass ticks wake first, a cyan scan crosses the protein field, molecular nodes respond, and an energy point returns along the orbit. Desktop and mobile use different geometry; mobile keeps only the scan, protein flash, and one orbit return. The typing strip uses a 10 second opacity rotation on both sizes. Keep the static PNG and the reduced-motion media sources intact.

The Day section uses the restored desktop and mobile research-loop SVGs. A light still completes the wet–dry path in 13 seconds; six `.motion` rings briefly respond at 0, 2.1, 4.2, 6.5, 8.7, and 10.8 seconds. The `.motion` class is hidden for `prefers-reduced-motion`.

The Night section links to `assets/tianji-card.svg` and `assets/tianji-card-mobile.svg`. The card uses a six second star-convergence and border-glow loop around the fixed lines “BaZi, but schema-validated.” and “A reproducible reading for an irreproducible universe.” Keep the card linked to the `Ficere/tianji` repository and avoid describing it as a biology result.

`.github/workflows/snake.yml` runs every 12 hours, on pushes to `main`, and through `workflow_dispatch`. It writes light and dark SVGs to the `output` branch with brass/cyan colors. The output branch is the live animation source; the checked-in `assets/snake-fallback*.svg` files are the last known good fallback if the branch is temporarily unavailable.

SynAster Hub is described on its public skill manifest as a protein-design skill bundle for AI agents. The README uses that capability description without claiming ownership, authorship, or a specific personal responsibility.
