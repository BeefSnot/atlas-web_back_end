export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string.');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number.');
    }
    if (!Array.isArray(students)) {
      throw new TypeError('Students must be an array.');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(updatedname) {
    if (typeof updatedname === 'string') {
      this._name = updatedname;
    } else {
      throw new TypeError('New name must be a string');
    }
  }

  set length(updatedlength) {
    if (typeof updatedlength === 'number') {
      this._length = updatedlength;
    } else {
      throw new TypeError('New length must be a number');
    }
  }

  set students(updatedstudents) {
    if (Array.isArray(updatedstudents)) {
      this._students = updatedstudents;
    } else {
      throw new TypeError('New students must be an array');
    }
  }
}
