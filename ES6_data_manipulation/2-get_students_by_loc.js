// return array of objects who are in a specific location

const getStudentsByLocation = (students, city) => {
  const studentsLocation = students.filter(
    (student) => student.location === city,
  );

  return studentsLocation;
};

export default getStudentsByLocation;
