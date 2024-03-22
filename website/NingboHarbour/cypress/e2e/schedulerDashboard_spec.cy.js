describe('Scheduler Dashboard Page Tests', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('scyqd1')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();

    cy.url().should('not.eq', 'http://127.0.0.1:8000/#/').then(() => {
      cy.visit('http://127.0.0.1:8000/#/scheduler');
    });
  });

  it('Your Dashboard is shown', () => {
    cy.contains('h2', 'Your Dashboard').should('exist');
  });

  it('Required function buttons available', () => {
    cy.contains('button', 'Schedule').should('exist');
    cy.contains('button', 'Import Task Data').should('exist');
    cy.contains('button', 'Import Tug Boat Data').should('exist');
    cy.contains('button', 'Download').should('exist');
    cy.contains('button', 'Publish').should('exist');
    cy.contains('button', 'Delete').should('exist');
    cy.contains('button', 'Add +').should('exist');
  });

  it('Filter function available', () => {
    cy.contains('label', 'Container Boat:').should('exist');
    cy.contains('label', 'Country:').should('exist');
    cy.contains('label', 'Tug Boat:').should('exist');
    cy.contains('label', 'Berth:').should('exist');
    cy.contains('label', 'Work Type').should('exist');
    cy.contains('label', 'Status:').should('exist');
  });

  it('Successfully visit apis', () => {
    cy.intercept('GET', '/api/display_schedule_entry/').as('displayScheduleEntry');
    cy.intercept('GET', '/api/display_task/').as('displayTask');
    cy.intercept('GET', '/api/display_berth/').as('displayBerth');
    cy.intercept('GET', '/api/display_container_boat/').as('displayContainerBoat');
    cy.intercept('GET', '/api/display_tugboat/').as('displayTugBoat');
    
    // Perform actions that trigger API requests here...

    // cy.wait('@scheduleEntry').should(({ request }) => {
    //   expect(request.url).to.include('/api/display_schedule_entry/');
    // });

    // cy.wait('@displayTask').should(({ request }) => {
    //   expect(request.url).to.include('/api/display_task/');
    // });
  });

  it('Shows "No Task Available" message when there is no task', () => {
    cy.window().then(win => {
      win.waiting = () => true;
    });
    cy.get('div').contains('No Task Available').should('be.visible');
  });

  it('Shows table when there is task', () => {
    cy.window().then(win => {
      win.waiting = () => false;
    });

    cy.get('.table-container').should('be.visible');
  });

  it('Click add button redirect to New Task page', () => {
      cy.get('#add').click();
      cy.url().should('include', '/#/add-new-task');
  });

});
