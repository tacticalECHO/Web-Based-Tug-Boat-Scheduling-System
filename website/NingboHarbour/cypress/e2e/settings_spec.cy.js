describe('Settings Page Tests', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();

    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/settings');
    });
  });

  it('Displays the current username and password placeholder', () => {
      cy.get('#username').should('have.attr', 'placeholder', 'scyqd1');
      cy.get('#password').should('have.attr', 'placeholder', '******');
  });

  it('Navigates to change password page on clicking the change password button', () => {
      cy.get('.change-pwd').click();
      cy.url().should('include', '/#/settings/change-password');
  });

  it('Logs out the user and redirects to login page on clicking the logout button', () => {
      cy.get('.btn-light').click();
      cy.url().should('eq', 'http://127.0.0.1:8000/#/');
  });
});
