describe('Work Schedule Page', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();

    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/work-schedules');
    });
  });

  it('successfully loads', () => {
    cy.get('.title').should('contain', 'Work Schedules');
    cy.get('.filter-group').should('exist');
    cy.get('.work-table').should('exist');
  });

  it('filters work schedules by container boat', () => {
    cy.contains('label', 'Container Boat:').next('select').as('containerBoatSelect');
    cy.get('@containerBoatSelect').select('UK0001');
    cy.get('.work-table tbody').find('tr').its('length').should('be.gt', 0);
    cy.get('.work-table tbody tr').each(($row) => {
      cy.wrap($row).find('.container-boat').should('contain', 'UK0001');
    });
  });

  it('displays correctly on mobile devices', () => {
    cy.viewport('iphone-6');
    cy.get('.filter-group').should('exist');
  }); 
  
});
