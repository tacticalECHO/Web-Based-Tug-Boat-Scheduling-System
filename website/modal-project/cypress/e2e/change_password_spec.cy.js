describe('Change Password Test', () => {
  it('Successful password change', () => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();

    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/settings');
      cy.visit('http://127.0.0.1:8000/#/settings/change-password');
    });

    cy.get('#password').type('newpassword1234');
    cy.get('#passwordReEntered').type('newpassword1234');
    cy.get('#save').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/#/');
  });


  it('Restore Password', () => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('newpassword1234')
    cy.get('.btn').click();

    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/settings');
      cy.visit('http://127.0.0.1:8000/#/settings/change-password');
    });

    cy.get('#password').type('dqr12345');
    cy.get('#passwordReEntered').type('dqr12345');
    cy.get('#save').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/#/');
  });

  it('Error is displayed when the passwords entered twice do not match', () => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();

    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/settings');
      cy.visit('http://127.0.0.1:8000/#/settings/change-password');
    });

    cy.get('#password').type('newpassword123');
    cy.get('#passwordReEntered').type('wrongpassword123');
    cy.get('#save').click();
    cy.get('#passwordReEntered').should('have.css', 'border', '0.8px solid rgb(255, 0, 0)');
  });

  
});
