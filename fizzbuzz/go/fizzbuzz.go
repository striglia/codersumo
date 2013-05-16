package main

import "fmt"

func main() {
	for n := 1; n <= 100; n++ {
		s := ""
		if n % 3 == 0 {
			s = s + "fizz"
		}
		if n % 5 == 0 {
			s += "buzz"
		}
		if s == "" {
			fmt.Printf("%d\n", n)
		} else {
			fmt.Printf("%s\n", s)
		}
	}
}
