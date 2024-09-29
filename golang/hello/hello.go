package main

import (
	"example/greeting"
	"fmt"
	"log"
)

func main() {
	log.SetPrefix("greeting: ")
	log.SetFlags(0)

	names := []string{"guddu", "shaakaal"};

	msg, err := greeting.Hellos(names)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(msg)
}