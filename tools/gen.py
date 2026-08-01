# -*- coding: utf-8 -*-
"""
GitHub Profile README hero banner generator.
Pure SVG + SMIL (no JavaScript). Emits dark.svg and light.svg with identical
layout/animation, differing only in palette.
"""
import io, json, os, math, random

W, H = 1180, 610
PAD = 22
# left (ASCII) panel geometry, shared by the clipPath pass and the draw pass
LX_, LY_, LW_ = 46, 46, 400

NAME = "Alper Enes Ersu"
HANDLE = "alperenesersu"
PHRASES = [
    "Full Stack Developer",
    "DevOps &amp; Automation",
    "Security / SIEM Enthusiast",
    "Full-time Student, Full-time Learner",
    "Open Source Contributor",
]
INFO = [
    ("location", "Location",  "Ankara, Turkiye"),
    ("cap",      "Education", "Computer Engineering @ THK University"),
    ("focus",    "Focus",     "DevOps  .  Log Analysis  .  Full Stack"),
    ("link",     "Portfolio", "alperenesersu.net"),
    ("linkedin", "LinkedIn",  "in/alper-enes-ersü-4a0176321"),
]
SKILLS = ["TypeScript", "React", "Next.js", "Node.js", "Python", "Ruby",
          "Java", "Flutter", "Docker", "Git", "Tailwind", "PostgreSQL"]

DOTS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "dots.json"), encoding="utf-8"))

MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, 'Liberation Mono', monospace"

PALETTES = {
    "dark": dict(
        bg="#030712", panel="#0F172A", panel2="#0B1220",
        border="rgba(255,255,255,.08)", border_strong="rgba(255,255,255,.14)",
        text="#F8FAFC", muted="#94A3B8",
        a1="#7C3AED", a2="#22D3EE", a3="#10B981",
        glow_o=".55", blob_o=".30", glass_o=".07", noise_o=".045",
        scan_o=".16", pill_bg="rgba(255,255,255,.04)", shadow_o=".55",
        ascii_o="1", dot_o=".85",
    ),
    "light": dict(
        bg="#FFFFFF", panel="#F8FAFC", panel2="#F1F5F9",
        border="rgba(15,23,42,.08)", border_strong="rgba(15,23,42,.14)",
        text="#0F172A", muted="#475569",
        a1="#2563EB", a2="#06B6D4", a3="#10B981",
        glow_o=".28", blob_o=".16", glass_o=".55", noise_o=".030",
        scan_o=".08", pill_bg="rgba(15,23,42,.035)", shadow_o=".14",
        ascii_o=".95", dot_o=".70",
    ),
}


def cw(fs):
    """approximate monospace advance width"""
    return fs * 0.6


def build(theme):
    p = PALETTES[theme]
    o = io.StringIO()
    w = o.write
    rnd = random.Random(7)

    w(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
      f'viewBox="0 0 {W} {H}" width="{W}" height="{H}" fill="none" role="img" '
      f'aria-label="{NAME} - GitHub profile banner">\n')

    # ---------------------------------------------------------------- defs
    w('<defs>\n')

    # accent gradient (animated)
    w(f'''<linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="{p['a1']}">
    <animate attributeName="stop-color" values="{p['a1']};{p['a2']};{p['a3']};{p['a1']}" dur="12s" repeatCount="indefinite"/>
  </stop>
  <stop offset=".5" stop-color="{p['a2']}">
    <animate attributeName="stop-color" values="{p['a2']};{p['a3']};{p['a1']};{p['a2']}" dur="12s" repeatCount="indefinite"/>
  </stop>
  <stop offset="1" stop-color="{p['a3']}">
    <animate attributeName="stop-color" values="{p['a3']};{p['a1']};{p['a2']};{p['a3']}" dur="12s" repeatCount="indefinite"/>
  </stop>
</linearGradient>\n''')

    # ascii gradient: vertical, colors cycle + gradient slides
    w(f'''<linearGradient id="asciiGrad" gradientUnits="userSpaceOnUse" x1="60" y1="120" x2="380" y2="470">
  <animate attributeName="y1" values="120;40;120" dur="9s" repeatCount="indefinite"/>
  <animate attributeName="y2" values="470;560;470" dur="9s" repeatCount="indefinite"/>
  <stop offset="0" stop-color="{p['a2']}">
    <animate attributeName="stop-color" values="{p['a2']};{p['a1']};{p['a3']};{p['a2']}" dur="10s" repeatCount="indefinite"/>
  </stop>
  <stop offset=".55" stop-color="{p['a1']}">
    <animate attributeName="stop-color" values="{p['a1']};{p['a3']};{p['a2']};{p['a1']}" dur="10s" repeatCount="indefinite"/>
  </stop>
  <stop offset="1" stop-color="{p['a3']}">
    <animate attributeName="stop-color" values="{p['a3']};{p['a2']};{p['a1']};{p['a3']}" dur="10s" repeatCount="indefinite"/>
  </stop>
</linearGradient>\n''')

    # border shimmer gradient
    w(f'''<linearGradient id="shimmer" gradientUnits="userSpaceOnUse" x1="-600" y1="0" x2="0" y2="{H}">
  <animate attributeName="x1" values="-600;{W};-600" dur="7s" repeatCount="indefinite"/>
  <animate attributeName="x2" values="0;{W+600};0" dur="7s" repeatCount="indefinite"/>
  <stop offset="0" stop-color="{p['a2']}" stop-opacity="0"/>
  <stop offset=".45" stop-color="{p['a2']}" stop-opacity=".9"/>
  <stop offset=".55" stop-color="{p['a1']}" stop-opacity=".9"/>
  <stop offset="1" stop-color="{p['a1']}" stop-opacity="0"/>
</linearGradient>\n''')

    # panel glass fill
    w(f'''<linearGradient id="glass" x1="0" y1="0" x2=".4" y2="1">
  <stop offset="0" stop-color="#FFFFFF" stop-opacity="{p['glass_o']}"/>
  <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
</linearGradient>\n''')
    w(f'''<linearGradient id="panelFill" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{p['panel']}"/>
  <stop offset="1" stop-color="{p['panel2']}"/>
</linearGradient>\n''')

    # background blobs
    for i, c in enumerate([p['a1'], p['a2'], p['a3']]):
        w(f'''<radialGradient id="blob{i}">
  <stop offset="0" stop-color="{c}" stop-opacity="{p['blob_o']}"/>
  <stop offset="1" stop-color="{c}" stop-opacity="0"/>
</radialGradient>\n''')

    # scanline gradient
    w(f'''<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{p['a2']}" stop-opacity="0"/>
  <stop offset=".5" stop-color="{p['a2']}" stop-opacity="{p['scan_o']}"/>
  <stop offset="1" stop-color="{p['a2']}" stop-opacity="0"/>
</linearGradient>\n''')

    # glass sheen sweep
    w(f'''<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
  <stop offset=".5" stop-color="#FFFFFF" stop-opacity="{p['glass_o']}"/>
  <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
</linearGradient>\n''')

    # filters
    w(f'''<filter id="noise" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/>
  <feColorMatrix type="saturate" values="0"/>
</filter>\n''')
    w(f'''<filter id="glowSoft" x="-60%" y="-60%" width="220%" height="220%">
  <feGaussianBlur stdDeviation="6" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>\n''')
    w(f'''<filter id="glowTight" x="-80%" y="-80%" width="260%" height="260%">
  <feGaussianBlur stdDeviation="2.2" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>\n''')
    w(f'''<filter id="blobBlur" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="40"/>
</filter>\n''')
    w(f'''<filter id="dropShadow" x="-30%" y="-30%" width="160%" height="160%">
  <feDropShadow dx="0" dy="18" stdDeviation="24" flood-color="#000000" flood-opacity="{p['shadow_o']}"/>
</filter>\n''')

    # clip for whole card
    w(f'<clipPath id="cardClip"><rect x="{PAD}" y="{PAD}" width="{W-2*PAD}" height="{H-2*PAD}" rx="26"/></clipPath>\n')


    # terminal typing clips
    fs_t = 22.0
    tx, ty = 552.0, 248.0
    cycle = len(PHRASES) * 3.0
    for i, ph in enumerate(PHRASES):
        pw = cw(fs_t) * len(ph.replace("&amp;", "&")) + 3
        t0 = i * 3.0 + 0.2
        k = [0.0, t0, t0 + 1.15, t0 + 2.35, t0 + 2.65, cycle]
        kt = ";".join(f"{max(0.0, min(1.0, v / cycle)):.4f}" for v in k)
        w(f'<clipPath id="tc{i}"><rect x="{tx-2:.1f}" y="{ty-fs_t-4:.1f}" height="{fs_t+12:.1f}" width="0">'
          f'<animate attributeName="width" values="0;0;{pw:.1f};{pw:.1f};0;0" keyTimes="{kt}" '
          f'dur="{cycle:.1f}s" repeatCount="indefinite" calcMode="linear"/>'
          f'</rect></clipPath>\n')

    w('</defs>\n')

    # ------------------------------------------------------------ background
    w(f'<rect width="{W}" height="{H}" rx="28" fill="{p["bg"]}"/>\n')

    w('<g clip-path="url(#cardClip)">\n')
    # floating blobs
    blobs = [(230, 180, 300, 0, "0;28;-18;0", "0;-22;20;0", 17),
             (930, 140, 320, 1, "0;-30;22;0", "0;24;-16;0", 21),
             (620, 560, 360, 2, "0;20;-26;0", "0;-14;18;0", 19)]
    for cx, cy, r, gi, vx, vy, dur in blobs:
        w(f'<g filter="url(#blobBlur)"><ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*0.72:.0f}" fill="url(#blob{gi})">'
          f'<animate attributeName="cx" values="{";".join(str(cx+float(v)) for v in vx.split(";"))}" dur="{dur}s" repeatCount="indefinite"/>'
          f'<animate attributeName="cy" values="{";".join(str(cy+float(v)) for v in vy.split(";"))}" dur="{dur+4}s" repeatCount="indefinite"/>'
          f'</ellipse></g>\n')

    # noise overlay
    w(f'<rect width="{W}" height="{H}" filter="url(#noise)" opacity="{p["noise_o"]}"/>\n')

    # tiny particles
    w('<g>\n')
    for i in range(26):
        px = rnd.uniform(40, W - 40)
        py = rnd.uniform(40, H - 40)
        r = rnd.uniform(0.9, 2.1)
        d = rnd.uniform(9, 20)
        dy = rnd.uniform(-26, -10)
        col = [p['a1'], p['a2'], p['a3']][i % 3]
        w(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{r:.1f}" fill="{col}" opacity="0">'
          f'<animate attributeName="opacity" values="0;.75;0" dur="{d:.1f}s" begin="{rnd.uniform(0,8):.1f}s" repeatCount="indefinite"/>'
          f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {dy:.0f};0 0" dur="{d:.1f}s" repeatCount="indefinite"/>'
          f'</circle>\n')
    w('</g>\n')
    w('</g>\n')

    # outer border + shimmer
    w(f'<rect x="{PAD}" y="{PAD}" width="{W-2*PAD}" height="{H-2*PAD}" rx="26" fill="none" stroke="{p["border"]}" stroke-width="1.5"/>\n')
    w(f'<rect x="{PAD}" y="{PAD}" width="{W-2*PAD}" height="{H-2*PAD}" rx="26" fill="none" stroke="url(#shimmer)" stroke-width="1.6" opacity=".9"/>\n')

    # ------------------------------------------------------------ LEFT PANEL
    LX, LY, LW, LH = LX_, LY_, LW_, H - 92
    w(f'<g filter="url(#dropShadow)"><rect x="{LX}" y="{LY}" width="{LW}" height="{LH}" rx="22" fill="url(#panelFill)" opacity=".92"/></g>\n')
    w(f'<rect x="{LX}" y="{LY}" width="{LW}" height="{LH}" rx="22" fill="url(#glass)"/>\n')
    w(f'<rect x="{LX}" y="{LY}" width="{LW}" height="{LH}" rx="22" fill="none" stroke="{p["border_strong"]}" stroke-width="1"/>\n')

    # panel label
    w(f'<text x="{LX+22}" y="{LY+34}" font-family="{MONO}" font-size="12.5" fill="{p["muted"]}" letter-spacing="1.6" opacity="0">'
      f'IDENTITY.MAP<animate attributeName="opacity" from="0" to=".85" dur=".6s" begin=".1s" fill="freeze"/></text>\n')
    w(f'<circle cx="{LX+LW-30}" cy="{LY+29}" r="4" fill="{p["a3"]}" filter="url(#glowTight)">'
      f'<animate attributeName="opacity" values=".35;1;.35" dur="2.4s" repeatCount="indefinite"/></circle>\n')

    # dot-matrix portrait (floating group), revealed row by row
    cols, rows, grid = DOTS["cols"], DOTS["rows"], DOTS["grid"]
    step = 352.0 / cols
    dx0 = LX + (LW - (cols - 1) * step) / 2.0
    dy0 = 126.0
    rmax = step * 0.47

    w('<g>\n')
    w(f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -5;0 0" dur="7s" repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .6 1;.4 0 .6 1" keyTimes="0;.5;1"/>\n')
    # glowSoft would smear dots this small -- the tight glow keeps them crisp
    w(f'<g fill="url(#asciiGrad)" opacity="{p["ascii_o"]}" filter="url(#glowTight)">\n')
    for j, row in enumerate(grid):
        if not any(row):
            continue
        beg = 0.3 + j * 0.035
        w(f'<g transform="translate(0 {dy0 + j*step:.1f})" opacity="0">'
          f'<animate attributeName="opacity" from="0" to="1" dur=".5s" begin="{beg:.2f}s" fill="freeze"/>')
        for c, t in enumerate(row):
            if not t:
                continue
            w(f'<circle cx="{dx0 + c*step:.1f}" cy="0" r="{t*rmax:.2f}"/>')
        w('</g>\n')
    w('</g>\n')
    # scanline over the portrait
    w(f'<rect x="{LX+10}" y="{LY+40}" width="{LW-20}" height="34" fill="url(#scan)">'
      f'<animateTransform attributeName="transform" type="translate" values="0 -60;0 {LH-60};0 -60" dur="6s" repeatCount="indefinite" keyTimes="0;.55;1" calcMode="linear"/></rect>\n')
    w('</g>\n')

    # whoami caption + cursor
    cy_ = LY + LH - 40
    w(f'<text x="{LX+24}" y="{cy_}" font-family="{MONO}" font-size="14.5" fill="{p["muted"]}" opacity="0">'
      f'<tspan fill="url(#accent)">&gt;</tspan> whoami :: {HANDLE}'
      f'<animate attributeName="opacity" from="0" to="1" dur=".5s" begin="2.5s" fill="freeze"/></text>\n')
    cur_x = LX + 24 + cw(14.5) * (len(f"> whoami :: {HANDLE}") + 1)
    w(f'<rect x="{cur_x:.0f}" y="{cy_-11:.0f}" width="8" height="14" fill="url(#accent)" opacity="0" filter="url(#glowTight)">'
      f'<animate attributeName="opacity" values="0;0;1;0;1" keyTimes="0;.32;.33;.66;1" dur="2.6s" begin="2.5s" repeatCount="indefinite"/></rect>\n')

    # ------------------------------------------------------- RIGHT: TERMINAL
    RX, RY, RW, RH = 470, 46, W - 470 - 46, H - 92
    w(f'<g filter="url(#dropShadow)"><rect x="{RX}" y="{RY}" width="{RW}" height="{RH}" rx="22" fill="url(#panelFill)" opacity=".94"/></g>\n')
    w(f'<rect x="{RX}" y="{RY}" width="{RW}" height="{RH}" rx="22" fill="url(#glass)"/>\n')
    w(f'<rect x="{RX}" y="{RY}" width="{RW}" height="{RH}" rx="22" fill="none" stroke="{p["border_strong"]}" stroke-width="1"/>\n')
    # sheen sweep across terminal
    w(f'<g clip-path="url(#cardClip)"><rect x="{RX}" y="{RY}" width="140" height="{RH}" fill="url(#sheen)" opacity=".8">'
      f'<animateTransform attributeName="transform" type="translate" values="-260 0;{RW+260} 0;{RW+260} 0" dur="9s" keyTimes="0;.45;1" repeatCount="indefinite"/></rect></g>\n')

    # title bar
    w(f'<line x1="{RX}" y1="{RY+46}" x2="{RX+RW}" y2="{RY+46}" stroke="{p["border"]}" stroke-width="1"/>\n')
    for i, c in enumerate(["#EF4444", "#F59E0B", "#22C55E"]):
        w(f'<circle cx="{RX+26+i*18}" cy="{RY+24}" r="5.5" fill="{c}" opacity="{p["dot_o"]}"/>\n')
    w(f'<text x="{RX+RW/2:.0f}" y="{RY+29}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{p["muted"]}" opacity=".8">'
      f'{HANDLE}@github: ~/profile</text>\n')

    # greeting
    w(f'<text x="{RX+50}" y="{RY+108}" font-family="{MONO}" font-size="17" fill="{p["muted"]}" opacity="0">'
      f'Hi <tspan font-size="19">&#128075;</tspan>'
      f'<animate attributeName="opacity" from="0" to=".9" dur=".6s" begin=".3s" fill="freeze"/></text>\n')
    w(f'<text x="{RX+50}" y="{RY+152}" font-family="{MONO}" font-size="34" font-weight="700" fill="{p["text"]}" opacity="0">'
      f"I'm <tspan fill=\"url(#accent)\" filter=\"url(#glowTight)\">{NAME}</tspan>"
      f'<animate attributeName="opacity" from="0" to="1" dur=".7s" begin=".55s" fill="freeze"/>'
      f'<animateTransform attributeName="transform" type="translate" from="0 10" to="0 0" dur=".7s" begin=".55s" fill="freeze"/></text>\n')

    # typing phrases
    w(f'<text x="{RX+50:.0f}" y="{ty:.0f}" font-family="{MONO}" font-size="{fs_t}" fill="url(#accent)" opacity="0">&gt;'
      f'<animate attributeName="opacity" from="0" to="1" dur=".4s" begin="1.1s" fill="freeze"/></text>\n')
    cur_pts = []
    for i, ph in enumerate(PHRASES):
        plain = ph.replace("&amp;", "&")
        pw = cw(fs_t) * len(plain)
        t0 = i * 3.0 + 0.2
        k = [0.0, t0, t0 + 1.15, t0 + 2.35, t0 + 2.65, cycle]
        kt = ";".join(f"{max(0.0, min(1.0, v / cycle)):.4f}" for v in k)
        w(f'<text x="{tx:.0f}" y="{ty:.0f}" font-family="{MONO}" font-size="{fs_t}" fill="{p["text"]}" '
          f'clip-path="url(#tc{i})" opacity=".92">{ph}</text>\n')
        cur_pts.append((t0, tx))
        cur_pts.append((t0 + 1.15, tx + pw))
        cur_pts.append((t0 + 2.35, tx + pw))
        cur_pts.append((t0 + 2.65, tx))

    # one cursor for the whole loop: it rides the end of whichever phrase is
    # being typed, then walks back as that phrase is erased
    cur_pts = [(0.0, tx)] + cur_pts + [(cycle, tx)]
    ckt = ";".join(f"{max(0.0, min(1.0, t / cycle)):.4f}" for t, _ in cur_pts)
    cvx = ";".join(f"{x:.0f}" for _, x in cur_pts)
    w(f'<rect x="{tx:.0f}" y="{ty-fs_t+2:.0f}" width="10" height="{fs_t:.0f}" fill="url(#accent)" opacity="0" filter="url(#glowTight)">'
      f'<animate attributeName="x" values="{cvx}" keyTimes="{ckt}" dur="{cycle:.1f}s" repeatCount="indefinite" calcMode="linear"/>'
      f'<animate attributeName="opacity" values=".95;.95;0;0;.95" keyTimes="0;.42;.45;.92;1" dur="1.1s" begin="1.1s" repeatCount="indefinite" fill="freeze"/>'
      f'</rect>\n')

    # info rows
    iy = RY + 252
    ROW = 31
    icons = {
        "location": 'M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.2A2.2 2.2 0 1 1 8 3.8a2.2 2.2 0 0 1 0 4.4z',
        "cap": 'M8 1 0 5l8 4 6.5-3.25V11H16V5L8 1zM3 8.4V12c0 1.1 2.2 2.5 5 2.5s5-1.4 5-2.5V8.4L8 11 3 8.4z',
        "focus": 'M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm0 2.6A5.4 5.4 0 1 1 8 13.4 5.4 5.4 0 0 1 8 2.6zm0 2.6a2.8 2.8 0 1 0 0 5.6 2.8 2.8 0 0 0 0-5.6z',
        "link": 'M6.9 9.1a3.4 3.4 0 0 0 5.1.4l2-2a3.4 3.4 0 0 0-4.8-4.8l-1.1 1.1a.9.9 0 0 0 1.3 1.3l1.1-1.1a1.6 1.6 0 1 1 2.3 2.3l-2 2a1.6 1.6 0 0 1-2.4-.2.9.9 0 0 0-1.5 1zM9.1 6.9a3.4 3.4 0 0 0-5.1-.4l-2 2a3.4 3.4 0 0 0 4.8 4.8l1.1-1.1a.9.9 0 1 0-1.3-1.3l-1.1 1.1a1.6 1.6 0 1 1-2.3-2.3l2-2a1.6 1.6 0 0 1 2.4.2.9.9 0 0 0 1.5-1z',
        "mail": 'M1 3.5A1.5 1.5 0 0 1 2.5 2h11A1.5 1.5 0 0 1 15 3.5v9A1.5 1.5 0 0 1 13.5 14h-11A1.5 1.5 0 0 1 1 12.5v-9zm1.9.5L8 8.1 13.1 4H2.9zM13.4 5.6 8.5 9.7a.8.8 0 0 1-1 0L2.6 5.6v6.6h10.8V5.6z',
        "linkedin": 'M3.2 1.6a1.6 1.6 0 1 1-3.2 0 1.6 1.6 0 0 1 3.2 0zM.2 4.8H3V16H.2V4.8zM5.3 4.8H8v1.5h.04c.37-.7 1.28-1.44 2.63-1.44 2.81 0 3.33 1.85 3.33 4.25V16h-2.79v-5.4c0-1.29-.02-2.95-1.8-2.95-1.8 0-2.08 1.4-2.08 2.85V16H5.3V4.8z',
    }
    for i, (ic, label, val) in enumerate(INFO):
        y = iy + i * ROW
        beg = 1.5 + i * 0.22
        w(f'<g opacity="0">'
          f'<animate attributeName="opacity" from="0" to="1" dur=".55s" begin="{beg:.2f}s" fill="freeze"/>'
          f'<animateTransform attributeName="transform" type="translate" from="-14 0" to="0 0" dur=".55s" begin="{beg:.2f}s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>\n')
        w(f'<g transform="translate({RX+50},{y-12}) scale(.95)" fill="url(#accent)" opacity=".95"><path d="{icons[ic]}"/></g>\n')
        w(f'<text x="{RX+82}" y="{y}" font-family="{MONO}" font-size="14" fill="{p["muted"]}">{label}</text>\n')
        w(f'<text x="{RX+192}" y="{y}" font-family="{MONO}" font-size="14" fill="{p["text"]}" opacity=".95">{val}</text>\n')
        w('</g>\n')

    # skills
    sy = iy + (len(INFO) - 1) * ROW + 34
    w(f'<text x="{RX+50}" y="{sy}" font-family="{MONO}" font-size="12.5" letter-spacing="1.6" fill="{p["muted"]}" opacity="0">'
      f'SKILLS<animate attributeName="opacity" from="0" to=".8" dur=".5s" begin="2.6s" fill="freeze"/></text>\n')
    w(f'<style>.pill{{transition:transform .2s ease}} .pill:hover{{transform:scale(1.06)}}</style>\n')
    px0, py0 = RX + 50, sy + 16
    px, py = px0, py0
    maxw = RW - 100
    fs_p = 13.0
    for i, s in enumerate(SKILLS):
        pw = cw(fs_p) * len(s) + 26
        if px - px0 + pw > maxw:
            px = px0
            py += 34
        beg = 2.75 + i * 0.07
        w(f'<g class="pill" opacity="0" transform-origin="{px+pw/2:.0f} {py+13:.0f}">'
          f'<animate attributeName="opacity" from="0" to="1" dur=".45s" begin="{beg:.2f}s" fill="freeze"/>'
          f'<animateTransform attributeName="transform" type="scale" from=".82" to="1" dur=".45s" begin="{beg:.2f}s" fill="freeze" additive="sum" calcMode="spline" keySplines=".2 1.2 .3 1"/>\n')
        w(f'<rect x="{px:.0f}" y="{py:.0f}" width="{pw:.0f}" height="27" rx="13.5" fill="{p["pill_bg"]}" stroke="url(#accent)" stroke-opacity=".55" stroke-width="1"/>\n')
        w(f'<rect x="{px:.0f}" y="{py:.0f}" width="{pw:.0f}" height="27" rx="13.5" fill="none" stroke="url(#accent)" stroke-width="1" opacity="0" filter="url(#glowTight)">'
          f'<animate attributeName="opacity" values="0;.55;0" dur="{3.2+i*0.13:.2f}s" begin="{beg+0.5:.2f}s" repeatCount="indefinite"/></rect>\n')
        w(f'<text x="{px+pw/2:.0f}" y="{py+18:.0f}" text-anchor="middle" font-family="{MONO}" font-size="{fs_p}" fill="{p["text"]}" opacity=".92">{s}</text>\n')
        w('</g>\n')
        px += pw + 10

    # social icons
    soc_y = RY + RH - 32
    socials = [
        ("github", 'M9 0a9 9 0 0 0-2.85 17.54c.45.08.62-.2.62-.44l-.01-1.53c-2.5.55-3.03-1.2-3.03-1.2-.41-1.04-1-1.32-1-1.32-.82-.56.06-.55.06-.55.9.06 1.38.93 1.38.93.8 1.38 2.1.98 2.62.75.08-.58.31-.98.57-1.2-2-.23-4.1-1-4.1-4.45 0-.98.35-1.79.93-2.42-.1-.23-.4-1.15.09-2.4 0 0 .75-.24 2.47.92a8.6 8.6 0 0 1 4.5 0c1.72-1.16 2.47-.92 2.47-.92.49 1.25.18 2.17.09 2.4.58.63.93 1.44.93 2.42 0 3.46-2.1 4.22-4.11 4.44.32.28.61.83.61 1.68l-.01 2.5c0 .24.16.52.62.43A9 9 0 0 0 9 0z'),
        ("linkedin", 'M3.6 1.8a1.8 1.8 0 1 1-3.6 0 1.8 1.8 0 0 1 3.6 0zM.25 5.4h3.1V18H.25V5.4zM6 5.4h2.97v1.72h.04c.41-.78 1.42-1.6 2.93-1.6 3.13 0 3.71 2.06 3.71 4.74V18h-3.1v-6.1c0-1.45-.03-3.32-2.02-3.32-2.03 0-2.34 1.58-2.34 3.21V18H6V5.4z'),
        ("mail", 'M1 3.5A1.5 1.5 0 0 1 2.5 2h13A1.5 1.5 0 0 1 17 3.5v11a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 1 14.5v-11zm2.2.5L9 9.2 14.8 4H3.2zm12.3 1.8L9.5 11.3a.8.8 0 0 1-1 0L2.5 5.8v8.2h13V5.8z'),
        ("globe", 'M9 0a9 9 0 1 0 0 18A9 9 0 0 0 9 0zM7.2 2.3A12 12 0 0 0 5.9 6H3.3a6.9 6.9 0 0 1 3.9-3.7zM9 2.1c.6.9 1.2 2.2 1.6 3.9H7.4C7.8 4.3 8.4 3 9 2.1zM2.5 7.6h3.1A17 17 0 0 0 5.5 9c0 .5 0 1 .1 1.4H2.5a7 7 0 0 1 0-2.8zm.8 4.4h2.6c.3 1.4.7 2.6 1.3 3.7A6.9 6.9 0 0 1 3.3 12zM9 15.9c-.6-.9-1.2-2.2-1.6-3.9h3.2c-.4 1.7-1 3-1.6 3.9zm1.9-5.5H7.1A15 15 0 0 1 7 9c0-.5 0-1 .1-1.4h3.8c.1.4.1.9.1 1.4s0 1-.1 1.4zm-.1 5.3c.6-1.1 1-2.3 1.3-3.7h2.6a6.9 6.9 0 0 1-3.9 3.7zM12.4 10.4c.1-.5.1-.9.1-1.4s0-1-.1-1.4h3.1a7 7 0 0 1 0 2.8h-3.1zM14.7 6h-2.6a12 12 0 0 0-1.3-3.7A6.9 6.9 0 0 1 14.7 6z'),
    ]
    for i, (nm, d) in enumerate(socials):
        cx = RX + 50 + i * 46
        beg = 3.8 + i * 0.15
        w(f'<g class="pill" opacity="0" transform-origin="{cx+9} {soc_y+9}">'
          f'<animate attributeName="opacity" from="0" to=".9" dur=".5s" begin="{beg:.2f}s" fill="freeze"/>\n')
        w(f'<g transform="translate({cx},{soc_y})" fill="url(#accent)" filter="url(#glowTight)"><path d="{d}"/></g>\n')
        w('</g>\n')

    # footer hint
    w(f'<text x="{RX+RW-50}" y="{soc_y+13}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{p["muted"]}" opacity="0">'
      f'building things that survive production'
      f'<animate attributeName="opacity" from="0" to=".65" dur=".7s" begin="4.4s" fill="freeze"/></text>\n')

    w('</svg>\n')
    return o.getvalue()


here = os.path.dirname(os.path.abspath(__file__))
for theme in ("dark", "light"):
    path = os.path.join(here, f"{theme}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build(theme))
    print(path, os.path.getsize(path), "bytes")
