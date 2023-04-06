function productArray(arr) {
    let product = [];
    let n = arr.length;
    let sum = 0;
  
    for (let i = 0; i < n; i++) {
      sum += arr[i];
    }
  // jadi rumusnya jumlah array di kurang dengan isi array dan di bagi dengan panjang array di kurang 1
    for (let i = 0; i < n; i++) {
      product.push((sum - arr[i]) / (n - 1));
    }
  
    return product;
  }
  console.log(productArray([12,20])); 
  console.log(productArray([12,9,6,3])); 
  console.log(productArray([2,4,6])); 
  