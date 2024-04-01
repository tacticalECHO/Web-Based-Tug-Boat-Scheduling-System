describe('Login Test with Different Users', () => {
  const users = [
    { role: 'Admin', username: 'scyqd1', password: 'dqr12345', redirectUrl: '/admin' },
    { role: 'Captain', username: 'CP0001', password: '12345678', redirectUrl: '/captain' },
    { role: 'Scheduler', username: 'SC0001', password: '12345678', redirectUrl: '/scheduler' },
  ];
  beforeEach(() => {
    cy.visit('http://127.0.0.1:8000/#/');
  });

  it('greets with Ningbo Harbour', () => {
    cy.contains('h1', 'Ningbo Harbour')
  })

  it('requires valid username and password', () => {
    cy.get('input[type=text]').type('wronguser')
    cy.get('input[type=password]').type('wrongpassword{enter}')
    cy.get('.btn').click();
    cy.get('.invalid-login').should('be.visible')
    cy.get('input[type=text]').clear()
    cy.get('input[type=password]').clear()
  })
  
  users.forEach(user => {
    it(`successfully logs in and redirects ${user.role}`, () => {
      cy.get('input[type=text]').type(user.username)
      cy.get('input[type=password]').type(`${user.password}{enter}`)
      cy.get('.btn').click();
      cy.url().should('include', user.redirectUrl)
    });
  });
});
