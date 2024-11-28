// return a rejected promise with the error message: `${filename} cannot be processed`

export default function uploadPhoto(filename) {
  return Promise.reject(
    new Error(`${filename} cannot be processed`),
  );
}
