export default function getStudentIdsSum(studentList) {
    const studentSum = studentList.map((item) => item.id)
      .reduce((total, studentID) => total + studentID, 0);
  
    return studentSum;
  }
  