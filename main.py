import flet as ft

# --- BRAND CONFIGURATION ---
BRAND_COLOR = "#00E5FF"  # Cyan: Represents AI Intelligence
BG_COLOR = "#0F1115"     # Dark Matter: Represents Security & Depth
TEXT_COLOR = "#FFFFFF"   # Pure White: Clarity
SEC_COLOR = "#1A1D24"    # Secondary Background

# --- CONTENT ASSETS ---
CONTACT_EMAIL = "tundetronics@gmail.com"
CONTACT_PHONE = "08165409044"

def main(page: ft.Page):
    # 1. PAGE SETUP
    page.title = "Owo-Nexus AI | Sovereign Orchestration"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG_COLOR
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    
    # Fonts
    page.fonts = {
        "Orbitron": "https://github.com/google/fonts/raw/main/ofl/orbitron/Orbitron-Bold.ttf",
        "Roboto": "https://github.com/google/fonts/raw/main/apache/roboto/Roboto-Regular.ttf"
    }

    # --- COMPONENTS ---

    # A. NAVIGATION BAR
    def build_navbar():
        return ft.Container(
            content=ft.Row([
                ft.Row([
                    ft.Icon(ft.icons.TOKEN, color=BRAND_COLOR, size=30),
                    ft.Text("OWO-NEXUS", size=24, font_family="Orbitron", weight="bold"),
                ]),
                ft.Row([
                    ft.TextButton("SERVICES", style=ft.ButtonStyle(color=TEXT_COLOR)),
                    ft.TextButton("SHIELDTRADE", style=ft.ButtonStyle(color=TEXT_COLOR)),
                    ft.ElevatedButton(
                        "INITIALIZE CONSULT", 
                        bgcolor=BRAND_COLOR, 
                        color="black",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                    )
                ], alignment=ft.MainAxisAlignment.END, expand=True)
            ]),
            padding=ft.padding.symmetric(horizontal=40, vertical=20),
            bgcolor=BG_COLOR
        )

    # B. HERO SECTION ( The Hook)
    def build_hero():
        return ft.Container(
            content=ft.Column([
                ft.Text(
                    "WE DO NOT BUILD APPS.\nWE ARCHITECT INTELLIGENCE.", 
                    size=50, 
                    weight="bold", 
                    font_family="Orbitron",
                    text_align=ft.TextAlign.CENTER,
                    color=TEXT_COLOR
                ),
                ft.Text(
                    "Agentive AI Orchestration • Business Automation • Sovereign Systems",
                    size=18,
                    color="grey",
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(height=20),
                ft.Row([
                    ft.ElevatedButton(
                        "VIEW SYSTEMS", 
                        bgcolor=BRAND_COLOR, 
                        color="black", 
                        height=50,
                        width=200
                    ),
                    ft.OutlinedButton(
                        "READ MANIFESTO", 
                        style=ft.ButtonStyle(color=BRAND_COLOR, side=ft.BorderSide(1, BRAND_COLOR)),
                        height=50,
                        width=200
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=80,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[BG_COLOR, "#142229"]
            )
        )

    # C. SERVICE GRID (The Revenue Engines)
    def service_card(icon, title, desc):
        return ft.Container(
            content=ft.Column([
                ft.Icon(icon, size=40, color=BRAND_COLOR),
                ft.Container(height=10),
                ft.Text(title, size=20, weight="bold", font_family="Orbitron"),
                ft.Container(height=10),
                ft.Text(desc, size=14, color="grey")
            ]),
            padding=30,
            bgcolor=SEC_COLOR,
            border_radius=10,
            border=ft.border.only(left=ft.BorderSide(4, BRAND_COLOR)),
            width=350,
            height=250
        )

    def build_services():
        return ft.Container(
            content=ft.Column([
                ft.Text("THE NEXUS CAPABILITIES", size=30, font_family="Orbitron", color="white"),
                ft.Container(height=40),
                ft.ResponsiveRow([
                    ft.Column([service_card(
                        ft.icons.AUTO_MODE, 
                        "AUTOMATION", 
                        "Deployment of autonomous bots to handle sales, inventory (Oriflame), and customer service."
                    )], col={"sm": 12, "md": 4}),
                    ft.Column([service_card(
                        ft.icons.SECURITY, 
                        "SOVEREIGN SECURITY", 
                        "MDM Parental Control protocols and Enterprise Cybersecurity auditing."
                    )], col={"sm": 12, "md": 4}),
                    ft.Column([service_card(
                        ft.icons.SHOW_CHART, 
                        "WEALTH ARCHITECTURE", 
                        "Implementation of 'Profit Architect' financial models and P2P exchange systems."
                    )], col={"sm": 12, "md": 4}),
                ], spacing=20)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=60,
            bgcolor=BG_COLOR
        )

    # D. AUTHORITY FOOTER (The Contact)
    def build_footer():
        return ft.Container(
            content=ft.Column([
                ft.Divider(color="grey"),
                ft.Row([
                    ft.Column([
                        ft.Text("OWO-NEXUS AI", size=20, weight="bold", color=BRAND_COLOR),
                        ft.Text("Prince Babatunde Adesina Jalaruru", weight="bold"),
                        ft.Text("AI Consultant | Rotary President of Presidents")
                    ]),
                    ft.Column([
                        ft.Text("CONTACT HUB", weight="bold"),
                        ft.Row([ft.Icon(ft.icons.EMAIL, size=16), ft.Text(CONTACT_EMAIL)]),
                        ft.Row([ft.Icon(ft.icons.PHONE, size=16), ft.Text(CONTACT_PHONE)]),
                    ])
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.START)
            ]),
            padding=40,
            bgcolor=SEC_COLOR
        )

    # --- ASSEMBLY ---
    page.add(
        build_navbar(),
        build_hero(),
        build_services(),
        build_footer()
    )

ft.app(target=main)
