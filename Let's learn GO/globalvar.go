package main
import ("fmt")

var a int
var b int = 2
var c = 3 //inferred

func main() {
  a = 1
  h:= 22 //inferred
  fmt.Println(a)
  fmt.Println(b)
  fmt.Println(c)
  fmt.Println(h)
}
