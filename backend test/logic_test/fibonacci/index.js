function nearestFibonacci(arr) {
    function isFibonacci(n) {
      if (n === 0 || n === 1) {
        return true;
      }
      let a = 0, b = 1;
      while (b < n) {
        const temp = a + b;
        a = b;
        b = temp;
      }
      return b === n;
    }
  
    const total = arr.reduce((acc, val) => acc + val, 0);
  
    let a = 0, b = 1;
    while (b < total) {
      const temp = a + b;
      a = b;
      b = temp;
    }
    if (Math.abs(total - a) < Math.abs(total - b)) {
      return Math.abs(total - a);
    } else {
      return Math.abs(total - b);
    }
  }
  const arr = [15, 1, 3];
  const result = nearestFibonacci(arr);
  console.log(result);
  
  