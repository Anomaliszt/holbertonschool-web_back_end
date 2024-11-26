// Update the value of the key in the map to 100 if the original value is 1

const updateUniqueItems = (map) => {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100);
    }
  }

  return map;
};

export default updateUniqueItems;
