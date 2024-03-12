# SEMANTIC COMMITS CHEATSHEET

Base of a commit message:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Type: The main topic of commit

- `feat`: new feature
- `fix`: bug fix for the user
- `perf`: performance improvements
- `docs`: new or changes to the documentation
- `style`: formatting changes, missing semicolons, etc.
- `refactor`: refactoring production code, e.g. renaming a variable.
- `test`: adding missing tests, refactoring tests
- `build`: updating build configuration or other changes irrelevant to the user
- `chore`: if not contained by all the type above and no production code changed

### Scope: What is the scope of the commit (category, features, etc)
- init
- runner
- watcher
- config
- web-server
- proxy
- etc.

## Reference
- https://www.conventionalcommits.org/en/v1.0.0/
- https://medium.com/@callmeryan/semantic-commit-messages-bcd60f75de1f
- https://karma-runner.github.io/6.3/dev/git-commit-msg.html
- https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716 