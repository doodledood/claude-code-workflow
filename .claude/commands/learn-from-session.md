# Session Insight Extraction Protocol

## Purpose

Ultrathink on this session to extract and document reusable insights that enhance future development efficiency, accuracy, and collaboration in CLAUDE.md.

## Extraction Process

### 1. Identify High-Value Patterns

Review the session for:

- **Efficiency Gains**: Approaches that eliminated friction or repetitive work
- **Error Prevention**: Strategies that avoided common pitfalls
- **Quality Improvements**: Techniques that enhanced output quality
- **Workflow Optimizations**: Process improvements discovered

### 2. Transform to Principles

Convert specific experiences to generalizable guidelines:

- Remove project-specific details
- Focus on underlying patterns
- Emphasize reproducible approaches
- Highlight decision criteria

### 3. Integration Approach for CLAUDE.md

#### Default: Add as Bullets

Simply append new insights as bullet points to relevant sections:

- Find the most appropriate existing section
- Add new bullet at the end of that section's list
- Keep bullet concise but complete
- Include the "why" when non-obvious

Example additions:

- Under "Testing Guidelines": Use --testFile with --testNamePattern for precise test targeting
- Under "Common Tasks": Run type checker after each file save to catch errors early
- Under "Implementation Best Practices": Check previous unit discoveries before searching codebase

#### Only Restructure When:

- Multiple related bullets create confusion
- Section becomes unwieldy or hard to scan
- Clear subcategories emerge naturally
- Existing structure conflicts with new insight

When restructuring:

- Group related bullets under descriptive subheadings
- Maintain all existing content
- Preserve the easy-to-scan bullet format
- Keep hierarchy shallow (max 3 levels)

## Qualification Criteria

Only document insights that:

- Meaningfully reduce future effort or confusion
- Prevent errors that actually occurred or nearly occurred
- Simplify workflows in noticeable ways
- Apply broadly across different scenarios
- Add genuine value beyond existing documentation

## Writing Style for Bullets

Good bullet format:

- Start with action verb when possible
- Include context trigger if needed
- Keep to one line when feasible
- Add brief explanation only if necessary

Examples:

- Run migrations with STAGE=test for test environment
- Combine --testFile and --testNamePattern to avoid running too many tests
- Search previous unit discoveries first - they often contain the exact pattern needed
- Never proceed to next unit until all verification gates pass - errors cascade exponentially

## Priority Focus Areas

Emphasize insights related to:

- Reducing debugging complexity
- Preventing common mistakes
- Accelerating pattern discovery
- Improving test reliability
- Streamlining verification
- Enhancing collaboration clarity

## Additional Context

$ARGUMENTS

Transform session-specific learnings into permanent efficiency gains for all future work.
