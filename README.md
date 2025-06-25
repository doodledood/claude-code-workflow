# Claude Code Development Workflow

A practical guide to autonomous development where Claude implements while you sleep, plan, or drink coffee.

## How to Set This Up

**Two simple steps:**

1. **Create your CLAUDE.md** - Base it on the one in this repo, adapt for your project
2. **Copy commands** - Copy `.claude/commands/` to your project

That's it. You're ready to go.

## Quick Start

**The Big Idea**: Describe what you want → Claude plans it → You approve → Claude builds it → You do other things.

**Your First Feature**:

```
You: "Add a user profile feature" + Shift+Tab, Shift+Tab
Claude: [creates a plan]
You: "Looks good"
Claude: [implements everything with tests]
You: ☕ [coffee break]
```

That's it. Claude handles the implementation while you handle... anything else.

## The Three Workflows

### 1. Simple Fix (5 minutes)

```
You: "Fix the typo in the login button"
Claude: [fixes it]
Done.
```

**When to use**: Typos, simple bugs, one-line changes

### 2. Normal Feature (Recommended Default)

```
You: "Add user authentication"
You: Shift+Tab, Shift+Tab         [enter plan mode]
Claude: [researches, plans with 3-5 units]
You: "Ship it"                    [approve]
Claude: [builds for 30-60 minutes]
You: [take a walk, plan next feature, or sleep]
```

**When to use**: Most development tasks

### 3. Complex Feature

```
You: "/prd Build a subscription system"
Claude: [creates requirements doc]
You: "Approved" + Shift+Tab, Shift+Tab
Claude: [creates detailed plan]
You: "Go ahead"
Claude: [builds for hours]
You: [work on other projects]
```

**When to use**: Unclear requirements, multi-component features

## Essential Commands

### First Time Setup

- **`/analyze-codebase`** - Run once when starting. Creates docs Claude uses for planning.

### Before Planning (Optional)

- **`/prime-context`** - When you already know exactly which files are relevant
  ```
  /prime-context Look at user.service.ts and auth.controller.ts
  ```
  **Pro tip**: Add "ultrathink" after Claude reads the files - triggers deeper analysis for better planning

### Planning

- **`Shift+Tab, Shift+Tab`** - Enter plan mode. Claude researches and creates a plan.
- **`/prd`** - For complex features. Creates a requirements doc first.

### Emergency

- **`/refresh-claude`** - If Claude acts weird. Reinforces the rules.

## What to Do While Claude Works

This is where the magic happens. Claude's execution time is YOUR time.

### Take a Break

- ☕ Coffee break
- 🚶 Go for a walk
- 😴 Take a nap
- 🛌 Go to sleep (seriously)

### Work on Other Features

**Same repo? Use git worktrees:**

```bash
# Terminal 1: Claude works here
/path/to/project (feature/auth)

# Terminal 2: You plan the next feature here
git worktree add ../project-feature2 -b feature/profiles
cd ../project-feature2
```

Now you can plan feature 2 while Claude builds feature 1!

### The Multiplication Effect

```
9 AM:  Plan feature A (20 min) → Start Claude → ☕
10 AM: Plan feature B (20 min) → Start Claude → 🚶
11 AM: Plan feature C (20 min) → Start Claude → 📧
12 PM: Review all 3 features → Tweak → 🍕

Result: 3 features built in a morning
```

Your productivity multiplies because thinking (planning) and doing (execution) happen in parallel.

## The Overnight Pattern

The ultimate productivity hack:

```
10 PM: "/prime-context auth and user files"
       "Build complete user management" + Shift+Tab, Shift+Tab
       [review plan]
       "Approved"
       😴 [go to bed]

7 AM:  ☕ [check results]
       "Add password reset to the email"
       [small refinement]
       ✅ Feature complete
```

**Real results**: Wake up to 80-90% completed features. Just review and refine.

## How It Really Works (Deep Dive)

_Optional reading - you don't need this to be productive, but it helps to understand why it works._

### The Planning Phase

When you hit Shift+Tab, Shift+Tab:

1. **Pattern Discovery** - Claude finds similar code using grep

   - **Why**: Consistency is king. Every service should look like every other service
   - **How**: Searches for 2-3 examples, reads entire files (not just grep results)
   - **Result**: Deep understanding of existing patterns

2. **Unit Design** - Breaks work into atomic pieces (always with tests)

   - **Why**: Small units = small risks. Problems caught early are easy to fix
   - **Atomic means**: Can be completed in one session, tested independently
   - **Never separate**: Implementation and tests are ONE unit (incomplete without tests)

3. **Validation** - Checks the plan follows all rules
   - **Why**: Catches design flaws before they become code problems
   - **Uses Agent tool**: Verifies units are truly independent
   - **Fixes issues**: Before presenting plan to you

Each unit is self-contained and includes:

- Implementation (what to build)
- Tests (proof it works)
- Pattern references (e.g., "copy auth.service.ts:15-89")
- Quality gates (how to verify)

### The Todo System

Claude creates "todos" that survive context switches:

```
"Unit 1.1: Create UserService [ReadClaude,ReadTestDocs] -
Create src/users/user.service.ts copying auth.service.ts:15-89 structure -
Implement CRUD methods - Tests: Copy auth.service.test.ts:234-289 patterns -
Gates: Run in parallel: tsc, test --testFile=user.service.test.ts, lint"
```

**Why todos are critical:**

- **Context windows fill up** - Todos survive when memory doesn't
- **Interruptions happen** - Resume exactly where you left off
- **Self-contained** - Another developer (or future Claude) could implement from todo alone

**Reading Hints explained:**

- `[ReadClaude,ReadTestDocs]` - Forces re-reading rules and test patterns
- `[SkipClaude,SkipDocs]` - Only for trivial fixes like missing imports
- **Why**: Ensures consistent behavior even after context resets

### Quality Gates

After each unit, three checks run automatically:

```bash
npx nx run <project>:tsc          # TypeScript compilation
npx nx test <project> --testFile= # Unit tests
npx nx lint <project> --fix       # Code style
```

**Why non-negotiable:**

- **Compound errors are exponential** - One bad unit breaks the next
- **Small, frequent checks** - Easier to fix than accumulated problems
- **Parallel execution** - All three run simultaneously for speed

**What happens on failure:**

1. Simple fix? Do it now
2. Complex? Create blocker todo
3. Can't continue? Mark pending, move to next unit
4. **Always maintain forward progress**

### Pattern-First Development

Claude never invents code. It finds patterns and copies them:

1. **Searches with grep** - Finds 2-3 similar implementations
2. **Reads entire files** - Understanding context, not just syntax
3. **Copies structure exactly** - Same organization, same patterns
4. **Only adapts specifics** - Names, types, business logic

**Why patterns are crucial:**

- **Less room for error** - If it worked before, it'll work again
- **Proven success** - You're copying what already succeeds in production
- **No guesswork** - Claude doesn't have to figure out "the right way"
- **Consistency** - New code indistinguishable from existing code
- **Compound benefits** - Each pattern reuse strengthens the approach

**The core insight**: Every pattern in your codebase represents a solved problem. By copying these solutions exactly, you inherit their success without their original development cost.

**The goal**: Your codebase should look like one person wrote it all.

### Why This All Works

**The entire process is designed for maximal automation without deviations.**

1. **Separation of Concerns**

   - Planning (thinking) is separate from execution (doing)
   - You focus on design, Claude focuses on implementation
   - **Result**: Execution becomes mechanical, predictable, and autonomous

2. **Atomic Units Reduce Risk**

   - Small changes = small potential for bugs
   - Quick feedback loops catch issues early
   - **Result**: Claude can handle blockers without stopping entirely

3. **Patterns Ensure Quality**

   - No reinventing wheels or creative coding
   - Leveraging existing, tested solutions
   - **Result**: No design decisions during execution = no deviations

4. **Validation Prevents Drift**

   - Agent checks keep plans on track
   - Quality gates ensure code meets standards
   - **Result**: Automated quality control without human oversight

5. **Todos Enable Persistence**
   - Work continues despite interruptions
   - Context loss doesn't mean progress loss
   - **Result**: True "fire and forget" development

**The key insight**: By front-loading all decisions into planning and using existing patterns for everything, execution becomes a deterministic process. Claude doesn't need to make judgment calls - it just follows the blueprint. This is why you can literally sleep while it works.

## When Things Go Wrong

### Claude Seems Confused

1. Try `/refresh-claude` first
2. Exit and re-enter plan mode
3. Use `/prime-context` with the right files

### Claude Hit a Blocker

**Can continue in the same unit?**

- Claude creates a sub-task and keeps going

**Totally blocked?**

- Claude marks current task pending
- Moves to next unit
- Returns to blockers later

The key: Forward progress always continues.

### Need to Resume Later?

No problem. Todos contain everything needed:

- What to build
- Which patterns to copy
- Exact line numbers
- Test requirements

Anyone (including future Claude) can pick up where things left off.

## Pro Tips

### Choose the Right Model

- **Planning & PRDs**: Use Opus 4 - Better at complex reasoning and design
- **Implementation**: Use Sonnet 4 - Faster and perfect for coding with patterns

This combination gives you the best of both worlds: thoughtful planning and efficient execution.

### Plan Multiple Features at Once

```
Morning: Create 3 PRDs
Lunch: Plan all 3 features
Afternoon: Execute all 3 in sequence
Evening: Review and ship
```

### Use Git Worktrees for Parallel Work

```bash
# Set up multiple workspaces
git worktree add ../proj-auth feature/auth
git worktree add ../proj-api feature/api
git worktree add ../proj-ui feature/ui

# Now run Claude in each!
```

### Batch Similar Work

- Plan all API endpoints together
- Plan all UI components together
- Claude reuses patterns more effectively

### Trust the Process

- Quality gates prevent bad code
- Tests are mandatory
- Patterns ensure consistency
- You can always review and adjust

### The 80/20 Rule

- Claude gets you 80-90% there
- You refine the last 10-20%
- Still 5x faster than doing it all yourself

## Summary

**Basic workflow**: Describe → Plan (Shift+Tab, Shift+Tab) → Approve → Walk away

**Key insight**: Separate thinking (planning) from doing (execution)

**Result**: Get 3-5x more done by working in parallel with Claude

Start with simple tasks to build confidence. Within a day, you'll be planning features before bed and waking up to working code.

It's not magic, but it's close.
