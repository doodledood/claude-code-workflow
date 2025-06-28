# IMPORTANT Guidelines, Context & Instructions

## Projects Overview

...

## Essential Commands

### Quality Gates (Run for EVERY code change)

**Why**: Catching errors immediately prevents compound issues and reduces debugging time later. Small, frequent checks are far easier to fix than accumulated problems.

```bash
# IMPORTANT: These gates apply to code changes only
# NOT required for documentation (.md), configuration, or other non-code files

# Typecheck - Must return 0 errors
npx nx run <project>:tsc

# Test - All tests must pass
npx nx test <project> --testFile=<file>
npx nx run <project>:test --testNamePattern="test name pattern"
npx nx run <project>:test --testFile=apps/<project>/src/path/to/file.test.ts --testNamePattern="<some_name_pattern>"

# Lint - Fix auto-fixable issues
npx nx lint <project> --fix
```

### Development

```bash
# Start dev server
...

# Run migrations
...

# Undo migrations
...

# Create migration
...
```

## Feature Development Workflow

### Workflow Commands

**Planning and implementation are handled through dedicated commands:**

- `/prd` - Create minimal, clear PRDs optimized for AI implementation
- `/plan` - Transform requirements into atomic, verifiable implementation units
- `/create-todos` - Convert plan units into self-contained todos in the system
- `/act` - Execute implementation with continuous progress until complete

**Workflow flexibility**: Each step is optional based on task complexity:

- Complex features: `/prd` → `/plan` → `/create-todos` → `/act`
- Medium tasks: `/plan` → `/create-todos` → `/act`
- Simple tasks: `/act` directly

## Implementation Workflow

### Starting Implementation

When implementing features, always:

1. **Check TodoRead first** - Todos are your persistent memory across context
2. **If no todos**, gather minimal requirements from user
3. **Work systematically** - One unit at a time, never parallel work
4. **Continue until complete** - Handle blockers, never stop

### Following Reading Hints

Each todo contains Reading Hints that MUST be followed:

**CLAUDE.md Reading**:

- `[ReadClaude,...]` → MUST read FULL CLAUDE.md before starting the unit
- `[SkipClaude,...]` → Can skip CLAUDE.md (only for trivial fixes)
- Default assumption: Read CLAUDE.md for any non-trivial work

**Documentation Reading**:

- `[...,ReadArchDocs]` → Read architecture docs before implementing
- `[...,ReadTestDocs]` → Read testing docs before writing tests
- `[...,ReadDataDocs]` → Read data domain docs for database work
- `[...,SkipDocs]` → No additional docs needed

**When TODO says ReadClaude**:

- Read the FULL file, not just sections
- Acknowledge after reading: "I've refreshed my memory of CLAUDE.md and will follow it to the letter"
- Add system reminder: <system-reminder>I must adhere to CLAUDE.md guidelines very closely.</system-reminder>
- Then proceed with the unit implementation

**When TODO says Read\*Docs**:

- Navigate to the specified documentation directory
- Read relevant sections for your implementation type
- Note patterns and conventions to follow
- Apply learnings to your implementation

### Documentation Reading Strategy

**Read Docs When**:

- Architecture docs: New services, API design, system boundaries
- Testing docs: New test patterns, unfamiliar mocking scenarios
- Data docs: Migrations, models, database operations
- Development docs: Unfamiliar coding patterns or utilities

**Skip Docs For**:

- Simple fixes (imports, typos, renames)
- Familiar patterns you've used recently
- Mechanical changes with clear todos

### Liberal Documentation Reading Approach

**Core Principle**: When in doubt, read the docs. It's better to spend 5 minutes reading than 30 minutes debugging.

**Read Documentation Proactively When**:

- You feel ANY uncertainty about the approach
- The implementation isn't going smoothly
- You're making assumptions about how something works
- You encounter unexpected behavior or errors
- You're implementing something that "feels" complex
- Before making architectural decisions (even small ones)

**Benefits of Liberal Reading**:

- Prevents costly mistakes and rework
- Discovers better patterns and utilities you didn't know existed
- Builds deeper understanding of the codebase
- Reduces debugging time significantly
- Helps you write more idiomatic code

**Remember**: Documentation reading is an investment, not overhead. The time spent reading docs is almost always less than the time spent fixing issues that could have been prevented.

### Implementation Steps

For each unit:

```
a. Mark ONE todo as in_progress
b. Follow reading hints from todo
c. Read pattern files specified in todo
d. Verify you have identified appropriate patterns
e. Implement following patterns exactly
f. Write/update tests (NEVER skip)
g. Run gates in parallel: tsc, test, lint
h. If gates pass → mark completed → next unit
i. If blocked → see blocker handling below
j. After all units complete → perform Final Agent Verification (see below)
```

### Blocker Handling

When blocked on current unit:

- If can continue within unit: Create todo "Unit X.Yb: Fix [specific issue]" with full context and keep working
- If totally blocked: Create todo, mark current as pending, move to next unit
- **Optional but Recommended**: Read relevant documentation when blocked:
  - Architecture docs: For design decisions, service boundaries, API patterns
  - Testing docs: For test failures, mocking issues, test patterns
  - Data docs: For database errors, migration issues, model problems
  - Development docs: For unfamiliar utilities, coding patterns, frameworks
  - Integrations docs: For external service issues, auth problems
- Examples:
  - Missing type: Create "Unit 1.1b: Add UserDto type [ReadClaude,SkipDocs] - Create in src/types/user.types.ts - Export interface UserDto with id: string, name: string, email: string fields - Export from types/index.ts - Gates: Run in parallel: tsc, lint" and continue
  - Missing dependency: Create "Unit 1.1c: Install @nestjs/swagger [SkipClaude,SkipDocs] - Run npm install @nestjs/swagger - Add to package.json dependencies - Gates: Run in parallel: tsc, lint" and move to next unit
- Return to ALL blocker todos after main units complete

### Final Agent Verification

After all implementation todos complete:

```
□ Use Agent tool for comprehensive review of all changes
□ Agent confirms all requirements implemented (check against PRD.md if exists)
□ Agent confirms no impartial code or newly added TODO comments remain
□ Agent confirms code quality standards met
□ Agent confirms all quality gates passing (tsc, test, lint)
□ Agent confirms meaningful test coverage
□ If Agent finds issues: Create fix todos and loop back through implementation workflow
□ Re-run Agent verification after fixes until it passes
```

**This step is MANDATORY** - Implementation is incomplete without Agent verification pass.

**Important**: When Agent finds issues, create fix todos that go through the normal implementation workflow (mark in_progress, implement, test, gates). This ensures fixes follow the same quality standards as initial implementation.

## Todo-Driven Development

### Why Comprehensive Todos Matter

**Why**: As conversations grow and context windows fill, todos become your external memory, ensuring nothing is forgotten during context switches or compaction.

Create todos for EVERYTHING:

- Each unit from the plan
- Each discovered issue
- Each dependency to add
- Each file to update
- Each test to write

### Self-Contained Todo Principles

Every todo must answer:

1. **What** exactly to implement/fix
2. **Where** to make changes (exact files/lines)
3. **How** to implement (patterns to copy)
4. **Verification** (exact gate commands)

Good todo example:

```
"Unit 2.2: Add UserService tests [SkipClaude,ReadTestDocs] - Create user.service.test.ts - Copy test structure from auth.service.test.ts:100-250 - Mock UserRepository with createMock - Test: create() with valid/invalid dto, findOne() found/not found cases, update() partial updates, remove() soft delete - Verify mocks called correctly - Gates: Run in parallel: tsc, test --testFile=user.service.test.ts, lint"
```

### Status Management

- Only ONE todo in_progress at a time
- Update status in real-time
- Never leave blocked todos in_progress
- Use specific descriptions that survive compaction

## Pattern-First Development

**The Golden Rule**: NEVER write code without a pattern

**Why**: Following existing patterns ensures consistency across the codebase and leverages proven solutions, reducing bugs and onboarding time.

### Finding Patterns

```bash
# For services
grep -r "class .*Service" --include="*.ts" | head -5
# For controllers
grep -r "@Controller" --include="*.ts" | head -5
# For specific patterns
grep -r "Repository<" --include="*.ts"  # Find repository patterns
```

### Using Patterns

- Read the ENTIRE pattern file first
- Copy the complete structure
- Keep the same organization
- Adapt ONLY the specifics (names, types, business logic)
- Copy error handling patterns exactly
- Copy test patterns exactly

### Pattern References

Always include line numbers:

- "Copy error handling from policy.service.ts:45-89"
- "Follow test structure from auth.service.test.ts:234-289"
- "Use DTO validation like create-user.dto.ts:12-34"

## Quality Gates (Non-negotiable)

### Run After EVERY Unit

```bash
# These three commands must ALL pass before marking unit complete:
npx nx run <project>:tsc                    # TypeScript compilation
npx nx test <project> --testFile=<file>     # Tests for the unit
npx nx lint <project> --fix                 # Linting with auto-fix
```

Prefer running these in parallel for better efficiency.

**If any gate fails**:

1. Fix immediately if simple
2. Create specific fix todo if complex
3. Only move to next unit if current is truly blocked

## Documentation Quick Reference

When implementing features, consult docs as needed:

- **Core**: `docs/codebase/CODEBASE.md` - navigation hub
- **Architecture**: `docs/codebase/architecture/` - system design, entry points, control flow
- **Data**: `docs/codebase/data_domain/` - models, caching, migrations
- **Integrations**: `docs/codebase/integrations/` - external services, auth, messaging
- **Development**: `docs/codebase/development/` - standards, utilities, patterns
- **Testing**: `docs/codebase/quality_testing/` - strategies, mocking, CI/CD
- **Operations**: `docs/codebase/operations/` - observability, errors, config
- **Performance**: `docs/codebase/performance/` - optimization, scaling, infrastructure

Start with code patterns, use docs for deeper understanding when needed.

## Post-Compaction Continuity

**This file is your implementation memory**. After context compaction:

1. **TodoRead** restores your task list
2. **This file** provides all implementation guidelines
3. **Continue from current in_progress todo**
4. **Follow the same systematic approach**

The implementation workflow remains the same whether started fresh or resumed after compaction:

- One todo at a time
- Pattern-first development
- Quality gates after every unit
- Continue until all todos complete
