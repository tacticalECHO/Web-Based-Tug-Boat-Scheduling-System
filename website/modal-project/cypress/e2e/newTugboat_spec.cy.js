describe('New TugBoat Page Test', () => {
  let tugboatId;
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();
    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/tugboat-list/add-new-tugboat');
    });
  });

  it('Successfully add a tugboat', () => {
    cy.get('input#tugboatId').type('NB000N');
    cy.get('select').select('CP000N : TestUser');
    cy.get('input#startTime').type('08:00');
    cy.get('input#endTime').type('16:00');
    cy.get('button#confirm').click();
    cy.on('window:alert', (str) => {
      expect(str).to.equal('New Tug Boat Added Successfully');
    });
    tugboatId = 'NB000N'
  });

  afterEach(() => {
    if (tugboatId) {
      cy.request({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/tugboat-delete/',
        body: {
          ids: [tugboatId]
        },
        headers: {
          'Content-Type': 'application/json',
        },
      }).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.have.property('message', 'Tugboats deleted successfully');
      });
    }
  });
});
