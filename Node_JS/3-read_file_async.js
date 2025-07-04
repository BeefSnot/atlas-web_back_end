const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    
    console.log(`Number of students: ${students.length}`);
    
    const fields = {};
    students.forEach((student) => {
      const [firstName, lastName, age, field] = student.split(',');
      if (!fields[field]) {
        fields[field] = { count: 0, names: [] };
      }
      fields[field].count += 1;
      fields[field].names.push(firstName);
    });
    
    Object.keys(fields).forEach((field) => {
      const { count, names } = fields[field];
      console.log(`Number of students in ${field}: ${count}. List: ${names.join(', ')}`);
    });
    
    return { students, fields };
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
