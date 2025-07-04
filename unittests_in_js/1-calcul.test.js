const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('should return 6 when type is SUM and inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should return 0 when type is SUM and inputs are 0.1 and -0.1', function() {
      assert.strictEqual(calculateNumber('SUM', 0.1, -0.1), 0);
    });
  });

  describe('SUBTRACT', function() {
    it('should return -4 when type is SUBTRACT and inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should return 0 when type is SUBTRACT and inputs are 1.4 and 1.4', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 1.4), 0);
    });
  });

  describe('DIVIDE', function() {
    it('should return 0.2 when type is DIVIDE and inputs are 1.4 and 4.5', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return "Error" when type is DIVIDE and second input rounds to 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('should return "Error" when type is DIVIDE and second input is 0.4', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
    });
  });
});
