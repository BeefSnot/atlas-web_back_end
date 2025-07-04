const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const url = 'http://localhost:7865';

  it('should return status code 200', (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct result', (done) => {
    request.get(url, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should have the correct content type', (done) => {
    request.get(url, (error, response, body) => {
      expect(response.headers['content-type']).to.include('text/html');
      done();
    });
  });
});

describe('Cart page', () => {
  const baseUrl = 'http://localhost:7865';

  it('should return status code 200 when id is a number', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct result when id is a number', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 status code when id is not a number', (done) => {
    request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('should return 404 status code when id contains both numbers and letters', (done) => {
    request.get(`${baseUrl}/cart/12abc`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Available payments endpoint', () => {
  const url = 'http://localhost:7865/available_payments';

  it('should return status code 200', (done) => {
    request.get(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct payment methods object', (done) => {
    request.get(url, (error, response, body) => {
      const expectedPaymentMethods = {
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      };
      const parsedBody = JSON.parse(body);
      
      expect(parsedBody).to.deep.equal(expectedPaymentMethods);
      done();
    });
  });
});

describe('Login endpoint', () => {
  const url = 'http://localhost:7865/login';

  it('should return status code 200', (done) => {
    const options = {
      url: url,
      method: 'POST',
      json: { userName: 'Betty' },
      headers: { 'Content-Type': 'application/json' }
    };

    request(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return Welcome message with the username', (done) => {
    const options = {
      url: url,
      method: 'POST',
      json: { userName: 'Betty' },
      headers: { 'Content-Type': 'application/json' }
    };

    request(options, (error, response, body) => {
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });

  it('should handle different usernames', (done) => {
    const options = {
      url: url,
      method: 'POST',
      json: { userName: 'Thomas' },
      headers: { 'Content-Type': 'application/json' }
    };

    request(options, (error, response, body) => {
      expect(body).to.equal('Welcome Thomas');
      done();
    });
  });
});
