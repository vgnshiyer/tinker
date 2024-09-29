package main

import (
	"example/greeting"
	"fmt"
	"log"
)

func main() {
	log.SetPrefix("greeting: ")
	log.SetFlags(0)

	msg, err := greeting.Hello("Vignesh")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(msg)
}