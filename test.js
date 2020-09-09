
function combination(n,r){
  let num = factorial(n);
  let de = factorial(r) * factorial(n-r)
  let result = num / de;
  console.log(result);
}

function factorial(target) {
  let result = 1;
  for(i = 0; i < target; i++){
    let num = i + 1;
    result = result * num;
  }
  return result;
}

// 引数に組み合わせを入れる
// 最初が総数、次が求めたいペア
console.log("引数を入れてください、総数:ペア");
combination(5,2);
