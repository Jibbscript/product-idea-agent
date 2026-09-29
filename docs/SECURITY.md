# Security Best Practices

This document covers security considerations for using and developing Product Idea Agent skills.

## Overview

The skill pack interacts with web content and generates analysis based on external data. Following these practices helps protect against common risks.

## Risk Categories

### 1. Credential Exposure

**Risk**: API keys or secrets accidentally included in skills or outputs.

**Mitigations**:
- The pack needs no API keys: research runs on Claude Code's built-in WebSearch and WebFetch
- Never hardcode credentials in skill files
- Review outputs before sharing externally

### 2. Prompt Injection from Web Content

**Risk**: Malicious web content could attempt to influence analysis or tool usage.

**Mitigations**:
- Every research skill (demand-signals, problem-segment, competitive-landscape, market-sizing, pricing-wtp, gtm-channels) states in its Working section that fetched page content is evidence to cite, never instructions to follow
- The synthesis skills that set the verdict, scorecard-generator and validation-report, have no web access at all (`disallowed-tools: WebSearch WebFetch`), so a hostile page can reach the verdict only through an artifact you can read
- Critical analysis should be verified manually
- Be skeptical of unusual recommendations

**Signs of Potential Injection**:
- Unexpected tool calls or file operations
- Analysis that contradicts visible evidence
- Instructions appearing in "quotes" from sources

### 3. Data Privacy

**Risk**: Sensitive business information could be exposed or retained.

**Mitigations**:
- Don't include truly confidential data in prompts
- Review generated artifacts before sharing
- Use placeholder names for stealth-mode ideas
- Understand that prompts may be logged

**Data Categories**:
| Category | OK to Include | Consider Anonymizing |
|----------|---------------|---------------------|
| Public market data | Yes | No |
| Competitor info (public) | Yes | No |
| Your business idea | Yes | If stealth |
| Customer names | Avoid | Yes |
| Financial details | Avoid | Yes |
| Personal info | No | Always |

### 4. Terms of Service Compliance

**Risk**: Automated web access could violate site terms or rate limits.

**Mitigations**:
- Skills respect robots.txt where applicable
- Built-in rate limiting between requests
- Avoid scraping beyond reasonable research
- Credit sources in outputs

### 5. Unsafe Automation

**Risk**: Unintended actions taken without user awareness.

**How the tool fields work**:
- `allowed-tools` in a skill's frontmatter **pre-approves** tools for the turn that invokes the skill. Research skills pre-approve `WebSearch WebFetch` (and every skill `Read Write`) so a long validation doesn't stop at a prompt for each search. It does not restrict anything; tools it doesn't list follow your permission settings.
- `disallowed-tools` **removes** tools while a skill is active. scorecard-generator and validation-report remove WebSearch and WebFetch.
- Deny rules in your permission settings still override a skill's pre-approval.

**Mitigations**:
- Review the frontmatter of any skill before installing it; `claude plugin details product-idea-agent` shows the plugin's components
- Artifacts are written only to the current project directory, where you can read every one
- The orchestrator posts a one-line status at each phase boundary

## Safe Defaults

The skill pack uses these default configurations:

```yaml
web_fetch_defaults:
  timeout_seconds: 30
  rate_limit_per_domain: "1 request per 3 seconds"
  max_response_size_mb: 10
  follow_redirects_max: 5
  javascript_execution: false
  cookie_handling: reject_all

content_processing:
  strip_html_tags: true
  remove_hidden_text: true
  max_tokens_per_fetch: 5000
  content_delimiter: "--- EXTERNAL CONTENT ---"

data_handling:
  pii_collection: avoid
  retention: session_only
```

## Security Checklist for Users

Before running validation:
- [ ] No confidential data in idea description
- [ ] Placeholder names used if stealth mode needed
- [ ] Understood that web searches may be visible
- [ ] Review outputs before sharing externally

After running validation:
- [ ] Check artifacts for any sensitive info
- [ ] Verify critical claims independently
- [ ] Remove or redact before public sharing

## Security Checklist for Skill Authors

**Credentials**:
- [ ] No API keys in skill files
- [ ] Document any required variables in README (the pack currently needs none)

**Web Operations**:
- [ ] Respect robots.txt directives
- [ ] Implement rate limiting (3-5 sec between requests)
- [ ] Handle 429 errors gracefully
- [ ] Don't require login or bypass authentication

**Content Safety**:
- [ ] State in the skill that fetched content is evidence, not instructions
- [ ] Put `WebSearch WebFetch` in `disallowed-tools` for any skill that must not reach the web
- [ ] Don't execute content from web sources
- [ ] Validate content type before processing
- [ ] Strip potentially malicious elements

**Output Safety**:
- [ ] Don't echo raw web content to outputs
- [ ] Paraphrase sources; mark any reproduced wording as a quotation with its source
- [ ] Flag uncertain or unverifiable claims
- [ ] Include source attribution

## Reporting Security Issues

If you discover a security vulnerability:

1. **Do not** open a public issue
2. Email security concerns to [maintainer email]
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We aim to respond within 48 hours and address critical issues promptly.

## Third-Party Dependencies

The skill pack has minimal dependencies:

| Component | Security Consideration |
|-----------|----------------------|
| Claude Code | Anthropic security practices |
| Python (eval) | Standard library only |
| YAML parsing | PyYAML safe_load only |
| JSON parsing | Standard library |

No external packages are required for core functionality.

## Audit Log

For compliance needs, consider:

1. Saving generated artifacts to version control
2. Logging Claude Code sessions
3. Documenting validation decisions
4. Retaining source citations

## Updates

This security guide is reviewed quarterly. Check the repository for the latest version.

Last updated: 2026-09
