# 🤖 Claude Code Development Workflow

> The streamlined guide to autonomous development where Claude implements while you sleep, plan, or drink coffee ☕

**The Big Idea**: Describe what you want → Claude plans it → You approve → Claude builds it autonomously → You do other things.

**Setting Expectations Upfront**:

- ⏱️ **Time Investment**: 1 hour upfront (30 min /spec + 30 min planning)
- 📊 **Completion Rate**: 90-95% autonomous implementation
- 🔄 **Final Step**: You'll review and polish to get to 100%
- ⚠️ **Success Factor**: Quality of spec/planning determines outcome
- 🚫 **Common Mistake**: Rushing the upfront work = frustrating back-and-forth

**The Reality**: This isn't magic. It's a disciplined process that trades upfront clarity for autonomous execution. Do it right, and you get 3-5x productivity. Rush it, and you'll waste time on iterations.

**Why This Works**: It builds on Claude Code's native flow you already know - Planning Mode (Shift-Tab) and telling it to implement. We just add /spec for clarity and let CLAUDE.md handle the rules. By front-loading the thinking, you reduce cognitive load during execution and play to Claude's strengths. Simple, familiar, effective.

## 🚦 Quick Start

**Your First Feature**:

```
You: /spec Add a user profile feature
Claude: [challenges scope, creates minimal SPEC.md]
You: [Shift-Tab, Shift-Tab to enter Planning Mode]
Claude: [creates detailed plan with todos]
You: [Review and accept the plan]
Claude: [starts implementing automatically]
You: ☕ [coffee break]
```

That's it. Accepting the plan triggers autonomous implementation. Claude handles the heavy lifting while you handle other things.

**What happens next**: Claude implements for hours. You come back to 90-95% complete code. Review, polish, ship.

## 📊 The Three Workflows

### 1. Simple Fix (5 minutes)

```
You: Fix the typo in the login button
Claude: [fixes it directly]
Done.
```

**When to use**: Typos, simple bugs, one-line changes. No planning needed.

### 2. Skip SPEC (When Requirements Are Crystal Clear)

```
You: [Shift-Tab, Shift-Tab] Add user authentication with email/password
Claude: [researches patterns, creates plan with todos]
You: [Accept plan]
Claude: [implements automatically for 30-60 minutes]
You: [take a walk, plan next feature, or sleep]
```

**When to use**: Requirements are already well-defined and boundaries are clear.

### 3. Full Feature (Recommended Default)

```
You: /spec Build a subscription system
Claude: [aggressively reduces scope, creates minimal SPEC.md]
You: [Shift-Tab, Shift-Tab to enter Planning Mode]
Claude: [creates comprehensive plan based on SPEC]
You: [Accept plan]
Claude: [implements autonomously for hours]
You: [work on other projects]
```

**When to use**: New features, complex changes, or when you want clear boundaries. The /spec phase saves hours by clarifying edge cases upfront.

## 🛠️ How to Set This Up

**Four simple steps:**

### 1. Copy the Claude configuration from this repo

```bash
# Copy all commands
cp -r .claude/commands /path/to/your/project/.claude/

# Copy all hooks
cp -r .claude/hooks /path/to/your/project/.claude/

# Copy and adapt settings.json
cp .claude/settings.json /path/to/your/project/.claude/
```

### 2. Adapt CLAUDE.md for your project

Base your CLAUDE.md on the one in this repo. Key sections to customize:

- Quality gates for your language (test, lint, compile commands)
- Pattern examples from your project structure
- Project-specific conventions and rules
- File paths and project names

### 3. Run analyze-codebase (Once)

```bash
/analyze-codebase
```

This generates comprehensive documentation about your codebase that Claude uses during planning. Run it once when starting with a new project.

### 4. Test with a small feature

Try the workflow with something simple first to ensure everything is configured correctly.

✅ **That's it. You're ready for autonomous development.**

## 🎯 Essential Commands & Shortcuts

### Commands You'll Actually Use

**Every Feature**:

- **`/spec`** - Create minimal specs by aggressively challenging scope and defining boundaries. Critical for non-trivial features.
- **`Shift-Tab, Shift-Tab`** - Enter Planning Mode. Claude researches patterns and creates implementation plan.
- **Accept Plan** - Triggers automatic implementation. No further commands needed.

**Once Per Project**:

- **`/analyze-codebase`** - Creates comprehensive docs about your codebase. Run once when starting, update after major architectural changes.

**Emergency**:

- **`/refresh-claude`** - If Claude acts weird. Reinforces the rules.

## 💡 What to Do While Claude Works

This is where the magic happens. Claude's autonomous execution time is YOUR time.

### Take a Break

- ☕ Coffee break
- 🚶 Go for a walk
- 🏃 Hit the gym
- 😴 Take a nap
- 🛌 Go to sleep (seriously - the overnight pattern is real)

### Work on Other Features

**Same repo? Use git worktrees:**

```bash
# Terminal 1: Claude implements feature A here
/path/to/project (feature/auth)

# Terminal 2: You plan feature B here
git worktree add ../project-feature2 -b feature/profiles
cd ../project-feature2
# Run /spec for the next feature while Claude builds the first
```

### The Multiplication Effect

```
9 AM:  /spec feature A → Planning Mode → Accept → ☕
10 AM: /spec feature B → Planning Mode → Accept → 🚶
11 AM: /spec feature C → Planning Mode → Accept → 📧
12 PM: Review all 3 features → Minor tweaks → 🍕

Result: 3 features built in a morning
```

Your productivity multiplies because thinking (specs/planning) and doing (implementation) happen in parallel.

## 🌙 The Overnight Pattern

The ultimate productivity hack:

```
10 PM: /spec Build complete user management system
       [review and refine SPEC.md]
       [Shift-Tab, Shift-Tab]
       [review plan, ensure it's comprehensive]
       [Accept plan]
       😴 [go to bed]

7 AM:  ☕ [check results]
       Review the implementation
       ✅ Feature complete
```

**Real results**: Wake up to features that are 90-95% complete with tests. Review in the morning, run a quick polish cycle if needed. The key is that the heavy lifting is done while you slept.

## 💪 Pro Tips

### The Critical Importance of /spec

**Don't skip /spec for non-trivial features.** Here's why:

- It forces you to define boundaries clearly
- Edge cases get identified before implementation starts
- Ambiguity is eliminated (ambiguity = failed implementation)
- The 30 minutes here saves hours of frustration later

**From experience**: Features with proper /spec succeed. Features without it drift and require multiple rounds of fixes. The choice is yours.

### Trust the Process

Once you accept a plan, **walk away**. The system handles the implementation:

- Quality gates catch errors
- Patterns ensure consistency
- Hooks maintain context
- CLAUDE.md rules are followed

**What to expect**: 90-95% completion. You'll review, make adjustments, maybe run another quick cycle. Still faster than doing it all yourself.

### Setting Realistic Expectations

- Claude gets you 90-95% there autonomously
- You review and polish the final 5-10%
- Often needs 1-2 quick additional cycles for perfection
- Still 3-5x faster than doing it all yourself
- The better your spec/plan, the less cleanup needed

### Plan Multiple Features at Once

```
Morning: Create 3 SPECs
Afternoon: Review and launch all 3 plans
Evening: All 3 features implemented
Next day: Review, test, and ship
```

### The Mindset Shift

**From**: "I need to watch every step"  
**To**: "I'll define what I want clearly, then check the results"

The hardest part is trusting the process. But the hooks, quality gates, and CLAUDE.md ensure good outcomes even without supervision.

## 🔍 How It Really Works

### The Simplified Flow

1. **CLAUDE.md** - Auto-loaded, contains all implementation rules
2. **Hooks** - Enforce reading directives in todos automatically
3. **/analyze-codebase docs** - Provide deep context during planning
4. **Planning Mode** - Native to Claude Code, creates comprehensive plans
5. **Auto-implementation** - Accepting plan triggers autonomous execution

### Why /spec Matters

When you run `/spec`:

- Requirements get challenged and reduced to essentials
- Boundaries become crystal clear
- Edge cases are identified upfront
- Ambiguity is eliminated before planning

This clarity propagates through planning into implementation, resulting in focused, correct features.

### The Planning Mode Advantage

Native Planning Mode (Shift-Tab, Shift-Tab):

- Integrates seamlessly with Claude Code
- Automatically reads SPEC.md if present
- Creates todos with built-in directives
- Triggers implementation on acceptance
- No manual todo creation needed

### How Context Is Maintained

Behind the scenes, the system ensures nothing gets forgotten:

- Documentation is read when needed
- Project rules are consistently followed
- Context persists even during long sessions
- Quality gates run automatically
- Everything just works without configuration

### Why Autonomous Implementation Works

1. **Clear Requirements** - /spec eliminates ambiguity
2. **Pattern-Based** - Claude copies existing successful code
3. **Quality Gates** - Automated checks after each unit
4. **Persistent Todos** - Survive context switches
5. **Enforced Directives** - Hooks ensure nothing is forgotten
6. **CLAUDE.md Rules** - Always loaded, always followed

## 🎨 Choosing Your Workflow Depth

### Minimal (for trivial tasks)

```
You: Fix the typo in the error message
Claude: [fixes directly]
Done in 2 minutes.
```

### Standard (clear requirements)

```
You: [Shift-Tab, Shift-Tab] Add rate limiting to API endpoints
Claude: [plans and implements]
Done in 30 minutes.
```

### Full (recommended default)

```
You: /spec → review → Planning Mode → Accept
Requirements first, then autonomous implementation.
```

**The rule**: When in doubt, use /spec. 10 minutes defining boundaries saves hours of implementation drift.

## 📚 Understanding /analyze-codebase

**Run this once when starting with the workflow on a new codebase.**

What it does:

- Maps your entire codebase architecture
- Documents patterns and conventions
- Identifies key integration points
- Creates detailed reference documentation in `docs/codebase/`

Why it matters:

- Claude uses these docs during planning for better pattern matching
- Architecture is understood holistically
- Integration points are documented
- Results in more accurate implementation

When to run it:

- Once when first setting up the workflow
- After major architectural changes
- When adding significant new patterns or frameworks

## 🚨 When Things Go Wrong

### Claude Seems Confused

```bash
/refresh-claude
```

This reloads CLAUDE.md and reinforces all rules.

### Need to Adjust Mid-Implementation

- Claude handles most issues autonomously
- For major pivots, you can intervene
- Minor adjustments happen naturally through the process

### Want to Resume Later?

The persistent todo system means work can continue anytime. All context is preserved.

## 🎉 Summary

**The workflow**: Define clearly → Plan thoroughly → Accept → Walk away → Review & polish

**Choose your depth**:

- 🔧 Trivial? Just ask directly
- 📋 Clear requirements? Planning Mode → Accept
- 🎯 New feature? `/spec` → Planning Mode → Accept (recommended)

**Prerequisites**:

- ✅ Run `/analyze-codebase` once (if new to the codebase)
- ✅ Have a complete CLAUDE.md
- ✅ Invest the hour upfront (30 min spec + 30 min planning)

**The reality**: You'll get 90-95% completed features. A quick review and polish gets you to 100%. Still 3-5x faster than doing it all yourself.

**The key to success**: Don't rush the spec and planning phases. The clearer your requirements, the better the autonomous implementation. Skip this, and you'll spend more time on back-and-forth fixes than you saved.

Start with a small feature to build confidence. Once you experience waking up to working code (even if it needs a bit of polish), you'll never go back to the old way.

## 🏃 Quick Reference

```
SETUP (once per project):
├── Copy .claude/commands, hooks, settings.json
├── Adapt CLAUDE.md for your stack
└── Run /analyze-codebase

DAILY WORKFLOW:
├── Trivial fix?         → Just ask directly
├── Clear task?          → Shift-Tab × 2 → Accept
└── New feature?         → /spec → Shift-Tab × 2 → Accept

THEN GO DO SOMETHING ELSE:
├── ☕ Coffee break
├── 🚶 Take a walk
├── 💻 Work on another feature (git worktrees)
├── 😴 Go to sleep (seriously)
└── 🏃 Hit the gym

PRODUCTIVITY MULTIPLIERS:
├── Overnight: Start at 10 PM → Wake to working code
├── Parallel: Plan feature B while A builds
└── Batching: Plan 3 features → Execute all → Ship
```

**Remember**: The best code is written while you're not watching. Define what you want clearly, then go live your life. ✨
