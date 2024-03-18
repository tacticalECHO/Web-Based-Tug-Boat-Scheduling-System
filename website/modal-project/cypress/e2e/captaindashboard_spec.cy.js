describe('Captain Dashboard Page Tests', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/')
    cy.get('input[type=text]').type('CP0001')
    cy.get('input[type=password]').type('dqr12345')
    cy.get('.btn').click();
  });

  it('successfully loads', () => {
    cy.url().should('include', '/captain')
  })

  it('sidebar is visible', () => {
    cy.get('.sidebar').should('be.visible')
  })

  it('download button directs download', () => {
    cy.window().then((win) => {
      win.localStorage.setItem('username', 'CP0001')
    })

    cy.intercept('POST', '/api/download-captain', {
      statusCode: 200,
      body: {
        message: 'Download initiated'
      }
    }).as('downloadRequest')
    cy.get('#download').click()
    cy.wait('@downloadRequest').its('request.body').should('deep.equal', {
      captainId: 'CP0001'
    })
    cy.on('window:alert', (str) => {
      expect(str).to.equal(`Successfully Download!`)
    })
  })
})
