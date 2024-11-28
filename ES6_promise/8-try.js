// return the result of dividing the first parameter by the second

export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  } else {
    return numerator / denominator;
  }
}
