// new_task_spec.js
describe('New Task Page Test', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('SC0001')
    cy.get('input[type=password]').type('12345678')
    cy.get('.btn').click();
    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/settings');
      cy.visit('http://127.0.0.1:8000/#/add-new-task'); 
    });
  });
  it('Successfully submit a new task', () => {
    const alertStub = cy.stub();
    cy.on('window:alert', alertStub);
    cy.get('input[placeholder="Input the ID of Container Boat"]').type('CB123');
    cy.get('input[placeholder="Input the Country"]').type('China');
    cy.get('input[placeholder="Input Tonnage of Ship"]').type('5000');
    cy.get('input[placeholder="Input Number of Tugboats Needed"]').type('2');
    cy.get('input[type="datetime-local"]').type('2022-05-30T08:30');
    cy.get('select').eq(0).select('INBOUND');
    cy.get('select').eq(1).select('1');
    cy.get('input[type="submit"]').click().then(() => {
      expect(alertStub).to.be.calledOnce;
      expect(alertStub).to.be.calledWith('Added successfully');
    });
  });
});
