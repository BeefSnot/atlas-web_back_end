export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const updatedStudentList = studentList.map((item) => {
    const newGrade = newGrades.find((grade) => grade.studentId === item.id);
    const grade = newGrade ? newGrade.grade : 'N/A';
    return { ...item, grade };
  });

  const sortedStudentList = updatedStudentList.filter((item) => item.location === city);

  return sortedStudentList;
}
