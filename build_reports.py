import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    KeepTogether,
    HRFlowable
)

def create_lab6_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()

    # Custom styles
    primary = colors.HexColor("#1A365D")
    secondary = colors.HexColor("#2B6CB0")
    dark_gray = colors.HexColor("#2D3748")
    light_bg = colors.HexColor("#F7FAFC")
    border_color = colors.HexColor("#E2E8F0")

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=primary,
        alignment=0,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=secondary,
        alignment=0,
        spaceAfter=15
    )
    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=primary,
        spaceBefore=14,
        spaceAfter=6
    )
    h2_style = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=secondary,
        spaceBefore=10,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=dark_gray,
        spaceAfter=6
    )
    code_style = ParagraphStyle(
        "Code_Custom",
        parent=styles["Normal"],
        fontName="Courier",
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#1A202C")
    )
    callout_style = ParagraphStyle(
        "Callout_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#2C5282")
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("Lab 6: Code & Branch Coverage Analysis Report", title_style))
    story.append(Paragraph("<b>Student:</b> Vaibhav Tulsian &nbsp;|&nbsp; <b>Repository:</b> Lab_L6_L7_20_food_delivery &nbsp;|&nbsp; <b>Application:</b> food_delivery.py", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=secondary, spaceAfter=12))

    # 1. Executive Summary & Objective
    story.append(Paragraph("1. Objective & Overview", h1_style))
    story.append(Paragraph(
        "This laboratory focuses on measuring, analyzing, and maximizing test coverage using Python's <code>coverage</code> "
        "and <code>pytest</code> tools. Test suites were designed to differentiate between statement (line) coverage and "
        "branch coverage, uncovering untested logical paths and achieving <b>100% Code Coverage</b> and <b>100% Branch Coverage</b> "
        "(surpassing the mandatory 90% threshold).",
        body_style
    ))

    # 2. Concept Comparison Table
    story.append(Paragraph("2. Conceptual Comparison: Line vs Branch Coverage", h1_style))
    concept_data = [
        [Paragraph("<b>Metric</b>", body_style), Paragraph("<b>Definition</b>", body_style), Paragraph("<b>Limitation / Vulnerability</b>", body_style)],
        [
            Paragraph("<b>Line Coverage</b>", body_style),
            Paragraph("Measures whether each line of source code executed at least once during test execution.", body_style),
            Paragraph("Gives a false sense of security; does not check whether boolean conditional branches evaluated to both True and False.", body_style)
        ],
        [
            Paragraph("<b>Branch Coverage</b>", body_style),
            Paragraph("Measures whether every decision point / branch (if, elif, else) evaluated to both True and False.", body_style),
            Paragraph("Forces comprehensive testing of all decision outcomes, edge conditions, and boundary values.", body_style)
        ]
    ]
    t_concept = Table(concept_data, colWidths=[1.3*inch, 2.7*inch, 3.0*inch])
    t_concept.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), light_bg),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_concept)
    story.append(Spacer(1, 10))

    # 3. Initial Coverage Run
    story.append(Paragraph("3. Step 4: Initial Test Coverage Analysis", h1_style))
    story.append(Paragraph(
        "Executing the baseline starter tests (<code>test_nearby_small_order</code> and <code>test_no_coupon</code>) "
        "yielded <b>36% Line Coverage</b> (21 missing lines out of 33) and only <b>30% Branch Coverage</b> (5 branches partially evaluated).",
        body_style
    ))
    img_initial = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 6/screenshots/lab6_initial_coverage.png"
    if os.path.exists(img_initial):
        story.append(Image(img_initial, width=7.0*inch, height=4.4*inch))
        story.append(Spacer(1, 10))

    # 4. Code Coverage Test Suite
    story.append(Paragraph("4. Step 5: Code Coverage Test Suite (100% Line Coverage)", h1_style))
    story.append(Paragraph(
        "A dedicated suite <code>CodeCoverageTest_food_delivery.py</code> was implemented with 15 test cases covering all execution paths: "
        "invalid delivery distances, free delivery tier (&ge; 500), tier 1 (&le; 3km), tier 2 (&le; 8km), tier 3 (> 8km), rain surcharges, "
        "coupon validation (None, invalid, WELCOME restrictions, order minimums), and estimated delivery times.",
        body_style
    ))
    img_code = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 6/screenshots/lab6_code_coverage.png"
    if os.path.exists(img_code):
        story.append(Image(img_code, width=7.0*inch, height=2.8*inch))
        story.append(Spacer(1, 10))

    # 5. Branch Coverage Test Suite
    story.append(Paragraph("5. Step 7: Branch Coverage Test Suite (100% Branch Coverage)", h1_style))
    story.append(Paragraph(
        "A rigorous suite <code>BranchCoverageTest_food_delivery.py</code> with 23 targeted test cases was created to test both sides of "
        "compound conditionals (e.g. <code>distance_km &lt;= 0 or distance_km &gt; 15</code>), exact boundary values (0, 3, 8, 15, 15.1), "
        "first-order coupon flags (WELCOME with first_order True vs False, order value &ge; 200 vs &lt; 200), and all 4 combinations of peak/busy restaurant status. "
        "This achieved <b>100% Branch Coverage (24/24 branches evaluated, 0 missing)</b>.",
        body_style
    ))
    img_branch = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 6/screenshots/lab6_branch_coverage.png"
    if os.path.exists(img_branch):
        story.append(Image(img_branch, width=7.0*inch, height=2.8*inch))
        story.append(Spacer(1, 10))

    # 6. Results Summary Table
    story.append(Paragraph("6. Coverage Metrics Summary", h1_style))
    metrics_data = [
        [Paragraph("<b>Stage</b>", body_style), Paragraph("<b>Test File</b>", body_style), Paragraph("<b>Stmts / Miss</b>", body_style), Paragraph("<b>Line Cover</b>", body_style), Paragraph("<b>Branches (Total/Miss)</b>", body_style), Paragraph("<b>Branch Cover</b>", body_style)],
        [Paragraph("Initial", body_style), Paragraph("starter test cases", body_style), Paragraph("33 / 21", body_style), Paragraph("36%", body_style), Paragraph("24 / 5 partial", body_style), Paragraph("30%", body_style)],
        [Paragraph("Step 5", body_style), Paragraph("CodeCoverageTest_food_delivery.py", body_style), Paragraph("33 / 0", body_style), Paragraph("<b>100%</b>", body_style), Paragraph("24 / 0", body_style), Paragraph("100%", body_style)],
        [Paragraph("Step 7", body_style), Paragraph("BranchCoverageTest_food_delivery.py", body_style), Paragraph("33 / 0", body_style), Paragraph("<b>100%</b>", body_style), Paragraph("24 / 0", body_style), Paragraph("<b>100%</b>", body_style)],
    ]
    t_metrics = Table(metrics_data, colWidths=[0.8*inch, 2.3*inch, 1.0*inch, 0.9*inch, 1.2*inch, 0.8*inch])
    t_metrics.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), light_bg),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('ALIGN', (2,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_metrics)
    story.append(Spacer(1, 10))

    # 7. Git Commits & Deliverables
    story.append(Paragraph("7. Deliverables & Git Commits", h1_style))
    story.append(Paragraph(
        "All required deliverables have been structured into the repository:<br/>"
        "&bull; <code>CodeCoverageTest_food_delivery.py</code> &mdash; Dedicated suite for code coverage.<br/>"
        "&bull; <code>BranchCoverageTest_food_delivery.py</code> &mdash; Dedicated suite for exhaustive branch testing.<br/>"
        "&bull; <code>test_food_delivery.py</code> &mdash; Complete integrated test suite.<br/>"
        "&bull; Minimum 2 git commits recorded in git history per evaluation rubric.",
        body_style
    ))

    doc.build(story)
    print(f"Lab 6 PDF generated: {output_path}")

def create_lab7_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()

    primary = colors.HexColor("#7B1FA2")
    secondary = colors.HexColor("#9C27B0")
    dark_gray = colors.HexColor("#2D3748")
    light_bg = colors.HexColor("#F3E5F5")
    border_color = colors.HexColor("#E1BEE7")

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=primary,
        alignment=0,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=secondary,
        alignment=0,
        spaceAfter=15
    )
    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=primary,
        spaceBefore=12,
        spaceAfter=5
    )
    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=dark_gray,
        spaceAfter=6
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("Lab 7: Fuzzing for Input Validation Bugs Report", title_style))
    story.append(Paragraph("<b>Student:</b> Vaibhav Tulsian &nbsp;|&nbsp; <b>Repository:</b> Lab_L6_L7_20_food_delivery &nbsp;|&nbsp; <b>Module:</b> food_delivery.py / processor.py", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=secondary, spaceAfter=10))

    # 1. Objective
    story.append(Paragraph("1. Objective & Methodology", h1_style))
    story.append(Paragraph(
        "This lab explores property-based fuzz testing using Python's <b>Hypothesis</b> library. Fuzzing generates unexpected, malformed, "
        "and boundary inputs automatically (Unicode strings, None, empty strings, delimiters without content) to uncover hidden crashes and "
        "vulnerabilities that traditional manual unit tests miss. Defensive programming was then applied to harden all functions against failure.",
        body_style
    ))

    # 2. Step 2: Run Buggy Application
    story.append(Paragraph("2. Step 2: Running the Initial Buggy Application", h1_style))
    story.append(Paragraph(
        "The baseline application ran successfully when given well-behaved, happy-path user inputs (<code>pizza:2,burger:1</code>, <code>4.5</code>, <code>SAVE50</code>). "
        "However, it lacked defensive input validation, leaving it prone to crashing on real-world malformed data.",
        body_style
    ))
    img_step2 = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 7/screenshots/step2_run_buggy_app.png"
    if os.path.exists(img_step2):
        story.append(Image(img_step2, width=7.0*inch, height=2.1*inch))
        story.append(Spacer(1, 8))

    # 3. Step 3 & 4: Hypothesis Fuzz Testing Uncovers Crashes
    story.append(Paragraph("3. Steps 3 & 4: Fuzz Testing with Hypothesis & Bug Discovery", h1_style))
    story.append(Paragraph(
        "Using Hypothesis strategy <code>@given(st.text() | st.none())</code>, we tested <code>parse_order</code>, <code>delivery_eta</code>, "
        "and <code>coupon_discount</code> for crash resistance. Hypothesis immediately generated edge-case inputs that crashed all three functions:",
        body_style
    ))

    bug_table_data = [
        [Paragraph("<b>Function</b>", body_style), Paragraph("<b>Failing Input</b>", body_style), Paragraph("<b>Crash Exception</b>", body_style), Paragraph("<b>Root Cause</b>", body_style)],
        [
            Paragraph("<code>parse_order(s)</code>", body_style),
            Paragraph("<code>s = None</code><br/><code>s = ''</code><br/><code>s = ':'</code>", body_style),
            Paragraph("AttributeError<br/>ValueError (unpacking)<br/>ValueError (int conversion)", body_style),
            Paragraph("No None check; assumes commas and colons always exist; assumes quantity is always a valid integer.", body_style)
        ],
        [
            Paragraph("<code>delivery_eta(s)</code>", body_style),
            Paragraph("<code>s = None</code><br/><code>s = ''</code><br/><code>s = 'abc'</code>", body_style),
            Paragraph("TypeError<br/>ValueError<br/>OverflowError", body_style),
            Paragraph("Direct float() cast without handling None, empty strings, non-numeric strings, or infinite/NaN values.", body_style)
        ],
        [
            Paragraph("<code>coupon_discount(s)</code>", body_style),
            Paragraph("<code>s = None</code><br/><code>s = ''</code><br/><code>s = 'SAVE'</code>", body_style),
            Paragraph("AttributeError<br/>IndexError<br/>ValueError", body_style),
            Paragraph("Direct .upper() on None; assumes 'SAVE' always splits into at least 2 parts; assumes second part contains digits.", body_style)
        ],
    ]
    t_bugs = Table(bug_table_data, colWidths=[1.4*inch, 1.3*inch, 1.8*inch, 2.5*inch])
    t_bugs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), light_bg),
        ('GRID', (0,0), (-1,-1), 0.5, border_color),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_bugs)
    story.append(Spacer(1, 8))

    img_step4 = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 7/screenshots/step4_test_cases_failing.png"
    if os.path.exists(img_step4):
        story.append(Image(img_step4, width=7.0*inch, height=3.8*inch))
        story.append(Spacer(1, 8))

    # 4. Step 5: Fixing the Buggy Application
    story.append(Paragraph("4. Step 5: Defensive Hardening & Running Fixed Code", h1_style))
    story.append(Paragraph(
        "Each function was defensively refactored with comprehensive validation:<br/>"
        "&bull; <b>parse_order</b>: Validates string type and non-empty content; checks for delimiter format; strips whitespace; validates positive integer quantities; ignores malformed entries cleanly without crashing.<br/>"
        "&bull; <b>delivery_eta</b>: Handles None, non-numeric values, negative distances, NaN, and Infinity safely, returning default baseline ETA (15 mins).<br/>"
        "&bull; <b>coupon_discount</b>: Validates string and None; safely detects 'SAVE'; extracts leading numeric digits using regex; returns 0 for non-matching or invalid coupons.",
        body_style
    ))
    img_step5 = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 7/screenshots/step5_run_fixed_app.png"
    if os.path.exists(img_step5):
        story.append(Image(img_step5, width=7.0*inch, height=2.6*inch))
        story.append(Spacer(1, 8))

    # 5. Step 6: Re-Running Test Cases wrt Fixed Code
    story.append(Paragraph("5. Step 6: Verification & Passing Fuzz Tests", h1_style))
    story.append(Paragraph(
        "Re-running <code>pytest test_processor.py</code> with Hypothesis generated hundreds of random inputs across all three functions. "
        "<b>All 3 test suites passed with 0 failures and 0 crashes</b>, demonstrating true robustness against arbitrary inputs.",
        body_style
    ))
    img_step6 = "/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 7/screenshots/step6_test_cases_passing.png"
    if os.path.exists(img_step6):
        story.append(Image(img_step6, width=7.0*inch, height=1.9*inch))
        story.append(Spacer(1, 8))

    # 6. Deliverables summary
    story.append(Paragraph("6. Deliverables Summary", h1_style))
    story.append(Paragraph(
        "&bull; <b>PDF Document with screenshots:</b> Complete documentation with all 4 terminal screenshots.<br/>"
        "&bull; <b>Fixed Application Python Script:</b> <code>food_delivery.py</code> and <code>processor.py</code> hardened against all fuzzing inputs.<br/>"
        "&bull; <b>Updated test_processor.py code:</b> Property-based Hypothesis test suite validating crash resistance.",
        body_style
    ))

    doc.build(story)
    print(f"Lab 7 PDF generated: {output_path}")

if __name__ == "__main__":
    create_lab6_pdf("/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 6/Lab6_Report_Vaibhav_Tulsian.pdf")
    create_lab6_pdf("/Users/vaibhav/Documents/se/lab 6/Lab6_Report_Vaibhav_Tulsian.pdf")
    create_lab7_pdf("/Users/vaibhav/Documents/se/lab 6/Lab_L6_L7_20_food_delivery/Lab 7/Lab7_Report_Vaibhav_Tulsian.pdf")
    create_lab7_pdf("/Users/vaibhav/Documents/se/lab 6/Lab7_Report_Vaibhav_Tulsian.pdf")
