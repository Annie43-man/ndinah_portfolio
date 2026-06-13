import flet as ft
import os
import base64

base_dir = r"C:\Users\marti\Desktop\web_portfolio"

with open(os.path.join(base_dir, "profile.jpg"), "rb") as f:
    profile_b64 = base64.b64encode(f.read()).decode("utf-8")

# ── Colours ──────────────────────────────────────
BG          = "#03010a"
NEBULA      = "#0d0621"
CARD_BG     = "#0a0718"
CARD_BORDER = "#1e1340"
AURORA1     = "#b06aff"
AURORA2     = "#5d9fff"
AURORA3     = "#ff6ab0"
GOLD        = "#ffd97d"
TEXT        = "#d8d0f8"
MUTED       = "#5a5080"
STAR_WHITE  = "#f0eeff"

def main(page: ft.Page):
    page.bgcolor = "#03010a"
    page.padding = 0
    page.title   = "Martin Ndinelao — Portfolio"

    def star_divider():
        return ft.Container(
            height=1,
            gradient=ft.LinearGradient(
                colors=["transparent", "#b06aff", "#5d9fff", "transparent"],
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
            ),
        )

    def about_page():
        def info_card(icon_text, label, value, color):
            return ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.Text(icon_text, size=20),
                        width=40,
                        height=40,
                        bgcolor=NEBULA,
                        border_radius=20,
                    ),
                    ft.Column([
                        ft.Text(label, size=10, color=MUTED,
                                font_family="Courier New",
                                weight=ft.FontWeight.BOLD),
                        ft.Text(value, size=13, color=color,
                                font_family="Georgia"),
                    ], spacing=2, tight=True),
                ], spacing=12),
                bgcolor=CARD_BG,
                border_radius=14,
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
                border=ft.border.all(1, CARD_BORDER),
                expand=True,
            )

        description_text = (
            "[ Paste your personal description here. ]"
        )

        return ft.Column(
            controls=[
                ft.Container(height=40),
                ft.Row([
                    ft.CircleAvatar(
                        foreground_image_src=f"data:image/jpeg;base64,{profile_b64}",
                        radius=100,
                    ),
                    ft.Column([
                        ft.Text("Martin Ndinelao", size=36, color=STAR_WHITE,
                                weight=ft.FontWeight.BOLD, font_family="Georgia"),
                        ft.Text("Electrical Engineering Student — UNAM", size=16,
                                color=AURORA1, font_family="Georgia"),
                        ft.Text("Ongwediva, Namibia", size=13,
                                color=MUTED, font_family="Georgia"),
                        ft.Container(height=12),
                        ft.Text(
                            description_text,
                            size=13, color=TEXT, font_family="Georgia",
                            expand=True,
                        ),
                        ft.Container(height=16),
                        ft.Row([
                            ft.Container(
                                content=ft.Text("View Projects", size=12,
                                                color=AURORA2,
                                                font_family="Courier New",
                                                weight=ft.FontWeight.BOLD),
                                padding=ft.padding.symmetric(horizontal=16, vertical=8),
                                border=ft.border.all(1, AURORA2),
                                border_radius=20,
                                ink=True,
                                on_click=lambda e: navigate("projects"),
                            ),
                        ], spacing=12),
                    ], spacing=6),
                ], spacing=40),
                ft.Container(height=32),
                star_divider(),
                ft.Container(height=28),
                ft.Text("Get in Touch", size=28, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=12),
                ft.Row([
                    info_card("✉", "Email",   "martinndinah@gmail.com", AURORA1),
                    info_card("📞", "Phone",  "081 630 5078",           AURORA2),
                ], spacing=12, expand=True),
                ft.Container(height=8),
                ft.Row([
                    info_card("🐙", "GitHub",   "github.com/Annie43-man", AURORA3),
                    info_card("💼", "LinkedIn", "Martin Ndinelao",         GOLD),
                ], spacing=12, expand=True),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def skills_page():
        return ft.Column(
            controls=[
                ft.Text("Skills", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=16),
                ft.Text("Coming soon...", size=13, color=MUTED,
                        font_family="Georgia"),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def portfolio_page():
        def project_card(title, role, description, tech_stack, color, github_url=None):
            tech_badges = ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(tech, size=10, color=color,
                                        font_family="Courier New",
                                        weight=ft.FontWeight.BOLD),
                        padding=ft.padding.symmetric(horizontal=10, vertical=4),
                        border=ft.border.all(1, color),
                        border_radius=20,
                    )
                    for tech in tech_stack
                ],
                spacing=6,
            )

            controls = [
                ft.Text(title, size=18, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text(role, size=11, color=color,
                        font_family="Courier New", weight=ft.FontWeight.BOLD),
                ft.Container(height=8),
                ft.Text(description, size=13, color=TEXT,
                        font_family="Georgia"),
                ft.Container(height=12),
                tech_badges,
            ]

            if github_url:
                controls.append(ft.Container(height=12))
                controls.append(
                    ft.Container(
                        content=ft.Text("View on GitHub", size=11,
                                        color=color, font_family="Courier New",
                                        weight=ft.FontWeight.BOLD),
                        padding=ft.padding.symmetric(horizontal=14, vertical=7),
                        border=ft.border.all(1, color),
                        border_radius=20,
                        ink=True,
                        on_click=lambda e, u=github_url: os.startfile(u),
                    )
                )

            return ft.Container(
                content=ft.Column(controls=controls, spacing=4),
                bgcolor=CARD_BG,
                border_radius=16,
                padding=24,
                border=ft.border.all(1, color),
                expand=True,
            )

        return ft.Column(
            controls=[
                ft.Text("Portfolio", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text("Things I've built", size=16,
                        color=AURORA1, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=24),
                project_card(
                    title="Fix-Flow — Water Leak Reporting App",
                    role="Project Manager",
                    description=(
                        "A mobile app built for residents of Ongwediva to report water leaks "
                        "and infrastructure issues in real time. Led a 16-member team as "
                        "Project Assistant Manager and personally developed ReportScreen.js — the core "
                        "home screen featuring a live leak counter, report submission, and "
                        "emergency contact display."
                    ),
                    tech_stack=["React Native", "Expo", "Firebase", "JavaScript"],
                    color=AURORA1,
                    github_url="https://github.com/git-user01nf/UNAM-I3691CP-WaterLeak-Ongwediva",
                ),
                ft.Container(height=16),
                project_card(
                    title="MATLAB GUI Calculator",
                    role="Solo Developer",
                    description=(
                        "A desktop GUI calculator built in MATLAB App Designer featuring "
                        "two tabs: Ohm's Law & Power calculations (Tab 1) and RLC Impedance "
                        "analysis (Tab 2). Styled with a custom Midnight Galaxy dark theme."
                    ),
                    tech_stack=["MATLAB", "App Designer"],
                    color=AURORA2,
                ),
                ft.Container(height=16),
                project_card(
                    title="Personal Portfolio App",
                    role="Solo Developer",
                    description=(
                        "This portfolio is built entirely in Python using the Flet framework. "
                        "Features a galaxy/space design theme, multi-page navigation, "
                        "MATLAB certificate showcase, and GitHub contribution evidence."
                    ),
                    tech_stack=["Python", "Flet"],
                    color=AURORA3,
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        )

    def matlab_page():
        courses = [
            ("MATLAB Onramp",                            "3 March 2026",  "Matlab Onramp.pdf",                                    AURORA1),
            ("Calculations with Vectors and Matrices",   "6 March 2026",  "Calculation with Vectors and Matrices.pdf",            AURORA2),
            ("MATLAB Desktop Tools and Troubleshooting", "8 March 2026",  "MATLAB Desktop Tools and Troubleshooting Scripts.pdf", AURORA3),
            ("Make and Manipulate Matrices",             "20 March 2026", "Make and Manipulate Matrices.pdf",                    GOLD),
            ("Explore Data with MATLAB Plots",           "20 March 2026", "Explore Data with MATLAB Plots.pdf",                  AURORA1),
            ("Machine Learning Onramp",                  "18 April 2026", "Machine Learning Onramp.pdf",                        AURORA2),
            ("Simulink Onramp",                          "24 April 2026", "Simulink Onramp.pdf",                                AURORA3),
        ]

        def make_card(name, date, filename, color):
            return ft.Container(
                content=ft.Column([
                    ft.Text(name, size=14, color=STAR_WHITE,
                            weight=ft.FontWeight.BOLD, font_family="Georgia"),
                    ft.Text(date, size=11, color=MUTED, font_family="Georgia"),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Text("View Certificate", size=11,
                                        color=color, font_family="Courier New",
                                        weight=ft.FontWeight.BOLD),
                        padding=ft.padding.symmetric(horizontal=12, vertical=6),
                        border=ft.border.all(1, color),
                        border_radius=20,
                        ink=True,
                        on_click=lambda e, f=filename: os.startfile(
                            os.path.join(base_dir, f)
                        ),
                    ),
                ], spacing=6),
                bgcolor=CARD_BG,
                border_radius=16,
                padding=20,
                border=ft.border.all(1, color),
                width=340,
            )

        cards = [make_card(n, d, f, c) for n, d, f, c in courses]

        return ft.Column(
            controls=[
                ft.Text("MATLAB Achievement Hub", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text("7 / 7 courses completed", size=16,
                        color=AURORA1, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=16),
                ft.Column(controls=[
                    ft.Row(controls=cards[0:2], spacing=16),
                    ft.Row(controls=cards[2:4], spacing=16),
                    ft.Row(controls=cards[4:6], spacing=16),
                    ft.Row(controls=cards[6:],  spacing=16),
                ], spacing=16),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def projects_page():
        return ft.Column(
            controls=[
                ft.Text("Projects", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=16),
                ft.Text("Coming soon...", size=13, color=MUTED,
                        font_family="Georgia"),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def blog_page():
        return ft.Column(
            controls=[
                ft.Text("Blog", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=16),
                ft.Text("Coming soon...", size=13, color=MUTED,
                        font_family="Georgia"),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def experience_page():
        return ft.Column(
            controls=[
                ft.Text("Experience", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=16),
                ft.Text("Coming soon...", size=13, color=MUTED,
                        font_family="Georgia"),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def timeline_page():
        return ft.Column(
            controls=[
                ft.Text("Project Timeline", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=16),
                ft.Text("Coming soon...", size=13, color=MUTED,
                        font_family="Georgia"),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def github_page():
        return ft.Column(
            controls=[
                ft.Text("GitHub Evidence", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text("Individual contributions to Fix-Flow", size=16,
                        color=AURORA1, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=16),
                ft.Text("Pull Requests", size=28, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=12),
                ft.Container(
                    content=ft.Column([
                        ft.Text("PR #7 — feat: describe your changes", size=14,
                                color=AURORA1, weight=ft.FontWeight.BOLD,
                                font_family="Georgia"),
                        ft.Text("Status: Merged ✓", size=11, color=AURORA2,
                                font_family="Courier New"),
                        ft.Container(height=6),
                        ft.Text(
                            "Built the complete ReportScreen.js - the main home screen "
                            "of the Fix-Flow Water Leak Management System. This included "
                            "a live leak counter, Report New Water Leak button, View All "
                            "Reports button, emergency contact display, and full stylesheet.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                    ], spacing=4),
                    bgcolor=CARD_BG, border_radius=16, padding=20,
                    border=ft.border.all(1, AURORA1), expand=True,
                ),
                ft.Container(height=12),
                ft.Container(
                    content=ft.Column([
                        ft.Text("PR #20 — Feature/your feature name", size=14,
                                color=AURORA3, weight=ft.FontWeight.BOLD,
                                font_family="Georgia"),
                        ft.Text("Status: Open", size=11, color=MUTED,
                                font_family="Courier New"),
                        ft.Container(height=6),
                        ft.Text(
                            "Ongoing feature contribution to the Fix-Flow app. "
                            "This pull request documents additional screen updates "
                            "and improvements made to the project.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                    ], spacing=4),
                    bgcolor=CARD_BG, border_radius=16, padding=20,
                    border=ft.border.all(1, AURORA3), expand=True,
                ),
                ft.Container(height=24),
                ft.Text("Impact Summary", size=28, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=12),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "As Project Assistant Manager for Group 13, I coordinated team efforts "
                            "and ensured individual contributions were tracked and merged "
                            "correctly. My direct code contribution was the ReportScreen.js "
                            "- the core home screen of the Fix-Flow app, which allows "
                            "residents of Ongwediva to report and view water leaks and "
                            "active infrastructure issues.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                    ], spacing=4),
                    bgcolor=CARD_BG, border_radius=16, padding=20,
                    border=ft.border.all(1, GOLD), expand=True,
                ),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    # ── Content area ─────────────────────────────
    content_area = ft.Container(
        content=about_page(),
        expand=True,
        padding=40,
        bgcolor=BG,
    )

    # ── Nav ───────────────────────────────────────
    nav_buttons = {}

    def navigate(route):
        pages = {
            "about":      about_page(),
            "skills":     skills_page(),
            "portfolio":  portfolio_page(),
            "timeline":   timeline_page(),
            "projects":   projects_page(),
            "blog":       blog_page(),
            "experience": experience_page(),
            "matlab":     matlab_page(),
            "github":     github_page(),
        }
        content_area.content = pages[route]
        for r, btn in nav_buttons.items():
            if r == route:
                btn.border         = ft.border.only(
                    bottom=ft.BorderSide(2, AURORA1))
                btn.content.color  = AURORA1
                btn.content.weight = ft.FontWeight.BOLD
            else:
                btn.border         = ft.border.only(
                    bottom=ft.BorderSide(2, "transparent"))
                btn.content.color  = MUTED
                btn.content.weight = ft.FontWeight.NORMAL
        page.update()

    def make_nav_btn(label, route):
        btn = ft.Container(
            content=ft.Text(label, size=12, color=MUTED,
                            font_family="Georgia"),
            padding=ft.padding.symmetric(horizontal=10, vertical=12),
            bgcolor="transparent",
            border=ft.border.only(bottom=ft.BorderSide(2, "transparent")),
            ink=True,
            on_click=lambda e, r=route: navigate(r),
        )
        nav_buttons[route] = btn
        return btn

    # ── Top navbar ───────────────
    navbar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("MARTIN NDINELAO", size=13, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Courier New"),
                ft.Row(
                    controls=[
                        make_nav_btn("About",      "about"),
                        make_nav_btn("Skills",     "skills"),
                        make_nav_btn("Portfolio",  "portfolio"),
                        make_nav_btn("Timeline",   "timeline"),
                        make_nav_btn("Projects",   "projects"),
                        make_nav_btn("Blog",       "blog"),
                        make_nav_btn("Experience", "experience"),
                        make_nav_btn("MATLAB Hub", "matlab"),
                        make_nav_btn("GitHub",     "github"),
                    ],
                    spacing=0,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        bgcolor=NEBULA,
        padding=ft.padding.symmetric(horizontal=32, vertical=0),
        border=ft.border.only(bottom=ft.BorderSide(1, CARD_BORDER)),
    )

    navigate("about")

    page.add(
        ft.Column(
            controls=[
                navbar,
                content_area,
            ],
            spacing=0,
            expand=True,
        )
    )

ft.app(target=main)