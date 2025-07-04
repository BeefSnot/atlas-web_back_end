const express = require('express');
const fs = require('fs').promises;

const app = express();
const port = 1245;
const databasePath = process.argv[2];

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    
    let output = `Number of students: ${students.length}\n`;
    
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
      output += `Number of students in ${field}: ${count}. List: ${names.join(', ')}\n`;
    });
    
    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  let responseText = 'This is the list of our students\n';
  
  try {
    const studentsInfo = await countStudents(databasePath);
    res.send(`${responseText}${studentsInfo}`);
  } catch (error) {
    res.send(`${responseText}${error.message}`);
  }
});

app.listen(port);

module.exports = app;
