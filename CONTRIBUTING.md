# Contributing to OpenAI-ELI5-Wiki

We appreciate your interest in contributing to OpenAI-ELI5-Wiki! This document provides guidelines to ensure smooth collaboration and help you get started with your contributions.

## Code of Conduct

Please ensure that your interactions with other contributors are respectful and inclusive.

## Getting Started

1. Fork the repository to your GitHub account.
2. Clone the forked repository to your local machine.
git clone https://github.com/your-username/OpenAI-ELI5-Wiki.git
3. Create a new branch for your changes:
```
git checkout -b your-branch-name
```

## Ways to Contribute

- Identify and fix hallucinations via suggesting updates to existing explanations
- Suggest new concepts to be added to the wiki

### Update an Existing Explanation

1. Locate the markdown file in the `content` directory corresponding to the explanation you want to update.
2. Modify the content to improve the explanation or fix inaccuracies/ hallucinations.
3. Commit your changes and push them to your fork.
4. Open a pull request with a detailed description of the changes made.
5. An accepted PR will update Hallucinations.json

### Hallucinations.json

1. Our core contributors will use Github Actions and manual updates to keep this file up-to-date
2. It will contain: ELI5-Title, Open-AI Response, and Corrected Response.

### Suggest New Concepts

1. Create a new issue using the "New Concept Suggestion" template to propose a new concept or list of concepts for for the ELI5 wiki.

## Pull Request Process

1. Ensure your changes are made in a dedicated branch (not the `main` branch).
2. Open a pull request from your branch to the `main` branch of the original repository.
3. Provide a detailed description of your changes and the rationale behind them.
4. One or more maintainers will review your pull request. They may request changes or clarifications before approving the PR.
5. Once approved, your pull request will be merged, and your changes will be incorporated into the project.

## GitHub Actions

This project will use GitHub Actions to automate certain workflows, such as validating pull requests and updating the known hallucinations.json file. Make sure your changes comply with the workflows set up in the `.github/workflows` directory.

THIS WILL BE ADDED IF I CAN NOT HANDLE UPDATING THE FILE MANUALLY

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

Thank you for your interest in contributing to OpenAI-ELI5-Wiki, and we look forward to collaborating with you!
