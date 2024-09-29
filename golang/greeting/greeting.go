package greeting

import (
	"fmt"
	"errors"
	"math/rand"
)

func Hello(name string) (string, error)  {
	if name == "" {
		return "", errors.New("No name provided!")
	}
	msg := fmt.Sprintf(randomMessage(), name)
	return msg, nil
}

func Hellos(names []string) (map[string]string, error)  {
	msgs := make(map[string]string)
	for _, name := range names {
		msg, err := Hello(name)
		if err != nil {
			return nil, err
		}
		msgs[name] = msg
	}
	return msgs, nil
}

func randomMessage() string {
	msgs := []string {
		"Hi, %v. Welcome!",
		"Great to see you %v.",
		"How are you %v?",
	}
	return msgs[rand.Intn(len(msgs))]
}