export default function getListStudentIds(studentList) {
    if (!Array.isArray(studentList)) {
      const emptylist = [];
      return emptylist;
    }
  
    const newArray = studentList.map((item) => item.id);
  
    return newArray;
  }
  