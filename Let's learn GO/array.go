package main
import ("fmt")

func main() {
  // var array_name = [length] type {values}
  var arr1 = [3] int {1,2,3}
  arr2 := [5] int {4,5,6,7,8}
  arr3 := [...] int {46,22,6,7,8}

  fmt.Println(arr1)
  fmt.Println(arr2)
  fmt.Println(arr3)
}
