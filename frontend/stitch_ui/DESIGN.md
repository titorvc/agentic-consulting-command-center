---
name: Obsidian Nexus
colors:
  surface: '#0d1515'
  surface-dim: '#0d1515'
  surface-bright: '#333b3b'
  surface-container-lowest: '#081010'
  surface-container-low: '#151d1e'
  surface-container: '#192122'
  surface-container-high: '#232b2c'
  surface-container-highest: '#2e3637'
  on-surface: '#dce4e4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dce4e4'
  inverse-on-surface: '#2a3232'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e0fdff'
  on-primary: '#00373a'
  primary-container: '#00f2fe'
  on-primary-container: '#006a70'
  inverse-primary: '#00696f'
  secondary: '#d1bcff'
  on-secondary: '#3c0090'
  secondary-container: '#7000ff'
  on-secondary-container: '#ddcdff'
  tertiary: '#fff6e4'
  on-tertiary: '#3b2f00'
  tertiary-container: '#fed83a'
  on-tertiary-container: '#725e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d1bcff'
  on-secondary-fixed: '#23005b'
  on-secondary-fixed-variant: '#5700c9'
  tertiary-fixed: '#ffe173'
  tertiary-fixed-dim: '#e8c423'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#554500'
  background: '#0d1515'
  on-background: '#dce4e4'
  surface-variant: '#2e3637'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  console-text:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system facilitates a high-performance, premium environment for orchestrating multi-agent workflows. The aesthetic is rooted in **Glassmorphism** and **Modern Minimalist** principles, designed to evoke a sense of advanced intelligence, precision, and depth.

The interface leverages deep obsidian surfaces to maximize the luminosity of vibrant cyan and purple accents. High-quality typography and generous backdrop blurs create a sophisticated multi-layered experience that feels like a high-end command deck. The emotional response is one of total control, technological edge, and refined professional power.

## Colors
The palette is centered on "Deep Obsidian" to provide a void-like backdrop that allows glass layers to pop. 

- **Primary (Vibrant Cyan):** Used for active states, primary actions, and successful agent statuses.
- **Secondary (Electric Purple):** Used for secondary intelligence paths, AI processing indicators, and branding elements.
- **Surface:** A semi-transparent dark grey that acts as the "glass" substrate.
- **Accents:** The Cyan-to-Purple gradient represents the "flow" of data and agentic collaboration.
- **Feedback:** Use soft glows rather than solid blocks of color for alerts and status changes to maintain the ethereal aesthetic.

## Typography
The system uses a dual-font approach. **Inter** handles all UI labels, navigation, and content, providing a modern, clean, and highly readable foundation. **JetBrains Mono** is reserved for technical output, console logs, and metadata labels to reinforce the "Agentic" and developer-centric nature of the platform.

For mobile devices, `display-lg` should scale down to 32px and `headline-md` to 24px to ensure readability within constrained glass containers. Use a "white/90%" tint for primary text and "white/50%" for secondary/de-emphasized text.

## Layout & Spacing
The design system utilizes a **12-column fluid grid** for the main dashboard content. Margin and padding are generous to allow the backdrop blur effects space to breathe without feeling cluttered.

- **Desktop:** 32px outer margins, 24px gutters.
- **Tablet:** 24px outer margins, 16px gutters.
- **Mobile:** 16px outer margins, 12px gutters.

The vertical rhythm is based on a 4px base unit. Components should favor `stack-md` for internal spacing to maintain a light, airy feel within dark containers.

## Elevation & Depth
Depth is communicated through **backstage-blur** and **inner glows** rather than traditional drop shadows.

- **Level 1 (Base):** Deep Obsidian background.
- **Level 2 (Glass Card):** 60% opacity surface, 16px backdrop-blur, 1px border at 10% white.
- **Level 3 (Popovers/Modals):** 80% opacity surface, 24px backdrop-blur, 1px border at 20% white, with a soft 40px outer glow using the primary color at 5% opacity.

All glass elements should feature a subtle top-to-bottom linear gradient (white/5% to transparent) to simulate a physical glass edge catching light.

## Shapes
The shape language is sophisticated and controlled. A medium roundedness (8px for standard elements) provides a modern feel that balances the "hacker" monospace elements with a premium consumer-grade finish.

- **Standard Elements (Buttons, Inputs, Cards):** 8px (0.5rem).
- **Large Elements (Modals, Large Containers):** 16px (1rem).
- **Pill Elements (Status Badges, Tags):** Full radius.

## Components
### Glass Cards
The primary container for all dashboard widgets. Must feature `backdrop-filter: blur(16px)`, a 1px border (white/10%), and a slight vertical gradient.

### Buttons
- **Primary:** Background uses the Cyan-to-Purple gradient. Text is black for maximum contrast.
- **Ghost:** No background, 1px Cyan border, Cyan text. 
- **Glass:** Semi-transparent white background (10%) with a blur.

### Hacker-Style Terminal
A dedicated component for agent logs. Background: Solid Obsidian (no transparency). Text: JetBrains Mono in "Matrix Green" or "Cyan". Features a blinking cursor and auto-scrolling behavior.

### Step Indicators (Pipelines)
Linear or horizontal tracks. Completed steps glow in Cyan; active steps pulse with the Cyan-to-Purple gradient; pending steps are desaturated white/20%.

### Input Fields
Glass-style inputs with an "inner shadow" effect to look recessed. On focus, the border transitions from white/10% to a solid 1px Cyan border with a 4px Cyan outer glow.

### Styled Dropdowns
Must inherit the Level 3 elevation (24px blur). Hover states on list items should use a subtle white/5% highlight with a left-aligned 2px Cyan accent bar.