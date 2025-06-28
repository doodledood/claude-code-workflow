# Claude Code Development Workflow

A practical guide to autonomous development where Claude implements while you sleep, plan, or drink coffee.

## How to Set This Up

**Two simple steps:**

1. **Create your CLAUDE.md** - Base it on the one in this repo, adapt for your project

   - Replace quality gates with your language's commands (test, lint, compile)
   - Update pattern examples to match your project structure
   - Add your project-specific conventions and rules
   - This is what enables autonomous implementation in YOUR stack

2. **Copy commands** - Copy `.claude/commands/` to your project

That's it. You're ready to go.

## Quick Start

**The Big Idea**: Describe what you want → Claude plans it → You approve → Claude builds it → You do other things.

**Your First Feature**:

```
You: /spec Add a user profile feature
Claude: [challenges scope, creates minimal SPEC.md]
You: /plan
Claude: [creates a plan in PLAN.md]
You: /create-todos
Claude: [transforms plan into persistent todos]
You: /act
Claude: [implements everything with tests]
You: ☕ [coffee break]
```

That's it. Claude handles the implementation while you handle... anything else.

**The key mindset**: Once you start `/act`, walk away. Don't babysit. The quality gates and validation ensure good results even if progress looks messy initially. This only works if you invested in clear requirements upfront.

**Pro tip**: Happy with the output? Just run the next command. Need changes? Say what to fix and Claude will iterate.

## The Three Workflows

### 1. Simple Fix (5 minutes)

```
You: /act Fix the typo in the login button
Claude: [fixes it directly]
Done.
```

**When to use**: Typos, simple bugs, one-line changes

### 2. Skip SPEC (When Requirements Are Crystal Clear)

```
You: /plan Add user authentication
Claude: [researches, creates PLAN.md with 3-5 units]
You: /create-todos
Claude: [transforms plan into persistent todos]
You: /act
Claude: [builds for 30-60 minutes]
You: [take a walk, plan next feature, or sleep]
```

**When to use**: Requirements are already well-defined

### 3. Full Feature (Recommended for New Features)

```
You: /spec Build a subscription system
Claude: [creates SPEC.md with minimal requirements]
You: /plan
Claude: [creates detailed PLAN.md]
You: /create-todos
Claude: [creates todos in system]
You: /act
Claude: [builds for hours]
You: [work on other projects]
```

**When to use**: New features, ensuring clear requirements upfront

## Essential Commands

### First Time Setup

- **`/analyze-codebase`** - Run once when starting a new project. Creates comprehensive docs that make planning and implementation much smoother. Optional but highly recommended (especially for big/established codebases) - it helps Claude understand patterns, architecture, and conventions better.

### Before Planning (Optional)

- **`/prime-context`** - When you already know exactly which files are relevant
  ```
  /prime-context Look at user.service.ts and auth.controller.ts
  ```
  **Pro tip**: Add "ultrathink" after Claude reads the files - triggers deeper analysis for better planning

### Workflow Commands

- **`/spec`** - Create minimal specs by aggressively challenging and deleting features. Outputs SPEC.md.
- **`/plan`** - Research patterns and create implementation plan. Outputs PLAN.md.
- **`/create-todos`** - Transform plan into persistent todos in the system.
- **`/act`** - Execute implementation until complete. The workhorse command.

**Choose your depth**: `/act` for simple tasks, `/plan` → `/create-todos` → `/act` for normal features, full workflow for complex ones.

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
10 PM: /prime-context auth and user files
       /plan Build complete user management
       [review PLAN.md]
       /create-todos
       [verify todos look good]
       /act
       😴 [go to bed]

7 AM:  ☕ [check results]
       /act Add password reset to the email
       ✅ Feature complete
```

**Real results**: Wake up to 80-90% completed features. Just review and refine.

## Pro Tips

### Choose the Right Model

- **Planning & SPECs**: Use Opus 4 - Better at complex reasoning and scope reduction
- **Implementation**: Use Sonnet 4 - Faster and perfect for coding with patterns

This combination gives you the best of both worlds: thoughtful planning and efficient execution.

### The Iteration Pattern

- Happy with SPEC/Plan/Todos? Just run the next command
- Need changes? Say what to fix and Claude will update
- No need to say "approved" - moving forward is approval
- This keeps the workflow flowing smoothly

### Plan Multiple Features at Once

```
Morning: Create 3 SPECs
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

### Don't Babysit - Change Your Mindset

**The hardest part**: Resisting the urge to watch and micromanage.

- **Trust the gates**: Even if progress looks messy initially, the quality gates and validation layers ensure a good outcome
- **Do something else**: The whole point is parallel productivity - go work on another feature, take a break, or sleep
- **Let it fail forward**: Blockers get handled, errors get fixed, the process continues
- **Caveat**: This only works if you did requirements and planning well - garbage in, garbage out

**The mindset shift**: From "I need to watch every step" to "I'll check the results later". The process is designed to reach a satisfactory result without your intervention.

**Remember**: It won't be perfect, and that's OK. The goal is to maximize your time efficiency, not achieve perfection. You'll polish the rough edges later.

### Trust the Process

- Quality gates prevent bad code
- Tests are mandatory
- Patterns ensure consistency
- You can always review and adjust

### The 80/20 Rule (Accept Imperfection)

**Critical understanding**: The goal is NOT 100% perfection. The goal is maximizing your output per time invested.

- Claude gets you 80-90% there
- You refine the last 10-20%
- Still 5x faster than doing it all yourself
- **Accept this trade-off**: Less perfect but far more productive

**The math**: Would you rather have 1 perfect feature or 5 features at 85% that you can polish? The choice is clear.

## How It Really Works (Deep Dive)

_Optional reading - you don't need this to be productive, but it helps to understand why it works._

**The Ultimate Goal**: Enable complete automation after planning is done correctly. Once you approve the todos, Claude should be able to implement everything while you sleep, handle any issues that arise, and deliver a working feature by morning.

**Language Agnostic**: While examples use TypeScript/NestJS, this workflow works for ANY language or framework. Just adapt:

- Pattern searching (grep for your language's constructs)
- Quality gates (your test/lint/compile commands)
- File patterns (your project's structure)
- CLAUDE.md (your project's specific rules and standards)

### The SPEC Phase (Deletion First)

When you run `/spec`:

1. **Requirements Extraction** - Claude becomes a minimalist product manager

   - **Why**: Clear WHAT before HOW. AI needs testable requirements, not business cases
   - **Focus**: Specific capabilities with acceptance criteria
   - **Skip**: ROI, market analysis, user personas, business metrics
   - **Result**: Minimal SPEC with ruthless scope reduction

2. **Testable Criteria** - Every requirement gets a verification method

   - **Why**: Ambiguity kills automation. "Fast" means nothing, "< 200ms" is testable
   - **Example**: "User can upload avatar" → "POST /profile/photo returns 200 and stores file"
   - **Benefit**: Implementation knows exactly when it's done

3. **SPEC.md Creation** - Temporary workspace file

   - **Why**: Review and modify requirements before planning
   - **Format**: Problem context (1-2 sentences), requirements list, out of scope
   - **Lifespan**: Created by `/spec`, consumed by `/plan`, then obsolete
   - **Note**: This file is gitignored - it's just a workflow artifact

4. **Agent Validation** - Automated quality check
   - **Why**: Catch vague requirements before they propagate
   - **Checks**: Clarity, testability, scope boundaries, minimalism
   - **Result**: SPEC ready for planning without ambiguity

**The SPEC insight**: By aggressively deleting features and forcing requirements into testable form upfront, the entire downstream process becomes deterministic. No guessing during implementation.

### The Planning Phase

When you run `/plan`:

1. **Requirements Input** - Claude reads SPEC.md (or gets requirements from you)

   - **Why**: Plans need clear requirements as foundation
   - **Source priority**: SPEC.md → User input → Suggest creating SPEC first
   - **Focus**: Transform WHAT (requirements) into HOW (implementation units)
   - **Result**: Concrete plan based on testable criteria

2. **Pattern Discovery** - Claude finds similar code using grep

   - **Why**: Consistency is king. Every service should look like every other service
   - **How**: Searches for 2-3 examples, reads ENTIRE files (not just grep results)
   - **Deep dive**: Understands WHY patterns work, not just copying blindly
   - **Result**: Specific file:line references for every pattern

3. **Unit Design** - Breaks work into atomic pieces (ALWAYS with tests)

   - **Why**: Small units = small risks. Problems caught early are easy to fix
   - **Atomic means**: Can be completed in one session, tested independently
   - **Never separate**: Implementation and tests are ONE unit (incomplete without tests)
   - **Right-sized**: Not "add import" but not "entire system" either

4. **PLAN.md Creation** - Another temporary workspace file

   - **Why**: Review and modify plan before creating todos
   - **Format**: Structured markdown with units, patterns with line numbers, gates
   - **Lifespan**: Created by `/plan`, consumed by `/create-todos`, then obsolete
   - **Important**: Like SPEC.md, this is just a workflow artifact

5. **Agent Validation** - Automated plan review
   - **Why**: Ensures units are truly atomic and patterns are specific
   - **Checks**: Unit independence, pattern clarity, test inclusion, completeness
   - **Updates**: Plan improved before presenting to you

Each unit is self-contained and includes:

- Implementation (what to build)
- Tests (proof it works)
- Pattern references (e.g., "copy auth.service.ts:15-89")
- Quality gates (how to verify)

**The planning insight**: PLAN.md exists only to be transformed into todos. Once `/create-todos` runs, modifying PLAN.md is meaningless - the todos are what drive implementation, not the plan file.

### The Todo System (The Real Execution Driver)

When you run `/create-todos`:

Claude transforms your PLAN.md into **THE persistent execution memory** that drives everything:

```
"Unit 1.1: Create UserService [ReadClaude,ReadTestDocs] -
Create src/users/user.service.ts copying auth.service.ts:15-89 structure -
Inject UserRepository - Implement: create(dto) with validation,
findOne(id) with NotFoundException if not found, findAll() with pagination -
Error handling from policy.service.ts:45-89 -
Tests: Copy auth.service.test.ts:234-289, mock UserRepository with createMock -
Gates: Run in parallel: tsc, test --testFile=user.service.test.ts, lint"
```

**Critical understanding: Todos are THE execution driver, not PLAN.md**

1. **Complete Self-Containment** - Each todo has EVERYTHING needed

   - **Pattern files**: With exact line numbers (auth.service.ts:15-89)
   - **Implementation steps**: Detailed enough for zero ambiguity
   - **Test requirements**: Embedded in the same todo (never separate)
   - **Quality gates**: Exact commands to run in parallel
   - **Result**: Could hand this todo to another developer and they'd succeed

2. **Reading Hints System** - Context loading instructions

   - `[ReadClaude,ReadTestDocs]` - Read CLAUDE.md + testing docs before starting
   - `[ReadClaude,ReadArchDocs]` - Read CLAUDE.md + architecture docs
   - `[ReadClaude,ReadDataDocs]` - Read CLAUDE.md + data domain docs
   - `[SkipClaude,SkipDocs]` - ONLY for trivial fixes (imports, typos)
   - **Why**: Ensures correct behavior even after context compaction

3. **TodoWrite Tool** - Creates persistent system todos

   - **Not file-based**: Uses TodoWrite tool to create in-memory todos
   - **Survives compaction**: TodoRead restores them after context loss
   - **Status tracking**: pending → in_progress → completed
   - **One at a time**: Only ONE todo in_progress ever

4. **Final Verification Todo** - ALWAYS the last todo

   ```
   "Final Verification: Comprehensive Agent Review [ReadClaude,SkipDocs] -
   Use Agent tool to verify ALL implementation complete -
   Check against SPEC.md if exists - Verify code quality and patterns -
   Confirm all quality gates pass - Verify meaningful test coverage -
   Fix any issues found - Gates: Agent verification must pass"
   ```

**The todo insight**: Once todos are created, PLAN.md becomes irrelevant. The todos contain everything needed for implementation. They ARE the plan, the guide, and the checklist all in one.

### The Execution Phase

When you run `/act`:

Claude becomes an unstoppable implementation machine with a specific workflow:

1. **TodoRead FIRST** - Always starts by reading todos from system

   - **Why**: Todos are the persistent memory, not files
   - **Always**: Even if you think you know what to do
   - **Result**: Current task list with status of each todo

2. **Reading Hints Execution** - Follows todo's context loading instructions

   **When todo says `[ReadClaude,...]`**:

   - Reads the FULL CLAUDE.md file (not sections)
   - Acknowledges: "I've refreshed my memory of CLAUDE.md and will follow it to the letter"
   - Adds system reminder: `<system-reminder>I must adhere to CLAUDE.md guidelines very closely.</system-reminder>`
   - **Critical**: This happens for EVERY non-trivial todo

   **Documentation hints**:

   - `ReadArchDocs` → Reads architecture docs before implementing
   - `ReadTestDocs` → Reads testing docs before writing tests
   - `ReadDataDocs` → Reads data domain docs for database work
   - **Liberal reading**: When in doubt, read the docs - 5 minutes reading saves hours debugging

3. **Pattern-First Implementation** - Never writes code without patterns

   - **Reads ENTIRE pattern files**: Not just the lines mentioned
   - **Understands context**: Why the pattern works, not just syntax
   - **Copies exactly**: Structure, error handling, test patterns
   - **Adapts only**: Names, types, specific business logic

4. **Quality Gates After EVERY Unit** - Run in parallel, non-negotiable

   ```bash
   # All three must pass before marking complete:
   npx nx run <project>:tsc                    # TypeScript
   npx nx test <project> --testFile=<file>     # Tests
   npx nx lint <project> --fix                 # Linting
   ```

   - **Parallel execution**: Three separate tool calls at once
   - **Wait for ALL results**: Don't proceed until all pass
   - **Zero tolerance**: One failure = unit not complete

5. **Blocker Handling** - Nuanced decisions maintain progress

   **Can continue in unit?**

   - Create: `"Unit 1.1b: Fix missing UserDto type [ReadClaude,SkipDocs] - Create in src/types..."`
   - Keep working on current unit

   **Totally blocked?**

   - Create blocker todo with full context
   - Mark current todo as pending
   - Move to next unit

   **Optional doc reading**: When blocked, often reading relevant docs unblocks immediately

6. **Final Agent Verification** - MANDATORY completion step

   - **Runs after all todos done**: Not optional
   - **Comprehensive review**: All changes, all requirements
   - **Creates fix todos**: If issues found, goes through same workflow
   - **Implementation incomplete**: Until Agent verification passes

**The execution insight**: Implementation is deterministic because todos contain everything needed. No decisions during execution, just following the blueprint. This is why you can literally sleep while it works.

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

### Context Compaction & CLAUDE.md (The Hidden Continuity)

Here's a critical insight about long implementation sessions:

1. **What Happens During Implementation**

   - Claude starts with `/act` command loaded
   - Implements todo after todo, context fills up
   - Eventually triggers automatic compaction
   - **Problem**: Claude forgets command contents (including act.md)
   - **But**: Claude Code doesn't auto-trigger commands after compaction

2. **The CLAUDE.md Redundancy** - Intentional design for continuity

   - **act.md**: Contains full implementation workflow (loaded by /act)
   - **CLAUDE.md**: Contains similar implementation rules (auto-loaded)
   - **Why redundant?**: When compaction happens, CLAUDE.md is automatically reloaded
   - **Result**: Implementation rules persist even when command memory is lost

3. **Post-Compaction Recovery** - Seamless continuation

   ```
   After compaction:
   - TodoRead restores task list (what to do)
   - CLAUDE.md restores rules (how to do it)
   - Implementation continues without missing a beat
   ```

4. **Why This Design Works**

   - **No manual intervention**: You don't need to re-run /act
   - **Consistent behavior**: Same rules before and after compaction
   - **Uninterrupted progress**: Claude keeps implementing while you sleep
   - **Self-reinforcing**: Reading Hints ensure CLAUDE.md is read for each todo

**The compaction insight**: The "redundancy" between act.md and CLAUDE.md isn't redundancy at all - it's a failsafe ensuring autonomous operation survives context loss. This is why you can start a feature at night and wake up to it completed.

### Why This All Works

**The entire process is designed for maximal automation without deviations.**

1. **File-Based Workflow Enables Control**

   - SPEC.md → Review requirements before planning
   - PLAN.md → Review plan before creating todos
   - Each step outputs a file you can modify
   - **Result**: Full control while maintaining automation

2. **Separation of Concerns**

   - Planning (thinking) is separate from execution (doing)
   - You focus on design, Claude focuses on implementation
   - **Result**: Execution becomes mechanical, predictable, and autonomous

3. **Atomic Units Reduce Risk**

   - Small changes = small potential for bugs
   - Quick feedback loops catch issues early
   - Tests included in every unit ensure quality
   - **Result**: Claude can handle blockers without stopping entirely

4. **Patterns Ensure Quality**

   - No reinventing wheels or creative coding
   - Leveraging existing, tested solutions
   - Specific line numbers eliminate ambiguity
   - **Result**: No design decisions during execution = no deviations

5. **Multiple Validation Layers**

   - Agent validates SPEC for clarity and scope reduction
   - Agent validates plan for atomicity
   - Quality gates validate each unit
   - Final Agent verification validates completeness
   - **Result**: Automated quality control without human oversight

6. **Todos as Persistent Memory**

   - Survive context switches and compaction
   - Self-contained with all implementation details
   - Reading Hints ensure correct context loading
   - **Result**: Work continues despite any interruption

7. **CLAUDE.md Redundancy Ensures Continuity**

   - Auto-loaded after every compaction
   - Reinforces implementation rules without manual intervention
   - Combines with TodoRead for complete context restoration
   - **Result**: True "fire and forget" development

**The key insight**: By front-loading all decisions into planning and using existing patterns for everything, execution becomes a deterministic process. Claude doesn't need to make judgment calls - it just follows the blueprint. Add the CLAUDE.md failsafe for context loss, and you have a system that can run autonomously for hours. This is why you can literally sleep while it works.

## Choosing Your Workflow Depth

The beauty of the new system? **You choose how deep to go:**

### Minimal (for clear tasks)

```
You: /act Add rate limiting to API
Done in 20 minutes.
```

**When to use**: You know exactly what needs to be done, it's straightforward.

### Standard (when requirements are clear)

```
You: /plan → review → /create-todos → /act
Skip SPEC when requirements are already minimal and clear.
```

**When to use**: Requirements are already well-defined, no ambiguity.

### Full (recommended default)

```
You: /spec → /plan → /create-todos → /act
Requirements first, then plan, then execute.
```

**When to use**: Default for new features. Clear requirements = better implementation.

**Pro tips**:

- Start with `/spec` by default - aggressive scope reduction saves time later
- Skip to `/plan` only when requirements are crystal clear
- Use `/act` directly for fixes and simple changes
- Remember: 5 minutes writing requirements saves hours of rework

The commands are designed to chain naturally - each one's output feeds the next.

## File Lifecycle & Persistence

Understanding which files are temporary vs persistent is crucial:

### Temporary Workflow Files (Gitignored)

1. **SPEC.md** - Created by `/spec`

   - Purpose: Define testable requirements
   - Consumed by: `/plan`
   - Lifespan: Obsolete after planning starts
   - Location: Repository root

2. **PLAN.md** - Created by `/plan`
   - Purpose: Break down into implementation units
   - Consumed by: `/create-todos`
   - Lifespan: Obsolete after todos created
   - Location: Repository root

**Important**: These files exist only for review/modification between steps. Once consumed, they serve no purpose.

### Persistent System Memory

3. **Todos** - Created by `/create-todos`

   - Purpose: Drive entire implementation
   - Storage: In-memory via TodoWrite/TodoRead
   - Lifespan: Until marked completed
   - Survives: Context switches, compaction, restarts

4. **CLAUDE.md** - Created by you
   - Purpose: Implementation rules and patterns
   - Auto-loaded: After every compaction
   - Lifespan: Permanent (checked into repo)
   - Critical: Ensures continuity when context lost

**The lifecycle insight**: Files flow from temporary (SPEC → PLAN) to persistent (Todos + CLAUDE.md). This design enables both human control (file review) and autonomous execution (persistent memory).

## When Things Go Wrong

### Claude Seems Confused

1. Try `/refresh-claude` first
2. Use `/prime-context` with the right files
3. Restart with a clearer command

### Task Unclear During Implementation?

- If during `/act`: Stop and run `/spec` to clarify and reduce requirements
- If plan too vague: Re-run `/plan` with more specific guidance
- If todos missing context: Re-run `/create-todos` with feedback

**Example**:

```
You: /act Add user profiles
Claude: [struggling with unclear requirements]
You: "Stop. Let's clarify first"
You: /spec User profile system with avatar upload and bio
```

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

## Summary

**Basic workflow**: `/plan [task]` → `/create-todos` → `/act` → Walk away

**Choose your depth**:

- Simple fix? Just `/act Fix the login bug`
- Very clear requirements? `/plan Add user auth` → `/create-todos` → `/act`
- New feature? `/spec User profiles` → `/plan` → `/create-todos` → `/act` (recommended default)

**Key insight**: Separate thinking (planning) from doing (execution)

**Result**: Get 3-5x more done by working in parallel with Claude

Start with simple tasks to build confidence. Within a day, you'll be planning features before bed and waking up to working code.

It's not magic, but it's close.
