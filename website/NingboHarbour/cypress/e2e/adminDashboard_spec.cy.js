/** Cypress Test created by Team 10, ©2024  */
describe('Administrator Dashboard Page Tests', () => {
  before(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();
    cy.get('#new-staff').click()
    cy.get('#username').type('CP000D'); 
    cy.get('#name').type('TestCaptain'); 
    cy.get('#position').select('Captain');
    cy.get('#confirm').click();
  })

  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();
  });

  it('Load page successfully', () => {
    cy.url().should('include', '/admin')
  })

  it('Title bar is shown', () => {
    cy.contains('h2', 'Your Dashboard').should('exist');
  });

  it('Captaion visible', () => {
    cy.contains('div', 'Captain').should('exist');

    cy.window().then(win => {
      win.waiting = () => false;
    });

    cy.get('.table-container').should('be.visible');
  });

  it('Scheduler visible', () => {
    cy.contains('div', 'Scheduler').should('exist');

    cy.window().then(win => {
      win.waiting = () => false;
    });

    cy.get('.table-container').should('be.visible');
  });

  it('Button new and delete is visible', () => {
    cy.contains('button', 'New').should('exist')
    cy.contains('button', 'Delete').should('exist')
  })

  it('Delete staff successfully', () => {
    cy.get('#checkboxCP000D').check()
    cy.get('#delete').click()

    cy.on('window:confirm', (str) => {
      expect(str).to.equal('Confirm to delete?')
      return true
    })

    cy.on('window:alert', (str) => {
      expect(str).to.equal('Deleted successfully')
    })

    cy.get('#checkboxCP000D').should('not.exist')
  })

  it('Click new button redirect to New Staff page', () => {
    cy.get('#new-staff').click()
    cy.url().should('include', '/#/admin/add-new-staff')
  })
})
