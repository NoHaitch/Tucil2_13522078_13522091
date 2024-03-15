package main

import "fmt"

func main() {
  // for
  c := 3
  for i := 0; i < c; i++ {
    fmt.Print(i, " ")
  }
  fmt.Println()
  
  // replace while with for
  for c > 0 {
    fmt.Print(c, " ")
    c--
  }
  fmt.Println()

  // for with range
  d := []int{0, 1, 1, 2, 3, 5, 8}
  for _, i := range d {
    fmt.Print(i, " ")
  }
  fmt.Println()
}