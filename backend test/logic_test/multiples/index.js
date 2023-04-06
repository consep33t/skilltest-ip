function solution(n) {
    /*
    mengembalikan hasil penjumlahan semua bilangan yang merupakan kelipatan 3 atau 5 dan kurang dari n, serta bilangan-bilangan tersebut
    */
    let sum = 0;
    let multiples = [];
    for (let i = 0; i < n; i++) {
      if (i % 3 === 0 || i % 5 === 0) {
        multiples.push(i);
        sum += i;
      }
    }
    return `${sum} = ${multiples.join(' + ')}`;
  }
console.log(solution(10))
console.log(solution(20))  