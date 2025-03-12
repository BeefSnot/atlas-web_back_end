export default function getStudentIdsSum(studentList) {
  return studentList
    .map((item) => item.id)
    .reduce((total, studentID) => total + studentID, 0);
}
