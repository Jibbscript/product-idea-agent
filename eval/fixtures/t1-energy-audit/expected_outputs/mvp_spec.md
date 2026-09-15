# MVP Specification

## Product Vision
Become the go-to mobile app for homeowners to understand and improve their home's energy efficiency, making professional-grade thermal analysis accessible to everyone.

## MVP Scope

### Must Have (P0)
1. **Thermal Scanning**: Access device thermal sensor, capture and display thermal images - Core value delivery
2. **AI Issue Detection**: Automatically identify and label potential air leaks, insulation gaps, and HVAC issues - Differentiation from raw camera apps
3. **Room-by-Room Workflow**: Guided audit flow covering major rooms with prompts for key areas (windows, doors, outlets) - User guidance

### Should Have (P1)
1. **Savings Calculator**: Estimate annual savings from fixing identified issues
2. **Report Generation**: Exportable PDF report for contractor quotes or rebate applications
3. **History Tracking**: Compare before/after scans to measure improvement

### Won't Have (v1)
- **Contractor Marketplace**: Requires local partnership development - Phase 2
- **Smart Home Integration**: Not essential for core value - Phase 2
- **Multi-property Management**: Enterprise feature - Phase 3
- **Utility Bill Import**: Nice to have but complex to implement - Future

## Technical Approach
- **Platform**: iOS (iPhone 15 Pro+ with thermal sensor) - Android follow-on
- **Stack**: Swift/SwiftUI, Core ML for on-device AI, CloudKit for sync
- **Dependencies**: Apple thermal sensor API (ThermalState), OpenAI API for advanced analysis (optional)
- **Build vs Buy**: Build custom thermal analysis (core IP), use standard UI components

## Differentiation

### The Wedge
First app to leverage iPhone's built-in thermal capabilities for consumer-friendly energy audits, eliminating the need for expensive hardware attachments.

### Competitive Advantage
- No additional hardware required (vs FLIR, Seek)
- AI-powered interpretation (vs raw thermal images)
- Guided workflow for non-experts (vs professional tools)
- Fraction of the cost (vs professional auditors)

### Positioning Statement
For DIY homeowners who want to reduce energy bills, Home Energy Leak Mapper is a mobile app that identifies air leaks and insulation gaps using your iPhone's thermal sensor. Unlike expensive thermal cameras or professional auditors, we provide instant, actionable insights at a fraction of the cost.

## Timeline
- **Phase 1** (MVP): Core scanning + AI detection + guided workflow
- **Phase 2**: Savings calculator, report generation, contractor leads
- **MVP Launch**: Target first 100 beta users

## Success Criteria
- **User Activation**: 70% of users complete at least one full room scan
- **Issue Detection**: Users find at least 1 issue per room on average
- **Retention**: 30% of users return within 7 days
- **NPS**: Score > 40 from beta users

## Open Questions
1. How accurate are iPhone thermal sensors for detecting air leaks vs. professional equipment?
2. What's the minimum lighting/temperature differential needed for reliable detection?
3. How do we validate AI detection accuracy before launch?
