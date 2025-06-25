# IMPORTANT Guidelines, Context & Instructions

## Projects Overview

...

## Essential Commands

### Quality Gates (Run for EVERY code change)

**Why**: Catching errors immediately prevents compound issues and reduces debugging time later. Small, frequent checks are far easier to fix than accumulated problems.

```bash
# Note: These gates apply to code changes only, not documentation or configuration files

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

## Coding & Testing General Guidelines

### Type Safety Discipline

**Why**: Type safety catches bugs at compile time rather than runtime, preventing production issues and making refactoring safer. Linting enforces coding standards and catches common errors and code smells.

- Never use `any` type.
- Avoid `as unknown as X` patterns; fix the root type issue.
- When testing private methods, prefer testing through public APIs or extracting logic to pure, testable functions.

### Error Handling Discipline

When errors occur:

1. Read the exact error message.
2. Fix the root cause, not the symptom.
3. Run verification immediately to ensure the fix is effective.

### Testing Discipline

- When testing do not use conditional asserts
- Do not write comments unless they are essential to understand the why behind something
- Aim for readability of the code instead of comments

Always complete the implementation and verification for one unit before starting the next.

## Feature Development Workflow

### Planning Phase (When in Plan Mode or explicitly asked to plan)

When user requests a feature:

**Planning Principle**: Always aim for the simplest solution that covers the requirements, not necessarily the most elegant or ambitious, unless explicitly requested by the user.

**Why**: Simple solutions are easier to maintain, test, and debug. Complexity should only be added when justified by actual requirements, not anticipated ones.

1. **Create Planning Todos**:

   ```
   "Read PRD.md if exists, otherwise get requirements from user"
   "Read testing docs and other relevant documentation for non-trivial features"
   "Find patterns: Grep for similar services/controllers/entities (2-3 examples max)"
   "Design simple units with what/how/pattern/related/gates"
   "Validate plan compliance: Use Agent tool to verify plan follows CLAUDE.md rules"
   "Present plan via exit_plan_mode for approval"
   "After approval: Create comprehensive implementation TODOs following CLAUDE.md format"
   "Validate TODOs: Use Agent tool to verify all TODOs are self-contained and follow rules"
   ```

2. **Requirements Gathering**:

   - IF PRD.md exists: Read it for requirements and success criteria
   - ELSE: Get requirements from user
   - If unclear after 2 attempts: "Should we create a PRD first with /prd?"

   **Requirements Gathering Goals**:

   - **Primary Goal**: Identify the minimal viable solution that fully satisfies user needs
   - **Key Principle**: Strip complexity, not functionality
   - **Required Actions**:
     - Document what's being excluded and why
     - Confirm stripped requirements still meet user's actual goals
     - If removing features, explicitly ask: "Will removing X still meet your needs?"
   - **Anti-pattern**: Over-simplifying to the point of not solving the user's problem
   - **Success Metric**: User confirms the simplified solution addresses their core need

3. **Documentation Review (REQUIRED for non-trivial features)**:

   For any feature involving code changes, read relevant docs FIRST:

   - **Testing**: `docs/codebase/quality_testing/` - Required for all features with tests
   - **Architecture**: `docs/codebase/architecture/` - For system design decisions
   - **Data**: `docs/codebase/data_domain/` - For features involving models/migrations
   - **Development**: `docs/codebase/development/` - For coding standards and patterns

   Add to planning todos: "Read testing docs and other relevant documentation"

4. **Pattern Finding (Minimal Research)**:

   ```bash
   # Find similar implementations
   grep -r "class .*Service" --include="*.ts"
   grep -r "class .*Controller" --include="*.ts"
   # Look at 2-3 examples, note specific line numbers
   ```

   **Pattern Finding Goals**:

   - **Primary Goal**: Achieve deep understanding of existing patterns, not just locate them
   - **Required Actions**:
     - Use grep to find 2-3 similar implementations
     - Read each pattern file COMPLETELY (not just grep output)
     - Document specific line numbers and implementation approaches
     - Note error handling patterns, testing patterns, and integration patterns
   - **Anti-pattern**: Running grep and moving on without reading the files
   - **Success Metric**: Can explain WHY the pattern works, not just WHAT it does

5. **Unit Design**:

   **Why**: Atomic units can be completed and verified independently, reducing risk and enabling incremental progress. Including tests ensures quality at each step.

   Each unit must be:

   - **Atomic**: One logical piece including implementation AND tests (never separate)
   - **Right-sized**: Not "add import" but not "entire system"
   - **Pattern-based**: References all relevant files and line numbers for the unit
   - **Test-complete**: Every unit MUST include tests - a unit without tests is incomplete

   Unit structure (remember: describe what to do, not show code):

   ```yaml
   What: User CRUD service
   How:
     - Copy auth.service.ts structure
     - Add create, read, update, delete methods
     - Write comprehensive unit tests (REQUIRED - unit incomplete without tests)
     - Handle errors like policy.service.ts:45-89
   Pattern: auth.service.ts
   Related:
     - Types: user.types.ts:12-45 (User, CreateUserDto)
     - Repository: user.repository.ts
     - Module: app.module.ts:34 (add to providers)
     - Tests: auth.service.test.ts (mock patterns)
   Quality Gates:
     - [ ] npx nx run api:tsc
     - [ ] npx nx test api --testFile=user.service.test.ts
     - [ ] npx nx lint api --fix
   ```

   **Unit Design Validation Goals**:

   - **Primary Goal**: Ensure each unit is truly atomic and independently verifiable
   - **Validation Checklist** (before finalizing any unit):
     - Can this unit be completed in one work session?
     - Does it have clear, measurable success criteria?
     - Are all dependencies identified and available?
     - Can it be tested in isolation from other units?
     - Is the scope small enough to maintain focus?
   - **Required Action**: If ANY answer is "no", break the unit down further
   - **Anti-pattern**: Creating units that are too large or have hidden dependencies
   - **Success Metric**: Each unit can be assigned to a different developer and completed independently

6. **Plan Validation (CRITICAL)**:

   Before presenting the plan, validate it using the Agent tool:

   ```
   Agent Prompt: "Read CLAUDE.md thoroughly, then review this plan and verify it follows ALL rules:

   [Insert complete plan here]

   Validate:
   1. Units are atomic with tests included
   2. Each unit has proper structure: What/How/Pattern/Related/Gates
   3. Pattern references include specific line numbers
   4. Units are right-sized (not too small, not too large)
   5. Quality gates are specified for each unit
   6. Implementation follows pattern-first approach

   Provide specific feedback on any violations and suggest improvements."
   ```

   - If Agent finds issues: Fix them before proceeding
   - If Agent approves: Continue to exit_plan_mode
   - This validation ensures plan quality before implementation begins

### Implementation Phase (After plan approval)

1. **Create Comprehensive Implementation Todos**:

   **Your todos are your persistent memory** - they survive any context loss.

   Each todo MUST be self-contained with ALL context needed:

   **Format**:

   ```
   "Unit X.Y: [Task Summary] [ReadingHints] - [Detailed implementation steps with exact patterns, files, line numbers] - Gates: [exact commands]"
   ```

   **Reading Hints (MANDATORY for every TODO)**:

   - `[ReadClaude,SkipDocs]` - Read CLAUDE.md before starting, no docs needed
   - `[ReadClaude,ReadTestDocs]` - Read CLAUDE.md and testing docs before starting
   - `[ReadClaude,ReadArchDocs]` - Read CLAUDE.md and architecture docs before starting
   - `[ReadClaude,ReadArchDocs,ReadTestDocs]` - Read CLAUDE.md and multiple docs before starting
   - `[SkipClaude,SkipDocs]` - ONLY for trivial fixes like missing imports or typos

   **Examples**:

   ```
   "Unit 1.1: Create User CRUD Service [ReadClaude,ReadArchDocs,ReadTestDocs] - Create src/users/user.service.ts copying auth.service.ts:15-89 class structure - Inject UserRepository - Implement: create(dto) with validation, findOne(id) with NotFoundException if not found, findAll() with pagination, update(id, dto) with partial updates, remove(id) with soft delete - Error handling pattern from policy.service.ts:45-89 - Tests: Copy auth.service.test.ts:234-289 structure, mock UserRepository with createMock, test each method success/failure - Gates: Run in parallel: tsc, test --testFile=user.service.test.ts, lint"

   "Unit 1.1b: Fix missing import [SkipClaude,SkipDocs] - Fix TS2304 in user.controller.ts:12 - Add: import { UserDto } from './dto/user.dto' - Gates: Run in parallel: tsc, lint"

   "Unit 2.3: Debug failing auth tests [ReadClaude,SkipDocs] - Fix 5 failing tests in auth.service.test.ts after Guard update - Check: mock setup line 45, Guard expectations, token validation - Reference working pattern: user.service.test.ts:123-145 - Gates: Run in parallel: tsc, test --testFile=auth.service.test.ts, lint"
   ```

   **Todo Creation Success Metrics**:

   - **Primary Goal**: Enable perfect work resumption after any interruption
   - **Success Metric**: Another developer could implement from your todo alone
   - **Required Elements**:
     - Reading Hints (e.g., [MaybeReadClaude,ReadTestDocs])
     - Exact file paths (not just names)
     - Specific line numbers for patterns (not just file references)
     - Gates to run in parallel
     - All context needed for implementation
   - **Anti-pattern**: Todo that requires reading the plan or other todos to understand
   - **Validation Test**: Hide all other todos and the plan - can someone still implement this todo?

2. **TODO Validation (CRITICAL)**:

   After creating all implementation todos, validate them using the Agent tool:

   ```
   Agent Prompt: "Read CLAUDE.md thoroughly, focusing on the TODO creation guidelines. Review these implementation TODOs and verify they follow ALL rules:

   [Insert complete TODO list here]

   Validate each TODO for:
   1. Contains Reading Hints (e.g., [ReadClaude,ReadTestDocs])
   2. Self-contained with ALL context needed for implementation
   3. Includes exact file paths and line numbers for patterns
   4. Specifies all quality gates to run in parallel
   5. Follows the format: 'Unit X.Y: [Summary] [Hints] - [Details] - Gates: [commands]'
   6. Could be implemented by another developer without seeing the plan

   For each non-compliant TODO:
   - Identify what's missing
   - Suggest the corrected version
   - Explain why it matters"
   ```

   - If Agent finds issues: Fix ALL todos before starting implementation
   - Only proceed when Agent confirms TODO compliance
   - This validation prevents context loss and ensures implementation success

3. **Execution Flow Per Unit**:

   ```
   a. Mark ONE todo as in_progress
   b. Follow TODO reading hints EXACTLY:
      - [ReadClaude,...] → ALWAYS read FULL CLAUDE.md file first
      - [SkipClaude,...] → Skip CLAUDE.md ONLY for trivial fixes (eg. imports, typos)
      - After reading: Acknowledge with "I've refreshed my memory of CLAUDE.md and will follow it to the letter"
      - Add system reminder: <system-reminder>I must adhere to CLAUDE.md guidelines very closely.</system-reminder>
   c. Follow documentation reading hints from TODO:
      - ReadArchDocs → Read architecture docs before implementing
      - ReadTestDocs → Read testing docs before writing tests
      - ReadDataDocs → Read data domain docs for database work
      - SkipDocs → No additional docs needed

   **Documentation Reading Requirements**:
   - **Goal**: Ensure implementation follows established patterns and standards
   - **Mandatory Reading Triggers**:
     * First time implementing this type of component in session
     * Any architectural decision (service boundaries, data flow)
     * Test implementation (even if copying patterns)
     * After any quality gate failure related to patterns
   - **Track in Todos**: Document when you last read each doc type
   - **Anti-pattern**: Assuming familiarity from previous sessions

   d. Read pattern files specified in todo
   e. Verify you have identified appropriate patterns for all aspects (structure, error handling, tests)
   f. Implement following patterns exactly
   g. Write/update tests (NEVER skip)
   h. Run gates in parallel (separate tool calls): tsc, test, lint
   i. If gates pass → mark completed → next unit
   j. If blocked → see blocker handling below
   ```

   **Quality Gate Execution Goals**:

   - **Primary Goal**: Verify code correctness before proceeding
   - **Required Actions**:
     - Run all three gates in parallel (separate tool calls)
     - Wait for ALL results before proceeding
     - Read and analyze any failure messages
     - Only mark unit complete when ALL gates pass
   - **Anti-patterns**:
     - Running gates without checking results
     - Marking unit complete with failing gates
     - Running gates sequentially instead of in parallel
   - **Success Metric**: Zero errors, zero test failures, zero lint violations

4. **Blocker Handling (Critical Nuance)**:

   ```
   When blocked on current unit:
   - If can continue within unit: Create todo "Unit X.Yb: Fix [specific issue]" with full context and keep working
   - If totally blocked: Create todo, mark current as pending, move to next unit
   - Examples:
     * Missing type: Create "Unit 1.1b: Add UserDto type [ReadClaude,SkipDocs] - Create in src/types/user.types.ts - Export interface UserDto with id: string, name: string, email: string fields - Export from types/index.ts - Gates: Run in parallel: tsc, lint" and continue
     * Missing dependency: Create "Unit 1.1c: Install @nestjs/swagger [SkipClaude,SkipDocs] - Run npm install @nestjs/swagger - Add to package.json dependencies - Gates: Run in parallel: tsc, lint" and move to next unit
   - Return to ALL blocker todos after main units complete
   ```

   **Blocker Handling Goals**:

   - **Primary Goal**: Maintain forward progress while ensuring completeness
   - **Decision Criteria**:
     - Is this a simple fix with clear solution? → Fix now
     - Is this preventing ALL progress on unit? → Create todo, mark current as pending
     - Can I continue other parts of unit? → Create todo, keep working
   - **Anti-pattern**: Creating blocker todos for convenience rather than necessity
   - **Required**: Document WHY it's blocking and WHAT would unblock it
   - **Success Metric**: Zero pending units at feature completion

### Verification Phase

After all implementation todos complete:

```
□ All units implemented with tests
□ All quality gates passing
□ All blocker todos resolved
□ If PRD.md exists: Verify every requirement addressed
□ If PRD.md exists: Confirm all success criteria met
□ Final gates on entire feature: Run in parallel: tsc, test, lint
```

**Implementation Success Metrics**:

- **Goal**: Ensure feature is truly complete and production-ready
- **Required Criteria**:
  - All units implemented with passing gates
  - Zero "fix" todos remaining
  - Tests cover all meaningful code paths (happy paths, error cases, edge cases)
  - Code follows referenced patterns exactly
  - PRD requirements verified with specific evidence
- **Anti-pattern**: Claiming success with pending work or failing gates
- **Success Declaration**: Only when ALL criteria are met

## Todo-Driven Development

### Why Comprehensive Todos Matter

**Why**: As conversations grow and context windows fill, todos become your external memory, ensuring nothing is forgotten during context switches or compaction.

As context grows, todos become your memory. Create todos for EVERYTHING:

- Each unit from the plan
- Each discovered issue
- Each dependency to add
- Each file to update
- Each test to write

### Todo Patterns

**Planning Phase**:

1. "Read PRD.md if exists, otherwise get requirements from user"
2. "Read testing docs and other relevant documentation for non-trivial features"
3. "Find patterns: grep for similar services/controllers/entities"
4. "Design simple units with what/how/pattern/related/gates"
5. "Validate plan with Agent: Run Agent to verify plan follows all CLAUDE.md rules"
6. "Present plan via exit_plan_mode for approval"
7. "After approval: Create detailed implementation TODOs"
8. "Validate TODOs with Agent: Run Agent to verify all TODOs follow CLAUDE.md format"

**Implementation Phase** (be VERY specific):

- "Unit 1.1: Create user.service.ts [ReadClaude,ReadArchDocs,ReadTestDocs] - Copy auth.service.ts:15-89 pattern - Implement CRUD methods with user.repository.ts - Error handling: policy.service.ts:45-89 - Tests: auth.service.test.ts:234-289 patterns - Gates: Run in parallel: tsc, test --testFile=user.service.test.ts, lint"
- "Unit 1.1b: Add UserNotFoundException [SkipClaude,SkipDocs] - Create in exceptions/user.exceptions.ts - Copy NotFoundException pattern from exceptions/not-found.exception.ts:5-15 - Export from exceptions/index.ts - Gates: Run in parallel: tsc, lint"
- "Unit 1.1c: Register UserService [SkipClaude,SkipDocs] - Add to user.module.ts providers array at line 18 - Gates: Run in parallel: tsc, lint"

**Status Management**:

**Why**: Single focus prevents context switching and ensures quality gates are run before moving on, maintaining code quality throughout.

- Only ONE todo in_progress at a time
- Update status in real-time
- Never leave blocked todos in_progress
- Use specific descriptions that survive compaction

## Intelligent Context Management

### CLAUDE.md Reading Strategy

Since CLAUDE.md auto-loads at session start, re-reading is controlled by TODO hints:

**Always Read FULL File When Reading** - Never partial reads

**Follow TODO Reading Hints**:

- `[ReadClaude,...]` → MUST read FULL CLAUDE.md before starting the unit
- `[SkipClaude,...]` → Can skip CLAUDE.md (only for trivial fixes)
- Default assumption: Read CLAUDE.md for any non-trivial work

**When TODO says ReadClaude**:

- Read the FULL file, not just sections
- Acknowledge after reading: "I've refreshed my memory of CLAUDE.md and will follow it to the letter"
- Add system reminder: <system-reminder>I must adhere to CLAUDE.md guidelines very closely.</system-reminder>
- Then proceed with the unit implementation

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

### Self-Contained Todo Principles

Every todo must answer:

1. **What** exactly to implement/fix
2. **Where** to make changes (exact files/lines)
3. **How** to implement (patterns to copy)
4. **Verification** (exact gate commands)

Bad todo:

```
"Add user service tests"
```

Good todo:

```
"Unit 2.2: Add UserService tests [SkipClaude,ReadTestDocs] - Create user.service.test.ts - Copy test structure from auth.service.test.ts:100-250 - Mock UserRepository with createMock - Test: create() with valid/invalid dto, findOne() found/not found cases, update() partial updates, remove() soft delete - Verify mocks called correctly - Gates: Run in parallel: tsc, test --testFile=user.service.test.ts, lint"
```

Each todo contains everything needed to resume work after any interruption.

## Pattern-First Development

**The Golden Rule**: NEVER write code without a pattern

**Why**: Following existing patterns ensures consistency across the codebase and leverages proven solutions, reducing bugs and onboarding time.

1. **Finding Patterns**:

   ```bash
   # For services
   grep -r "class .*Service" --include="*.ts" | head -5
   # For controllers
   grep -r "@Controller" --include="*.ts" | head -5
   # For specific patterns
   grep -r "Repository<" --include="*.ts"  # Find repository patterns
   ```

2. **Using Patterns**:

   - Read the ENTIRE pattern file first
   - Copy the complete structure
   - Keep the same organization
   - Adapt ONLY the specifics (names, types, business logic)
   - Copy error handling patterns exactly
   - Copy test patterns exactly

3. **Pattern References**:
   Always include line numbers:
   - "Copy error handling from policy.service.ts:45-89"
   - "Follow test structure from auth.service.test.ts:234-289"
   - "Use DTO validation like create-user.dto.ts:12-34"

**Pattern Adherence Verification**:

- **Goal**: Maintain codebase consistency and quality
- **Success Criteria**: Another developer cannot distinguish your code from existing patterns
- **Anti-pattern**: "Following the spirit" of patterns while ignoring their structure

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
