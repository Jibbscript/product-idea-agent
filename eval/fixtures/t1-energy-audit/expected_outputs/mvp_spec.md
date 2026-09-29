# MVP Specification

## Product Vision
Become the go-to mobile app for homeowners to understand and improve their home's energy efficiency, making professional-grade thermal analysis accessible to everyone.

## MVP Scope

### Must Have (P0)
1. **Thermal Capture**: Connect to clip-on FLIR ONE cameras (Gen 3, Edge / Edge Pro) through the FLIR Mobile SDK, then capture and display radiometric (per-pixel temperature) frames - Core value delivery
2. **AI Issue Detection**: Automatically identify and label potential air leaks, insulation gaps, and HVAC issues in the radiometric frames - Differentiation from raw camera apps
3. **Room-by-Room Workflow**: Guided audit flow covering major rooms with prompts for key areas (windows, doors, outlets) - User guidance
4. **Temperature-Difference Check**: Pull the local outdoor temperature from a weather API and block insulation scans below a 10°C / 18°F indoor-outdoor difference; for air-leak checks, guide the user to depressurize the house by running bathroom and kitchen exhaust fans - Results the user can trust in any season
5. **No-Camera Guided Draft Check**: Visual checklist plus an incense / smoke-pencil walkthrough for users without a thermal camera - Value before (or without) a camera. P0 rather than P1 because it is part of the free tier and the main answer to the top activation risk, homeowners who have no camera and will not buy one

### Should Have (P1)
1. **Savings Calculator**: Estimate annual savings from fixing identified issues
2. **Report Generation**: Exportable PDF report for contractor quotes or rebate applications
3. **History Tracking**: Compare before/after scans to measure improvement

### Won't Have (v1)
- **Contractor Marketplace**: Requires local partnership development - Phase 2
- **Smart Home Integration**: Not essential for core value - Phase 2
- **Multi-property Management**: Enterprise feature - Phase 3
- **Utility Bill Import**: Nice to have but complex to implement - Future
- **Non-FLIR Cameras (Seek, TOPDON, InfiRay)**: Seek Nano has no third-party SDK; TOPDON and InfiRay have only community reverse-engineered UVC access on Android - Future (Android UVC)

## Technical Approach
- **Platform**: iOS first, then Android, both through the FLIR Mobile SDK. Supported cameras: FLIR ONE Gen 3 (iOS Lightning, the USB-C version for iPhone 15+, and Android USB-C) and the wireless (Wi-Fi) FLIR ONE Edge / Edge Pro
- **Stack**: Swift/SwiftUI on iOS, then Kotlin on Android; Core ML for on-device AI on iOS; CloudKit for sync
- **Dependencies**: FLIR Mobile SDK (free of charge; developers must apply and be approved, and FLIR reviews and approves the app before public release), a weather API for the outdoor temperature, OpenAI API for advanced analysis (optional)
- **Build vs Buy**: Buy camera access and radiometric data (FLIR Mobile SDK), build custom thermal analysis (core IP), use standard UI components

## Differentiation

### The Wedge
A bring-your-own-camera energy audit: guided, AI-annotated scans for the FLIR ONE cameras homeowners already own or borrow from library lending programs, on iOS and Android, with no kit to buy. HomeBoost's $99 BoostBox kit (launched October 2024) moved first; the wedge is people who already own or can borrow a FLIR ONE and do not want to buy a kit, plus Android users, whom its iPhone-plug-in kit does not serve.

### Competitive Advantage
- Bring your own camera: works with FLIR ONE cameras people already own or borrow from libraries, no kit purchase (vs HomeBoost BoostBox)
- iOS and Android through the FLIR SDK, including the wireless Edge (vs HomeBoost's kit camera, which plugs into iPhones)
- AI-powered interpretation of each image (vs raw thermal images)
- Before/after tracking over time, plus contractor referrals in phase 2
- Guided workflow for non-experts (vs professional tools)
- Fraction of the cost (vs professional auditors)
- Honest limit: for homeowners with no camera to use, HomeBoost's all-in $99 kit costs less than buying a FLIR ONE ($149.99-$199.99), so HomeBoost is the cheaper path for them

### Positioning Statement
For DIY homeowners who want to reduce energy bills and own or can borrow a clip-on FLIR ONE thermal camera, Home Energy Leak Mapper is a mobile app that turns that camera into a guided, AI-interpreted energy audit that identifies air leaks and insulation gaps. Unlike HomeBoost's $99 kit, FLIR's own app or professional auditors, we work with the camera you already have on iOS or Android, label every image with AI, and track before/after results over time.

## Timeline
- **Phase 1** (MVP): Apply to the FLIR developer program at the start; FLIR SDK capture + AI detection + guided workflow + temperature-difference check + no-camera draft check
- **Phase 2**: Savings calculator, report generation, contractor leads
- **MVP Launch**: Pass FLIR's pre-release app review, then target first 100 beta users

## Success Criteria
- **User Activation**: 70% of users with a supported camera complete at least one full room scan
- **Issue Detection**: Users find at least 1 issue per room on average
- **Retention**: 30% of users return within 7 days
- **NPS**: Score > 40 from beta users

## Open Questions
1. Is 80x60 clip-on resolution (FLIR ONE Gen 3 / Edge) enough for the AI to flag common air leaks and insulation gaps, or do reliable results need 160x120 (Edge Pro)?
2. How long do FLIR developer approval and FLIR's pre-release app review take, and what could cause either to be denied or delayed?
3. What's the minimum temperature differential needed for reliable air-leak detection with exhaust-fan depressurization? (Insulation checks need at least 10°C / 18°F.)
4. How do we validate AI detection accuracy before launch?
