// return array of objects who are in a specific location

const getStudentsByLocation = (students, city) => {
  students.filter((student) => student.location === city);
};
export default getStudentsByLocation;
