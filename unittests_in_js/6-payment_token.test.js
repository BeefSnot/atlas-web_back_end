const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', function() {
  it('should return a resolved promise with the right data when success is true', function(done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.be.an('object');
        expect(response).to.have.property('data', 'Successful response from the API');
        done();
      })
      .catch((error) => {
        done(error);
      });
  });
});
