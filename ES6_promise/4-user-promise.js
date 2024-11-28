// return a promise that resolves with an object of user data

function signUpUser(firstName, lastName) {
  return Promise.resolve(
    {
      firstName,
      lastName,
    },
  );
}

export default signUpUser;
