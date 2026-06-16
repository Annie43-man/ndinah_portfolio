import flet as ft
import flet_video as fv
import os
import base64

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, "profile.jpg"), "rb") as f:
    profile_b64 = base64.b64encode(f.read()).decode("utf-8")

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

def sym_pad(horizontal=0, vertical=0):
    return ft.Padding.symmetric(horizontal=horizontal, vertical=vertical)

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

    def home_page():
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
                padding=sym_pad(horizontal=16, vertical=12),
                border=ft.Border.all(1, CARD_BORDER),
                expand=True,
            )

        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row([
                        ft.CircleAvatar(
                            foreground_image_src=f"data:image/jpeg;base64,{profile_b64}",
                            radius=80,
                        ),
                        ft.Column([
                            ft.Text("Martin Ndinelao", size=36, color=STAR_WHITE,
                                    weight=ft.FontWeight.BOLD, font_family="Georgia"),
                            ft.Text("Electrical Engineering Student — UNAM", size=16,
                                    color=AURORA1, font_family="Georgia"),
                            ft.Text("Ongwediva, Namibia", size=13,
                                    color=MUTED, font_family="Georgia"),
                            ft.Container(height=12),
                            ft.Row([
                                ft.Container(
                                    content=ft.Text("View Projects", size=12,
                                                    color=AURORA2,
                                                    font_family="Courier New",
                                                    weight=ft.FontWeight.BOLD),
                                    padding=sym_pad(horizontal=16, vertical=8),
                                    border=ft.Border.all(1, AURORA2),
                                    border_radius=20,
                                    ink=True,
                                    on_click=lambda e: navigate("projects"),
                                ),
                                ft.Container(
                                    content=ft.Text("View Experience", size=12,
                                                    color=AURORA1,
                                                    font_family="Courier New",
                                                    weight=ft.FontWeight.BOLD),
                                    padding=sym_pad(horizontal=16, vertical=8),
                                    border=ft.Border.all(1, AURORA1),
                                    border_radius=20,
                                    ink=True,
                                    on_click=lambda e: navigate("experience"),
                                ),
                            ], spacing=12),
                        ], spacing=6, alignment=ft.MainAxisAlignment.CENTER),
                    ], spacing=40, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    height=300,
                    alignment=ft.Alignment(-1, 0),
                ),
                star_divider(),
                ft.Container(height=24),
                ft.Text("About Me", size=22, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=12),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "I am a motivated and dedicated Electrical Engineering student "
                            "with a strong passion for technology, innovation, and problem-solving. "
                            "Through my academic studies and project work, I have developed a solid "
                            "foundation in engineering principles while continuously seeking "
                            "opportunities to expand my technical knowledge and practical skills. "
                            "I enjoy analyzing challenges, finding effective solutions, and applying "
                            "engineering concepts to real-world situations.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                        ft.Container(height=12),
                        ft.Text(
                            "I am a hardworking, adaptable, and goal-oriented individual with "
                            "strong teamwork, communication, and organizational skills. I thrive "
                            "in collaborative environments where I can contribute ideas, learn from "
                            "others, and work toward shared objectives. My commitment to continuous "
                            "learning drives me to stay curious, embrace new challenges, and improve "
                            "both professionally and personally.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                        ft.Container(height=12),
                        ft.Text(
                            "As an aspiring engineer, I am eager to gain valuable industry "
                            "experience, apply my knowledge in practical settings, and contribute "
                            "positively to projects that create meaningful impact. I am committed "
                            "to excellence, professional growth, and developing innovative solutions "
                            "that address modern engineering challenges.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                    ], spacing=0),
                    bgcolor=CARD_BG,
                    border_radius=16,
                    padding=24,
                    border=ft.Border.all(1, CARD_BORDER),
                    expand=True,
                ),
                ft.Container(height=28),
                star_divider(),
                ft.Container(height=24),
                ft.Text("Get in Touch", size=22, color=STAR_WHITE,
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
                ft.Container(height=24),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def skills_page():
        def skill_category(title, color, skills, height=150):
            skill_chips = ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(skill, size=11, color=color,
                                        font_family="Courier New",
                                        weight=ft.FontWeight.BOLD),
                        padding=sym_pad(horizontal=14, vertical=7),
                        border=ft.Border.all(1, color),
                        border_radius=20,
                        bgcolor=CARD_BG,
                    )
                    for skill in skills
                ],
                spacing=8,
                wrap=True,
            )
            return ft.Container(
                content=ft.Column([
                    ft.Text(title, size=16, color=STAR_WHITE,
                            weight=ft.FontWeight.BOLD, font_family="Georgia"),
                    ft.Container(height=12),
                    skill_chips,
                ], spacing=4),
                bgcolor=CARD_BG,
                border_radius=16,
                padding=24,
                border=ft.Border.all(1, color),
                expand=True,
                height=height,
            )

        return ft.Column(
            controls=[
                ft.Text("Skills", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text("Technical & Soft Skills", size=16,
                        color=AURORA1, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=24),
                ft.Row([
                    skill_category("💻 Programming Languages", AURORA1,
                                   ["Python", "JavaScript", "React Native"], 160),
                    skill_category("🛠️ Engineering Software", AURORA2,
                                   ["MATLAB", "LTspice", "AutoCAD", "MATLAB App Designer", "Simulink"], 160),
                ], spacing=16, expand=True),
                ft.Container(height=16),
                ft.Row([
                    skill_category("⚙️ Developer Tools", AURORA3,
                                   ["VS Code", "Git", "GitHub", "Expo", "Firebase", "React Native"], 220),
                    skill_category("🤝 Soft Skills", GOLD,
                                   ["Leadership", "Public Speaking", "Teamwork",
                                    "Project Management", "Communication",
                                    "Problem Solving", "Time Management"], 220),
                ], spacing=16, expand=True),
                ft.Container(height=16),
                ft.Row([
                    skill_category("⚡ Electrical Engineering", AURORA1,
                                   ["Circuit Analysis", "AC/DC Power Systems",
                                    "RLC Circuit Design", "BJT & MOSFET Theory",
                                    "Analogue Electronics", "Three-Phase Systems",
                                    "Thévenin & Norton Theorems"], 200),
                ], spacing=16, expand=True),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        )

    def projects_page():
        def project_card(title, role, description, tech_stack, color, github_url=None):
            tech_badges = ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(tech, size=10, color=color,
                                        font_family="Courier New",
                                        weight=ft.FontWeight.BOLD),
                        padding=sym_pad(horizontal=10, vertical=4),
                        border=ft.Border.all(1, color),
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
                ft.Text(description, size=13, color=TEXT, font_family="Georgia"),
                ft.Container(height=12),
                tech_badges,
            ]
            if github_url:
                controls.append(ft.Container(height=12))
                controls.append(
                    ft.Container(
                        content=ft.Text("View on GitHub", size=11, color=color,
                                        font_family="Courier New",
                                        weight=ft.FontWeight.BOLD),
                        padding=sym_pad(horizontal=14, vertical=7),
                        border=ft.Border.all(1, color),
                        border_radius=20,
                        ink=True,
                        on_click=lambda e, u=github_url: page.launch_url(u),
                    )
                )
            return ft.Container(
                content=ft.Column(controls=controls, spacing=4),
                bgcolor=CARD_BG,
                border_radius=16,
                padding=24,
                border=ft.Border.all(1, color),
                expand=True,
            )

        return ft.Column(
            controls=[
                ft.Text("Projects", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text("Things I've built", size=16,
                        color=AURORA1, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=24),
                project_card(
                    title="Fix-Flow — Water Leak Reporting App",
                    role="Assistant Project Manager · Frontend Developer",
                    description=(
                        "A mobile app built for residents of Ongwediva to report water leaks "
                        "and infrastructure issues in real time. Served as Assistant Project "
                        "Manager in a 15-member team and personally developed ReportScreen.js "
                        "— the core home screen featuring a live leak counter, report "
                        "submission, and emergency contact display."
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
            ("MATLAB Onramp",                            "3 March 2026",  "1q7-d7p14utH42EZ7JfguIwE2_Sx32I-L", AURORA1),
            ("Calculations with Vectors and Matrices",   "6 March 2026",  "1_jOFafOH0w8Dagq7lW60x21NNiX5a8vD", AURORA2),
            ("MATLAB Desktop Tools and Troubleshooting", "8 March 2026",  "1P2tEwFmffLezYaPFDYqEEVeQ097Br0-2", AURORA3),
            ("Make and Manipulate Matrices",             "20 March 2026", "1PuA_DQMcUxkTC4Yw25Um6k6wpn8wkVRN", GOLD),
            ("Explore Data with MATLAB Plots",           "20 March 2026", "13CIFmY0O_K0Afd7e1Cq5Wo3mdTq5Zt0J", AURORA1),
            ("Machine Learning Onramp",                  "18 April 2026", "1rBXFtK5J5Z97eX2POqHVCMYrpgqi99Zp", AURORA2),
            ("Simulink Onramp",                          "24 April 2026", "1FkjknSGWrJISwW3jufVsYoTj4i11cHDU", AURORA3),
        ]

        def open_cert(file_id):
            url = f"https://drive.google.com/file/d/{file_id}/view"
            page.launch_url(url)

        def make_card(name, date, file_id, color):
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
                        padding=sym_pad(horizontal=12, vertical=6),
                        border=ft.Border.all(1, color),
                        border_radius=20,
                        ink=True,
                        on_click=lambda e, fid=file_id: open_cert(fid),
                    ),
                ], spacing=6),
                bgcolor=CARD_BG,
                border_radius=16,
                padding=20,
                border=ft.Border.all(1, color),
                expand=True,
            )

        cards = [make_card(n, d, fid, c) for n, d, fid, c in courses]

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
                    ft.Row(controls=cards[4:6],acing=16),
                    ft.Row(controls=cards[6:],  spacing=16),
                ], spacing=16),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def timeline_page():
        def week_card(week, dates, phase, title, contributions, color):
            bullet_items = [
                ft.Row([
                    ft.Container(width=6, height=6, bgcolor=color, border_radius=3),
                    ft.Text(item, size=12, color=TEXT,
                            font_family="Georgia", expand=True),
                ], spacing=10)
                for item in contributions
            ]
            return ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(
                            content=ft.Text(f"Week {week}", size=11, color=color,
                                            font_family="Courier New",
                                            weight=ft.FontWeight.BOLD),
                            padding=sym_pad(horizontal=12, vertical=5),
                            border=ft.Border.all(1, color),
                            border_radius=20,
                        ),
                        ft.Container(
                            content=ft.Text(phase, size=10, color=MUTED,
                                            font_family="Courier New",
                                            weight=ft.FontWeight.BOLD),
                            padding=sym_pad(horizontal=10, vertical=5),
                            bgcolor=NEBULA,
                            border_radius=20,
                        ),
                        ft.Text(dates, size=11, color=MUTED,
                                font_family="Courier New"),
                    ], spacing=10),
                    ft.Container(height=8),
                    ft.Text(title, size=15, color=STAR_WHITE,
                            weight=ft.FontWeight.BOLD, font_family="Georgia"),
                    ft.Container(height=8),
                    *bullet_items,
                ], spacing=4),
                bgcolor=CARD_BG,
                border_radius=16,
                padding=20,
                border=ft.Border.all(1, color),
            )

        return ft.Column(
            controls=[
                ft.Text("Project Timeline", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text("My individual journey through the semester", size=16,
                        color=AURORA1, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=24),
                week_card("1–2", "02–13 Mar", "PHASE 0", "Team Setup", [
                    "Joined Group 13 as Assistant Project Manager",
                    "Helped set up the GitHub repository",
                    "Set up Expo + React Native + Firebase on my machine",
                ], MUTED),
                ft.Container(height=12),
                week_card("3–4", "16–27 Mar", "PHASE 1", "Pitch Week & Public Speaking", [
                    "Contributed to pitching the Fix-Flow idea to Mr. Abisai",
                    "Fix-Flow officially registered and approved",
                ], AURORA3),
                ft.Container(height=12),
                week_card("5–8", "30 Mar–25 Apr", "PHASE 2", "SRS & MATLAB Certificates", [
                    "Helped complete and submit the SRS document",
                ], GOLD),
                ft.Container(height=12),
                week_card("9–12", "27 Apr–30 May", "PHASE 3", "ReportScreen Development", [
                    "Developed ReportScreen.js — the main home screen of Fix-Flow",
                    "PR #7 submitted and successfully merged",
                    "Reviewed team pull requests and resolved merge conflicts",
                ], AURORA2),
                ft.Container(height=12),
                week_card("13", "01–06 Jun", "PHASE 4A", "Live Demo", [
                    "Part of the team that presented the live Expo demo to Mr. Abisai",
                    "Submitted PR #20 with additional improvements",
                ], AURORA1),
                ft.Container(height=12),
                week_card("14", "08–15 Jun", "PHASE 4B", "Final Submission", [
                    "Helped finalise and build the APK via Expo EAS",
                    "Submitted this personal portfolio as final deliverable",
                ], GOLD),
                ft.Container(height=24),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        )

    def blog_page():
        return ft.Column(
            controls=[
                ft.Text("Blog", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text("Semester Project Reflection", size=16,
                        color=AURORA1, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=24),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Project Reflection Video", size=22,
                                color=STAR_WHITE, weight=ft.FontWeight.BOLD,
                                font_family="Georgia"),
                        ft.Container(height=8),
                        ft.Text(
                            "Below is my individual semester project reflection video for "
                            "Fix-Flow — a water leak reporting mobile app built for the "
                            "residents of Ongwediva. The video details my specific contributions "
                            "to the project as Assistant Project Manager and Frontend Developer.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                    ], spacing=4),
                    bgcolor=CARD_BG,
                    border_radius=16,
                    padding=24,
                    border=ft.Border.all(1, CARD_BORDER),
                ),
                ft.Container(height=20),
                ft.Container(
                    content=ft.Column([
                        ft.Text("▶  Reflection Video", size=14, color=AURORA1,
                                font_family="Courier New",
                                weight=ft.FontWeight.BOLD),
                        ft.Container(height=12),
                        fv.Video(
                            playlist=[fv.VideoMedia("Reflection Video.mp4")],
                            width=700,
                            height=400,
                            autoplay=False,
                            show_controls=True,
                            expand=False,
                        ),
                        ft.Container(height=10),
                        ft.Text(
                            "Duration: ≤ 1 min 30 sec  ·  Individual contribution reflection",
                            size=11, color=MUTED, font_family="Courier New",
                        ),
                    ], spacing=0),
                    bgcolor=CARD_BG,
                    border_radius=16,
                    padding=24,
                    border=ft.Border.all(1, AURORA1),
                ),
                ft.Container(height=20),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Written Summary", size=18, color=STAR_WHITE,
                                weight=ft.FontWeight.BOLD, font_family="Georgia"),
                        ft.Container(height=10),
                        ft.Text(
                            "My primary contribution to Fix-Flow was the design and "
                            "development of ReportScreen.js — the main home screen of the "
                            "application. This screen gives residents a live view of active "
                            "water leaks, a button to submit new reports, access to all "
                            "existing reports, and emergency contact details.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                        ft.Container(height=10),
                        ft.Text(
                            "As Assistant Project Manager I also helped coordinate our "
                            "15-member team: reviewing pull requests, resolving merge "
                            "conflicts, and keeping the GitHub workflow running smoothly "
                            "across the semester.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                        ft.Container(height=10),
                        ft.Text(
                            "This project taught me a lot, not just about React Native and "
                            "Firebase, but about what it truly means to work in a real team. "
                            "Dealing with merge conflicts, coordinating 15 people, reviewing "
                            "pull requests, and meeting deadlines showed me what software "
                            "development actually looks like in practice. I learned that "
                            "engineering is not just circuits and equations, it is "
                            "communication, problem solving under pressure, and building "
                            "things that genuinely help people. Fix-Flow was built for real "
                            "residents of Ongwediva, and that is not a class exercise, that "
                            "is real impact. This has been one of the most rewarding "
                            "experiences of my academic journey so far, and I leave this "
                            "semester more confident, more skilled, and more excited than "
                            "ever about the engineer I am becoming. I am proud of what our "
                            "team built, and I am grateful for every challenge that came "
                            "with it. Thank you.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                    ], spacing=0),
                    bgcolor=CARD_BG,
                    border_radius=16,
                    padding=24,
                    border=ft.Border.all(1, CARD_BORDER),
                ),
                ft.Container(height=24),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    def experience_page():
        def exp_card(title, role, period, description, color, details=None, screenshots=None):
            controls = [
                ft.Row([
                    ft.Container(
                        content=ft.Text(role, size=10, color=color,
                                        font_family="Courier New",
                                        weight=ft.FontWeight.BOLD),
                        padding=sym_pad(horizontal=10, vertical=4),
                        border=ft.Border.all(1, color),
                        border_radius=20,
                    ),
                ]),
                ft.Container(height=8),
                ft.Text(title, size=20, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text(period, size=11, color=MUTED, font_family="Courier New"),
                ft.Container(height=10),
                ft.Text(description, size=13, color=TEXT, font_family="Georgia"),
            ]
            if details:
                controls.append(ft.Container(height=10))
                for item in details:
                    controls.append(
                        ft.Row([
                            ft.Container(width=6, height=6, bgcolor=color, border_radius=3),
                            ft.Text(item, size=12, color=TEXT, font_family="Georgia"),
                        ], spacing=10)
                    )
            if screenshots:
                controls.append(ft.Container(height=12))
                controls.append(ft.Text("Screenshots", size=12, color=MUTED,
                                        font_family="Courier New",
                                        weight=ft.FontWeight.BOLD))
                controls.append(ft.Container(height=8))
                controls.append(
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Image(src=s, width=320, height=200,
                                                 border_radius=ft.BorderRadius.all(8)),
                                border=ft.Border.all(1, color),
                                border_radius=ft.BorderRadius.all(8),
                            )
                            for s in screenshots
                        ],
                        spacing=12,
                    )
                )
            return ft.Container(
                content=ft.Column(controls=controls, spacing=4),
                bgcolor=CARD_BG,
                border_radius=16,
                padding=24,
                border=ft.Border.all(1, color),
                expand=True,
            )

        return ft.Column(
            controls=[
                ft.Text("Experience", size=42, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Text("Leadership, projects & speaking", size=16,
                        color=AURORA1, font_family="Georgia"),
                ft.Container(height=8),
                star_divider(),
                ft.Container(height=24),
                exp_card(
                    title="Fix-Flow — Water Leak Reporting App",
                    role="Assistant Project Manager · Frontend Developer",
                    period="2026 — University of Namibia (UNAM)",
                    description=(
                        "Served as Assistant Project Manager in a 15-member development "
                        "team building Fix-Flow, a mobile app that allows residents of "
                        "Ongwediva to report water leaks and infrastructure issues in real "
                        "time. Assisted in coordinating team efforts, managing Git workflow, "
                        "reviewing pull requests, and ensuring timely delivery of the project."
                    ),
                    color=AURORA1,
                    details=[
                        "Contributed as part of a team of 15 developers",
                        "Personally developed ReportScreen.js — the core home screen",
                        "Assisted in managing GitHub repo, pull requests and merge conflicts",
                        "Tech stack: React Native, Expo, Firebase, JavaScript",
                    ],
                    screenshots=["ReportScreen.png"],
                ),
                ft.Container(height=16),
                exp_card(
                    title="MATLAB GUI Calculator",
                    role="Solo Developer",
                    period="2026 — University of Namibia (UNAM)",
                    description=(
                        "Designed and built a desktop GUI calculator using MATLAB App "
                        "Designer as part of coursework. The app features two tabs covering "
                        "Ohm's Law & Power calculations and RLC Impedance analysis, styled "
                        "with a custom Midnight Galaxy dark theme."
                    ),
                    color=AURORA2,
                    details=[
                        "Tab 1: Ohm's Law and Power calculations",
                        "Tab 2: RLC Impedance analysis",
                        "Custom Midnight Galaxy dark theme design",
                        "Built independently using MATLAB App Designer",
                    ],
                    screenshots=["matlab_calc_1.png", "matlab_calc_2.png"],
                ),
                ft.Container(height=16),
                exp_card(
                    title="Motivational Speaker — Annual Awards Ceremony",
                    role="Public Speaker",
                    period="13 March 2026 — Ruacana High School, Ruacana",
                    description=(
                        "Invited to deliver a motivational speech at Ruacana High School's "
                        "Annual Award Giving Ceremony. Addressed the full school body of "
                        "learners, sharing insights on university life and encouraging "
                        "students to work hard and pursue their academic goals."
                    ),
                    color=AURORA3,
                    details=[
                        "Spoke to the full Ruacana High School learner body",
                        "Shared personal experience of university life at UNAM",
                        "Encouraged learners to study hard and aim for higher education",
                        "Annual Award Giving Ceremony — 13 March 2026",
                    ],
                ),
            ],
            spacing=0,
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
                        ft.Container(height=12),
                        ft.Image(src="PR7 .png", width=700,
                                 border_radius=ft.BorderRadius.all(8)),
                    ], spacing=4),
                    bgcolor=CARD_BG, border_radius=16, padding=20,
                    border=ft.Border.all(1, AURORA1), expand=True,
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
                        ft.Container(height=12),
                        ft.Image(src="PR20 .png", width=700,
                                 border_radius=ft.BorderRadius.all(8)),
                        ft.Container(height=12),
                        ft.Image(src="PR20-2.png", width=700,
                                 border_radius=ft.BorderRadius.all(8)),
                    ], spacing=4),
                    bgcolor=CARD_BG, border_radius=16, padding=20,
                    border=ft.Border.all(1, AURORA3), expand=True,
                ),
                ft.Container(height=24),
                ft.Text("Impact Summary", size=28, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Georgia"),
                ft.Container(height=12),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "As Assistant Project Manager for Group 13, I coordinated team "
                            "efforts and ensured individual contributions were tracked and "
                            "merged correctly. My direct code contribution was the "
                            "ReportScreen.js - the core home screen of the Fix-Flow app, "
                            "which allows residents of Ongwediva to report and view water "
                            "leaks and active infrastructure issues.",
                            size=13, color=TEXT, font_family="Georgia",
                        ),
                        ft.Container(height=16),
                        ft.Text("Top Contributors Graph", size=14, color=GOLD,
                                font_family="Courier New", weight=ft.FontWeight.BOLD),
                        ft.Container(height=8),
                        ft.Image(src="TOP-COMMITERS GRAPH.png", width=700,
                                 border_radius=ft.BorderRadius.all(8)),
                    ], spacing=4),
                    bgcolor=CARD_BG, border_radius=16, padding=20,
                    border=ft.Border.all(1, GOLD), expand=True,
                ),
                ft.Container(height=24),
            ],
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )

    content_area = ft.Container(
        content=home_page(),
        expand=True,
        padding=40,
        bgcolor=BG,
    )

    nav_buttons = {}

    def navigate(route):
        pages = {
            "about":      home_page(),
            "skills":     skills_page(),
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
                btn.border        = ft.Border.only(bottom=ft.BorderSide(2, AURORA1))
                btn.content.color = AURORA1
                btn.content.weight = ft.FontWeight.BOLD
            else:
                btn.border        = ft.Border.only(bottom=ft.BorderSide(2, "transparent"))
                btn.content.color = MUTED
                btn.content.weight = ft.FontWeight.NORMAL
        page.update()

    def make_nav_btn(label, route):
        btn = ft.Container(
            content=ft.Text(label, size=12, color=MUTED, font_family="Georgia"),
            padding=sym_pad(horizontal=10, vertical=12),
            bgcolor="transparent",
            border=ft.Border.only(bottom=ft.BorderSide(2, "transparent")),
            ink=True,
            on_click=lambda e, r=route: navigate(r),
        )
        nav_buttons[route] = btn
        return btn

    navbar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("MARTIN NDINELAO", size=13, color=STAR_WHITE,
                        weight=ft.FontWeight.BOLD, font_family="Courier New"),
                ft.Row(
                    controls=[
                        make_nav_btn("Home",       "about"),
                        make_nav_btn("Skills",     "skills"),
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
        padding=sym_pad(horizontal=32, vertical=0),
        border=ft.Border.only(bottom=ft.BorderSide(1, CARD_BORDER)),
    )

    navigate("about")

    page.add(
        ft.Column(
            controls=[navbar, content_area],
            spacing=0,
            expand=True,
        )
    )

import os
port = int(os.environ.get("FLET_SERVER_PORT", 8000))
ft.run(main, view=ft.AppView.WEB_BROWSER, assets_dir=".", port=port)