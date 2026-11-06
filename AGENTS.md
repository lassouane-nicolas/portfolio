
# AI Development Guidelines

## Project context

- Project: minimalist developer portfolio built with Django and Wagtail CMS.
- Goal: deliver a functional MVP for the CMS certification on November 19, 2026.
- Prioritize certification requirements, maintainability, and simplicity.
- Use native Django and Wagtail features whenever appropriate.

## Communication and learning

- Explain decisions and technical concepts in French.
- Use English for code identifiers, comments, and docstrings.
- Write public-facing website content in French.
- Work incrementally: propose one actionable step at a time and wait for confirmation.
- Explain unfamiliar concepts, especially CSS properties, their effects, and how to verify them.
- Favor explicit, readable code over clever abstractions.
- Write comments only when they clarify intent or non-obvious decisions.

## Development rules

- Inspect relevant files and existing conventions before suggesting changes.
- Keep modifications small and within the current roadmap task.
- Explain potential impacts, especially database migrations.
- Request approval before deleting files, making destructive migrations, or restructuring existing code.
- Prefer semantic HTML, accessible interfaces, responsive design, and server-side validation.
- Never expose secrets, personal data, or environment files.
- Do not introduce dependencies or features without a demonstrated need.

## Testing and Git

- Run targeted checks and `python manage.py check` when relevant.
- Never claim a test passed without observing its result.
- Review changes before committing.
- Create one coherent commit per completed roadmap task, after testing and documentation.
- Never push, rewrite Git history, or perform destructive operations without explicit approval.

## AI assistant boundaries

- Do not assume access to local files, external tools, or project instructions.
- State clearly when information or access is unavailable.
- Do not assume every AI tool automatically reads this file.
- Keep the developer responsible for understanding, validating, and approving changes.
