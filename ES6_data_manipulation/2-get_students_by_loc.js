export default function getStudentsByLocation(studentList, city) {
    const newArray = studentList.filter((item) => item.location === city);
  
    return newArray;
  }
  