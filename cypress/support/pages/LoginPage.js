class LoginPage {
  elements = {
    usernameInput: () => cy.get("#Username"),
    passwordInput: () => cy.get("#Password"),
    loginButton: () => cy.get('button[type="submit"]'),
    errorMessage: () => cy.get(".validation-summary-errors"),
  };

  navigate() {
    cy.visit("/login");
  }

  login(username, password) {
    this.elements.usernameInput().type(username);
    this.elements.passwordInput().type(password);
    this.elements.loginButton().click();
  }

  getErrorMessage() {
    return this.elements.errorMessage();
  }
}

export default new LoginPage();
