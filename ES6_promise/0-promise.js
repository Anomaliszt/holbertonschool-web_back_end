// return a promise

function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const success = true;
    if (success) {
      resolve();
    } else {
      reject();
    }
  });
}

export default getResponseFromAPI;
