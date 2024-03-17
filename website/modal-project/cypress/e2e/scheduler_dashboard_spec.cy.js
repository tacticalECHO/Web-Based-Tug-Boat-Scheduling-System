describe('Settings Page Tests', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();

    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/scheduler');
    });
  });

});
