export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw TypeError('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(x) {
    if (typeof x === 'string') {
      this._code = x;
    }
  }

  get name() {
    return this._name;
  }

  set name(y) {
    if (typeof y === 'string') {
      this._name = y;
    }
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
