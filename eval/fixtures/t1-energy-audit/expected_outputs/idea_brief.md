# Idea Brief: Home Energy Leak Mapper

## One-Line Pitch
Home Energy Leak Mapper turns a clip-on phone thermal camera into a guided, AI-interpreted DIY home energy audit.

## Problem Statement
Homeowners waste $200-500 annually on energy bills due to invisible air leaks and insulation gaps. Professional energy audits cost $300-500 and require scheduling weeks in advance. Clip-on phone thermal cameras cost about $150-200 (FLIR ONE Gen 3) and require expertise to interpret results. Affordable DIY options are new and limited: HomeBoost's $99 kit launched only in October 2024, and library camera-loan programs exist but no national count does; the known ones cluster in the DC suburbs, and Arlington's drew an 8-month waitlist. Few affordable, accessible ways exist for homeowners to identify and fix these issues themselves.

## Target Customer
DIY-oriented homeowners aged 35-55 in US suburban areas with homes built before 2000. They shop at Home Depot, watch home improvement YouTube videos, and are motivated by both cost savings and environmental impact. They own a smartphone, are comfortable with mobile apps, and will buy, already own, or borrow (for example from a library energy lending program) a clip-on thermal camera such as a FLIR ONE.

## Solution Hypothesis
Be the software layer for a clip-on FLIR ONE thermal camera the homeowner already owns, buys, or borrows from a library: read its radiometric (per-pixel temperature) frames through the FLIR Mobile SDK and combine them with AI-powered interpretation to provide actionable energy audit results. The app guides users room-by-room, labels likely air leaks and insulation gaps, explains severity, calculates potential savings, exports a report, and (phase 2) connects them with local contractors for fixes. Users without a camera still get a no-camera guided draft check.

Key capabilities:
- Guided thermal scanning with a clip-on FLIR ONE camera (iOS and Android, via the FLIR Mobile SDK)
- No-camera guided draft check (visual checklist plus an incense / smoke-pencil walkthrough)
- AI-powered issue detection and severity scoring
- Room-by-room guided audit workflow
- Cost savings calculator
- Contractor matching marketplace

## Key Assumptions
1. Enough homeowners own, buy, or borrow a supported FLIR ONE clip-on thermal camera
2. Clip-on thermal images (80x60 to 160x120) plus AI flag common air leaks and insulation gaps reliably enough for a DIY triage
3. Homeowners will complete a 20-30 minute DIY audit process
4. Users will pay $30/year for premium subscription features
5. 15-20% of scanned issues will result in contractor booking requests
6. Contractor referral fees (10% commission) will provide meaningful revenue

## Success Metrics

### Validation Phase
- 100 beta testers complete full home audit
- 70% report finding "surprising" issues
- 30% request contractor quotes within 7 days

### Launch Phase
- 10,000 downloads in first month
- 15% conversion to paid subscription
- 500 contractor bookings in first quarter

## Created
2024-12-26

## Status
Draft
