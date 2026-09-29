# Risk Assessment

## Risk Matrix

| Risk | Category | Severity | Likelihood | Score | Mitigation |
|------|----------|----------|------------|-------|------------|
| Homeowners without a camera will not buy one | Market | 4 | 3 | 12 | No-camera free tier, library lending partnerships, later camera-bundle or loaner-kit partnership |
| FLIR SDK access or FLIR's pre-release app approval denied or delayed | Technical | 5 | 2 | 10 | Apply to the FLIR developer program at the start; later, Android UVC support for TOPDON / InfiRay cameras (community-documented access only) |
| DIY scans miss small leaks, or temperature difference too small out of season | Technical | 3 | 4 | 12 | Outdoor-temperature check blocks insulation scans below an 18°F difference; guided exhaust-fan depressurization for leak checks; position as triage before a professional audit |
| Low app store conversion rates | Market | 3 | 3 | 9 | Strong ASO, content marketing |
| HomeBoost and FLIR-approved apps take the segment first | Market | 4 | 3 | 12 | Bring-your-own-camera, library channel, Android support |
| Users can't interpret thermal results | Execution | 3 | 3 | 9 | AI detection, clear UX |
| Contractor marketplace slow to build | Execution | 3 | 4 | 12 | Start with referral links, build marketplace later |
| Seasonal demand variation | Financial | 2 | 4 | 8 | Plan marketing around heating/cooling seasons |
| High churn after single audit | Financial | 3 | 4 | 12 | Add ongoing value (monitoring, tips) |

## Critical Risks (Score >= 12)

### Camera Access
- **Description**: Thermal scans need a supported FLIR ONE clip-on camera, and homeowners without one may not buy one for a single audit. A FLIR ONE Gen 3 lists at $199.99 ($149.99 on sale, Nov-Dec 2024). Library energy-lending programs lend FLIR ONE units for 1-2 weeks (Arlington's first 4 cameras drew an 8-month waitlist), but no national count exists and the known programs cluster in the DC suburbs.
- **Impact if realized**: Activation stalls at the camera step; the serviceable market (about $236M, which already assumes an estimated 25% of the DIY segment can get a camera) shrinks further
- **Mitigation strategy**:
  - Free tier includes a no-camera guided draft check (visual checklist plus an incense / smoke-pencil walkthrough)
  - Partner with library lending programs as an acquisition channel
  - Pursue a camera-bundle or loaner-kit partnership later
- **Contingency**: Lead with the no-camera draft check and library borrowing; speed up the loaner-kit partnership if camera-step drop-off stays high

### DIY Detection Limits and Seasonal Temperature Window
- **Description**: DOE guidance says DIY checks find obvious leaks but not small, hard-to-detect ones; certified assessors pair a blower-door test with infrared imaging. Clip-on images are 80x60 (Gen 3) to 160x120 (Edge Pro). Insulation checks need at least a 10°C / 18°F indoor-outdoor temperature difference (FLIR guidance; ASTM C1060), so they only work in part of the year; air-leak checks work at smaller differences when the house is depressurized.
- **Impact if realized**: Missed leaks and weak out-of-season scans erode trust and overstate savings estimates; users churn
- **Mitigation strategy**:
  - App checks the outdoor temperature and blocks insulation scans below an 18°F difference
  - Guide exhaust-fan depressurization (bathroom and kitchen fans) for leak checks
  - Position the product as triage before a professional audit
- **Contingency**: Route homes with uncertain findings to a professional audit through the contractor referral path

### HomeBoost Head Start
- **Description**: HomeBoost launched its BoostBox on 2024-10-29: a $99 DIY home energy assessment kit (a thermal camera that plugs into an iPhone, a blacklight, and a guided app scan of about 30 minutes that produces a report of upgrades and rebates), available nationwide. FLIR's approved app gallery already lists home-energy apps (Home Boost, HouseRater) built on its SDK. For homeowners with no camera access, HomeBoost's all-in $99 kit is cheaper than buying a FLIR ONE ($149.99-$199.99).
- **Impact if realized**: HomeBoost and FLIR-approved apps own the DIY thermal audit segment before launch; the no-camera segment defaults to HomeBoost
- **Mitigation strategy**:
  - Bring-your-own-camera: works with FLIR ONE cameras people already own or borrow, no kit purchase
  - Library lending channel
  - iOS and Android through the FLIR SDK, including the wireless Edge (HomeBoost's kit camera plugs into iPhones)
  - AI annotation of each image, before/after tracking over time, contractor referrals
- **Contingency**: Concentrate on camera owners and library borrowers, where no kit purchase is needed, and cede kit buyers to HomeBoost

### Contractor Marketplace Development
- **Description**: Building a two-sided marketplace for contractor referrals requires significant local business development.
- **Impact if realized**: Missing major revenue stream; lower user value
- **Mitigation strategy**:
  - Phase 2 launch, not MVP blocker
  - Start with affiliate links to Angi/HomeAdvisor
  - Focus on high-density markets first
- **Contingency**: Partner with existing home services marketplace

### High Churn After Single Audit
- **Description**: Users may audit their home once and not return, leading to high churn.
- **Impact if realized**: LTV too low to support CAC; business model fails
- **Mitigation strategy**:
  - Add seasonal check-in reminders
  - Gamification (efficiency score over time)
  - Before/after comparison features
  - HVAC monitoring features in v2
- **Contingency**: Shift to one-time purchase model if retention too low

## Must-Be-True Assumptions
1. **Enough homeowners own, buy or borrow a supported FLIR ONE camera**: Validate through landing page surveys on camera ownership and library borrowing
2. **80x60 to 160x120 clip-on images plus AI flag common air leaks and insulation gaps reliably enough for DIY triage**: Validate through prototype testing in real homes and labeled dataset training
3. **Users will pay $30/year for energy insights**: Validate through landing page pricing tests
4. **Contractors will pay for referrals**: Validate through early partnership discussions

## Constraints
- **Platform limitation**: FLIR cameras only at launch; Seek Nano has no third-party SDK (limits addressable market)
- **Seasonal usage**: Higher demand in fall/winter, and insulation scans need at least an 18°F indoor-outdoor difference; need to plan marketing accordingly
- **FLIR app review**: FLIR reviews and approves any app before public release

## Dependencies
- **FLIR Mobile SDK**: Core functionality depends on SDK access and FLIR developer approval
- **AI/ML processing**: Requires model training on labeled thermal images
- **Contractor partnerships**: Revenue model depends on referral network
- **Library lending programs**: Acquisition channel for users without a camera; fewer free paths to a scan if unavailable
