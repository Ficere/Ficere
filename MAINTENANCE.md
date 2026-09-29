# Profile maintenance

The profile keeps the original star-chart/protein artwork in `assets/hero-archive.png` and uses two self-hosted SVG layers for the motion treatment: `hero-archive-animated.svg` and `hero-archive-animated-mobile.svg`. The static PNG variants are selected when reduced motion is requested. The animated SVGs embed an optimized copy of the same artwork, so the README does not depend on an image-generation service.

The Day section uses the restored desktop and mobile research-loop SVGs. Their only animation is a slow light moving through the loop, and the `.motion` class is hidden for `prefers-reduced-motion`.

`.github/workflows/snake.yml` runs every 12 hours, on pushes to `main`, and through `workflow_dispatch`. It writes light and dark SVGs to the `output` branch with brass/cyan colors. The output branch is the live animation source; the checked-in `assets/snake-fallback*.svg` files are the last known good fallback if the branch is temporarily unavailable.

SynAster Hub is described on its public skill manifest as a protein- and RNA-design skill bundle for AI agents. The README uses that capability description without claiming ownership or a personal role.
