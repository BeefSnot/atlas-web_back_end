const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const { expect } = require('chai');

describe('sendPaymentRequestToApi', function() {
  it('should stub Utils.calculateNumber and verify console.log', function() {
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    
    const consoleSpy = sinon.spy(console, 'log');
    
    sendPaymentRequestToApi(100, 20);
    
    sinon.assert.calledWith(calculateNumberStub, 'SUM', 100, 20);
    sinon.assert.calledOnce(calculateNumberStub);
    
    sinon.assert.calledWith(consoleSpy, 'The total is: 10');
    sinon.assert.calledOnce(consoleSpy);
    
    calculateNumberStub.restore();
    consoleSpy.restore();
  });
});
