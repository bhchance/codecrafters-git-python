This project is my partial solution to the [CodeCrafters Build Your Own Git course](https://codecrafters.io/). CodeCrafters walks you through some basic theory of how things works, then provides automated tests to prove correctness. So all of the code inside `app` is mine, as they only provide the skeleton code for a Hello World equivalent to prove the project is setup correctly. 

CodeCrafters providing automated testing is why this repo contains no tests, and why this README doesn't have any documentation on how to run the code, as their platform can be a bit finnicky around moving things too much. 

If this was a longer term project, I have a separate `src/` and `tests/` and `iac/` directories. `pytest`, and `ruff` would also be running as github actions, and I'd be using `uv` for dependency management.
