/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "on-surface-variant": "#b9cacb",
                        "error": "#ffb4ab",
                        "outline": "#849495",
                        "on-tertiary-container": "#725e00",
                        "secondary-fixed-dim": "#d1bcff",
                        "on-primary-fixed": "#002022",
                        "inverse-primary": "#00696f",
                        "surface-container-high": "#232b2c",
                        "tertiary-fixed": "#ffe173",
                        "primary-fixed": "#6ff6ff",
                        "on-secondary-fixed-variant": "#5700c9",
                        "secondary-container": "#7000ff",
                        "on-tertiary-fixed": "#221b00",
                        "on-tertiary-fixed-variant": "#554500",
                        "on-primary-fixed-variant": "#004f53",
                        "primary": "#e0fdff",
                        "background": "#0d1515",
                        "surface-container-lowest": "#081010",
                        "on-secondary": "#3c0090",
                        "surface-container-highest": "#2e3637",
                        "primary-container": "#00f2fe",
                        "tertiary-container": "#fed83a",
                        "surface-dim": "#0d1515",
                        "surface": "#0d1515",
                        "on-tertiary": "#3b2f00",
                        "surface-bright": "#333b3b",
                        "primary-fixed-dim": "#00dce6",
                        "inverse-surface": "#dce4e4",
                        "on-surface": "#dce4e4",
                        "inverse-on-surface": "#2a3232",
                        "on-error": "#690005",
                        "surface-container": "#192122",
                        "error-container": "#93000a",
                        "surface-variant": "#2e3637",
                        "tertiary": "#fff6e4",
                        "surface-container-low": "#151d1e",
                        "on-error-container": "#ffdad6",
                        "on-secondary-container": "#ddcdff",
                        "on-primary": "#00373a",
                        "surface-tint": "#00dce6",
                        "secondary-fixed": "#e9ddff",
                        "on-secondary-fixed": "#23005b",
                        "outline-variant": "#3a494b",
                        "secondary": "#d1bcff",
                        "on-primary-container": "#006a70",
                        "on-background": "#dce4e4",
                        "tertiary-fixed-dim": "#e8c423"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                    "spacing": {
                        "stack-lg": "32px",
                        "stack-md": "16px",
                        "container-max": "1440px",
                        "margin": "32px",
                        "stack-sm": "8px",
                        "unit": "4px",
                        "gutter": "24px"
                    },
                    "fontFamily": {
                        "body-lg": ["Inter"],
                        "display-lg": ["Inter"],
                        "console-text": ["JetBrains Mono"],
                        "label-mono": ["JetBrains Mono"],
                        "body-sm": ["Inter"],
                        "headline-sm": ["Inter"],
                        "body-md": ["Inter"],
                        "headline-md": ["Inter"]
                    },
                    "fontSize": {
                        "body-lg": ["18px", { "lineHeight": "1.6", "fontWeight": "400" }],
                        "display-lg": ["48px", { "lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "console-text": ["12px", { "lineHeight": "1.5", "fontWeight": "400" }],
                        "label-mono": ["13px", { "lineHeight": "1.4", "letterSpacing": "0.05em", "fontWeight": "500" }],
                        "body-sm": ["14px", { "lineHeight": "1.5", "fontWeight": "400" }],
                        "headline-sm": ["24px", { "lineHeight": "1.3", "fontWeight": "600" }],
                        "body-md": ["16px", { "lineHeight": "1.6", "fontWeight": "400" }],
                        "headline-md": ["32px", { "lineHeight": "1.2", "letterSpacing": "-0.01em", "fontWeight": "600" }]
                    }
                }
            }
        }