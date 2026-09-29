# Installation Guide

Product Idea Agent ships as a Claude Code plugin, `product-idea-agent`, from a single-plugin marketplace named `jibbscript` that lives in this repository. Installing the plugin gives you all twelve skills under the `product-idea-agent:` namespace, together with the artifact contracts they validate against.

## Prerequisites

- Claude Code, installed and signed in ([setup guide](https://code.claude.com/docs/en/setup)). The maintainers test on v2.1.283 or later.
- No API keys. Research skills use Claude Code's built-in WebSearch and WebFetch tools.

## Remove an old copy-install first

Earlier versions of this pack were installed by copying `skills/*` into `~/.claude/skills/` or a project's `.claude/skills/`. Those copies are un-namespaced, and their contract references do not resolve outside the plugin, so if they stay they keep triggering beside the plugin and produce artifacts that are never checked against a contract.

List the copies this pack left behind (they carry `pack: product-idea-agent` in their frontmatter):

```bash
find ~/.claude/skills .claude/skills -name SKILL.md -exec grep -l "pack: product-idea-agent" {} + 2>/dev/null
```

Then delete each listed skill directory, for example:

```bash
rm -rf ~/.claude/skills/idea-validation-orchestrator
```

Only remove directories the first command lists: another plugin or a personal skill of yours may use a generic name such as `risk-assessment`.

## Install

In a Claude Code session:

```text
/plugin marketplace add Jibbscript/product-idea-agent
/plugin install product-idea-agent@jibbscript
```

Or from your shell:

```bash
claude plugin marketplace add Jibbscript/product-idea-agent
```

```bash
claude plugin install product-idea-agent@jibbscript
```

Run `/reload-plugins` in any session that was already open.

## Verify

```bash
claude plugin details product-idea-agent
```

The component inventory lists twelve skills. In a session, typing `/product-idea-agent:` offers them in autocomplete.

## Update

You stay on the version you installed until the maintainer publishes a new one: a new version is a bump of `version` in `.claude-plugin/plugin.json`, so work-in-progress commits never change the skills under a running validation. To take a new version, open the **Installed** tab in `/plugin` and choose **Update now**, or run:

```bash
claude plugin update product-idea-agent@jibbscript
```

The next session loads the new version; an open session keeps the old one until `/reload-plugins`. Validations in progress resume from the artifacts already in your project directory, since the plugin never writes there itself.

## Uninstall

```bash
claude plugin uninstall product-idea-agent@jibbscript
```

To forget the marketplace as well:

```bash
claude plugin marketplace remove jibbscript
```

Your artifacts stay where they were written, in your project directories.

## Enable it for a team

Commit this to a repository's `.claude/settings.json`, and everyone who opens the repository and trusts it is offered the same marketplace and plugin:

```json
{
  "extraKnownMarketplaces": {
    "jibbscript": {
      "source": { "source": "github", "repo": "Jibbscript/product-idea-agent" }
    }
  },
  "enabledPlugins": {
    "product-idea-agent@jibbscript": true
  }
}
```

Organizations that restrict marketplaces can allowlist this one by repository with `{ "source": "github", "repo": "Jibbscript/product-idea-agent" }` in `strictKnownMarketplaces` in managed settings.

## Load a working copy (contributors)

To try local changes without installing or publishing anything, start Claude Code with the checkout as a session-only plugin:

```bash
claude --plugin-dir /path/to/product-idea-agent
```

Run `/reload-plugins` after editing a skill. See [Contributing](CONTRIBUTING.md) for the checks to run before a PR.

## Tools the skills use

| Tool | Skills | Purpose |
|------|--------|---------|
| Read, Write | All | Read upstream artifacts, write this step's artifact |
| WebSearch, WebFetch | Research skills and the orchestrator | Market data, competitor pages, community threads |
| Grep, Edit | A few | Search artifacts, revise an existing one |

A skill's `allowed-tools` pre-approves those tools for the turn that invokes it, so a full validation runs without a permission prompt for every search; your permission settings still apply to everything else. `scorecard-generator` and `validation-report` also set `disallowed-tools: WebSearch WebFetch`, which removes web access while they run, so the verdict is built only from artifacts already on disk. See [Security](SECURITY.md).

## Troubleshooting

**The skills don't appear.** Check `claude plugin list` shows `product-idea-agent@jibbscript` as enabled, then run `/reload-plugins` or start a new session.

**Two copies of a skill appear, one without the `product-idea-agent:` prefix.** That is an old copy-install; remove it as described above.

**Another plugin also has a `risk-assessment` or `market-sizing` skill.** Invoke this pack's by its namespaced name, such as `/product-idea-agent:risk-assessment`. The orchestrator already calls every step by its namespaced name.

**A skill can't find its contract.** Contracts are read from `${CLAUDE_PLUGIN_ROOT}/contracts/`, which Claude Code fills in only for plugin skills. A copy of a skill outside the plugin can't resolve it; install the plugin instead.

## Next steps

- [Usage Guide](USAGE.md) for running a validation
- [Security](SECURITY.md) for how the pack handles web content and tools
