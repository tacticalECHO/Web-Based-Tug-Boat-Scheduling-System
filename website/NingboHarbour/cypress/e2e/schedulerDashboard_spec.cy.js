describe('Scheduler Dashboard Page Tests', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('hfyeq2')
    cy.get('input[type=password]').type('hfyeq2')
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
    cy.contains('button', 'Add').should('exist');
  });

  it('Filter function available', () => {
    cy.contains('label', 'Container Boat:').should('exist');
    cy.contains('label', 'Country:').should('exist');
    cy.contains('label', 'Tug Boat:').should('exist');
    cy.contains('label', 'Berth:').should('exist');
    cy.contains('label', 'Work Type').should('exist');
    cy.contains('label', 'Status:').should('exist');
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

  it('filters work schedules and tasks by container boat', () => {
    cy.contains('label', 'Container Boat:').next('select').as('containerBoatSelect');
    cy.get('@containerBoatSelect').select('CN0020');
    cy.get('.table tbody').find('tr').its('length').should('be.gt', 0);
    cy.get('.table tbody tr').each(($row) => {
      cy.wrap($row).find('.container-boat').should('contain', 'CN0020');
    });
  });

  it('filters work schedules and tasks by country', () => {
    cy.contains('label', 'Country:').next('select').as('countrySelect');
    cy.get('@countrySelect').select('China');
    cy.get('.table tbody').find('tr').its('length').should('be.gt', 0);
    cy.get('.table tbody tr').each(($row) => {
      cy.wrap($row).find('.country').should('contain', 'China');
    });
  });  

  it('filters work schedules and tasks by tug boat', () => {
    cy.contains('label', 'Tug Boat:').next('select').as('tugboatSelect');
    cy.get('@tugboatSelect').select('NB002');
    cy.get('.table tbody').find('tr').its('length').should('be.gt', 0);
    cy.get('.table tbody tr').each(($row) => {
      cy.wrap($row).find('.tugboat').should('contain', 'NB002');
    });
  });

  it('filters work schedules and tasks by berth', () => {
    cy.contains('label', 'Berth:').next('select').as('berthSelect');
    cy.get('@berthSelect').select('1');
    cy.get('.table tbody').find('tr').its('length').should('be.gt', 0);
    cy.get('.table tbody tr').each(($row) => {
      cy.wrap($row).find('.berth').should('contain', '1');
    });
  });

  it('filters work schedules and tasks by work type', () => {
    cy.contains('label', 'Work Type:').next('select').as('work-typeSelect');
    cy.get('@work-typeSelect').select('INBOUND');
    cy.get('.table tbody').find('tr').its('length').should('be.gt', 0);
    cy.get('.table tbody tr').each(($row) => {
      cy.wrap($row).find('.work-type').should('contain', 'INBOUND');
    });
  });

  it('filters work schedules and tasks by status', () => {
    cy.contains('label', 'Status:').next('select').as('statusSelect');
    cy.get('@statusSelect').select('Unscheduled');
    cy.get('.table tbody').find('tr').its('length').should('be.gt', 0);
    cy.get('.table tbody tr').each(($row) => {
      cy.wrap($row).find('.status').should('contain', 'Unscheduled');
    });
  });


});
