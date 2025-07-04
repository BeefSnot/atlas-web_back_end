import readDatabase from '../utils.js';

class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const fields = await readDatabase(process.argv[2]);
      let responseText = 'This is the list of our students\n';
      
      const sortedFields = Object.keys(fields).sort((a, b) => 
        a.toLowerCase().localeCompare(b.toLowerCase()));
      
      sortedFields.forEach((field) => {
        responseText += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      });
      
      response.status(200).send(responseText);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    
    try {
      const fields = await readDatabase(process.argv[2]);
      const studentsInMajor = fields[major] || [];
      response.status(200).send(`List: ${studentsInMajor.join(', ')}`);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;