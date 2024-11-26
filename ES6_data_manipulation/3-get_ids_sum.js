// return the sum of all the student ids

const getStudentIdsSum = (students) => students.reduce((sum, student) => sum + student.id, 0);

export default getStudentIdsSum;
