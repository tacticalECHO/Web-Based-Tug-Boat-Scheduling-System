describe('New Staff Page Test', () => {
  let captainId;
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();
    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/admin/add-new-staff');
    });
  });

  it('Successfully create a new user', () => {
    cy.get('#username').type('CP000N'); 
    cy.get('#name').type('TestUser'); 
    cy.get('#position').select('Captain');
    cy.get('#confirm').click();
    cy.on('window:alert', (text) => {
      expect(text).to.contains('User created successfully');
    });
    captainId = 'CP000N'
  });

  afterEach(() => {
    if (captainId) {
      cy.request({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/captains-delete/',
        body: {
          ids: [captainId]
        },
        headers: {
          'Content-Type': 'application/json',
        },
      }).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.have.property('message', 'Captains deleted successfully');
      });
    }
  });
});
