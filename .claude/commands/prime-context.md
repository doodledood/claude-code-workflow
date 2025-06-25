Read the files mentioned in the user input to prime your context. Additionally, run `git ls-files` to get visibility of all files in the repository. Do not perform any actions, modifications, or analysis beyond reading and listing files.

User input: $ARGUMENTS

Steps:

1. Run `git ls-files` to see all tracked files in the repository
2. Read all files specified in the user input
3. Provide a brief confirmation listing:
   - The files you've read
   - A one-line summary of each file's purpose
   - A summary of the repository structure from git ls-files

Example usage:

```
/prime-context src/services/auth.service.ts src/models/user.model.ts
```

This command is useful for loading relevant context and understanding the repository structure before starting work on a feature or debugging an issue.
