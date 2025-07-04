const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return 6 when type is SUM and inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 0 when type is SUM and inputs are 0.1 and -0.1', function() {
      expect(calculateNumber('SUM', 0.1, -0.1)).to.equal(0);
    });
  });

  describe('SUBTRACT', function() {
    it('should return -4 when type is SUBTRACT and inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should return 0 when type is SUBTRACT and inputs are 1.4 and 1.4', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 1.4)).to.equal(0);
    });
  });

  describe('DIVIDE', function() {
    it('should return 0.2 when type is DIVIDE and inputs are 1.4 and 4.5', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when type is DIVIDE and second input rounds to 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE and second input is 0.4', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.equal('Error');
    });
  });
});
