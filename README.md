# Cypress Test Automation Framework for CDMS Demo

This repository contains a Cypress-based test automation framework for the CDMS Demo application (https://demo.cdms.co.ke). It provides a structured approach to writing, organizing, and running automated tests for the CDMS Demo web application.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Configuration](#configuration)
5. [Writing Tests](#writing-tests)
6. [Running Tests](#running-tests)
7. [Continuous Integration](#continuous-integration)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)

## Prerequisites

Before setting up the framework, ensure you have the following installed:

- Node.js (v14 or later)
- npm (usually comes with Node.js)
- Git

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/mobarasa/cdms_cypress.git
   ```

2. Navigate to the project directory:

   ```
   cd cdms_cypress
   ```

3. Install the dependencies:
   ```
   npm install
   ```

## Project Structure

```
cdms_cypress/
├── cypress/
│   ├── e2e/
│   │   ├── login/
│   │   ├── inventory/
│   │   ├── orders/
│   │   └── ...
│   ├── fixtures/
│   ├── support/
│   │   ├── commands.js
│   │   └── e2e.js
│   └── plugins/
├── .gitignore
├── cypress.config.js
├── package.json
└── README.md
```

## Configuration

The main configuration file for Cypress is `cypress.config.js`. Here you can set up environment variables, configure viewport size, and other Cypress options.

Example configuration:

```javascript
const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "https://demo.cdms.co.ke",
    viewportWidth: 1280,
    viewportHeight: 720,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
```

## Writing Tests

Tests are located in the `cypress/e2e` directory. Organize your tests into subdirectories based on features or modules of the CDMS Demo application.

Example test file (`cypress/e2e/login/login.spec.js`):

```javascript
describe("Login Functionality", () => {
  beforeEach(() => {
    cy.visit("/login");
  });

  it("should login with valid credentials", () => {
    cy.get("#username").type("validuser");
    cy.get("#password").type("validpassword");
    cy.get("#login-button").click();
    cy.url().should("include", "/dashboard");
  });

  it("should show error with invalid credentials", () => {
    cy.get("#username").type("invaliduser");
    cy.get("#password").type("invalidpassword");
    cy.get("#login-button").click();
    cy.get(".error-message").should("be.visible");
  });
});
```

## Running Tests

To run the tests, use the following npm scripts:

- Run all tests headlessly: `npm run test`
- Open Cypress Test Runner: `npm run cypress:open`
- Run tests in a specific browser: `npm run test:chrome` or `npm run test:firefox`

Add these scripts to your `package.json`:

```json
"scripts": {
  "test": "cypress run",
  "cypress:open": "cypress open",
  "test:chrome": "cypress run --browser chrome",
  "test:firefox": "cypress run --browser firefox"
}
```

## Continuous Integration

This framework can be integrated with various CI/CD platforms. Here's an example of how to set it up with GitHub Actions:

Create a file `.github/workflows/cypress.yml`:

```yaml
name: Cypress Tests

on: [push]

jobs:
  cypress-run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Cypress run
        uses: cypress-io/github-action@v5
        with:
          build: npm run build
          start: npm start
```

## Best Practices

1. Use Page Object Model (POM) for better maintainability.
2. Keep tests independent and atomic.
3. Use meaningful descriptions for your test cases.
4. Utilize Cypress commands and custom commands for common actions.
5. Use fixtures for test data.
6. Implement proper error handling and logging.

## Troubleshooting

If you encounter issues:

1. Ensure all dependencies are correctly installed.
2. Check if the CDMS Demo application is accessible.
3. Verify your Cypress configuration.
4. Check the Cypress documentation for known issues.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

For more information on Cypress, visit the [official Cypress documentation](https://docs.cypress.io/).
