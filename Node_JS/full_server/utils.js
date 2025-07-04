import fs from 'fs/promises';

const readDatabase = async (filePath) => {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    
    const fields = {};
    students.forEach((student) => {
      const [firstName, lastName, age, field] = student.split(',');
      if (field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    });
    
    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

export default readDatabase;