describe('Tug Boat List Page', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();
    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/tugboat-list');
    });
  });

  it('successfully loads', () => {
    cy.get('#TugBoatList').should('be.visible');
  });

  it('allows users to search for tugboats', () => {
    cy.get('#search').type('NB001');
    cy.get('.table-container').should('contain', 'NB001');
  });
  

  it('filters tugboats by status', () => {
    cy.get('input[type="radio"]').check('Busy', { force: true });
    cy.get('.table-container').should('contain', 'NB001');
  });
  
});
