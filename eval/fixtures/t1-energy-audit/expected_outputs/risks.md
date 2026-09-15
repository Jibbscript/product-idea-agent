# Risk Assessment

## Risk Matrix

| Risk | Category | Severity | Likelihood | Score | Mitigation |
|------|----------|----------|------------|-------|------------|
| Smartphone thermal sensor accuracy insufficient | Technical | 4 | 3 | 12 | Early prototyping and testing |
| Apple restricts thermal API access | Technical | 5 | 2 | 10 | Build fallback manual scanning mode |
| Low app store conversion rates | Market | 3 | 3 | 9 | Strong ASO, content marketing |
| Competitor launches similar app | Market | 3 | 3 | 9 | Move fast, build brand |
| Users can't interpret thermal results | Execution | 3 | 3 | 9 | AI detection, clear UX |
| Contractor marketplace slow to build | Execution | 3 | 4 | 12 | Start with referral links, build marketplace later |
| Seasonal demand variation | Financial | 2 | 4 | 8 | Plan marketing around heating/cooling seasons |
| High churn after single audit | Financial | 3 | 4 | 12 | Add ongoing value (monitoring, tips) |

## Critical Risks (Score >= 12)

### Smartphone Thermal Sensor Accuracy
- **Description**: iPhone thermal sensors are designed for system monitoring, not precision thermal imaging. Accuracy for detecting air leaks may be insufficient.
- **Impact if realized**: Core value proposition fails; product doesn't work
- **Mitigation strategy**:
  - Prototype and test with real homes before full development
  - Compare against FLIR images for calibration
  - Set appropriate user expectations about precision
- **Contingency**: Pivot to hybrid model with optional FLIR attachment support

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
1. **iPhone thermal sensors can detect air leaks**: Validate through prototype testing
2. **Users will pay $30/year for energy insights**: Validate through landing page pricing tests
3. **AI can reliably identify thermal issues**: Validate through labeled dataset training
4. **Contractors will pay for referrals**: Validate through early partnership discussions

## Constraints
- **Platform limitation**: iPhone 15 Pro+ only initially (limits addressable market)
- **Seasonal usage**: Higher demand in fall/winter; need to plan marketing accordingly
- **App Store policies**: Must comply with Apple guidelines for sensor access

## Dependencies
- **Apple thermal API**: Core functionality depends on continued API access
- **AI/ML processing**: Requires model training on thermal images
- **Contractor partnerships**: Revenue model depends on referral network
