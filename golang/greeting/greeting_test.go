package greeting

import (
	"testing"
	"regexp"
)

func TestHelloWithName(t *testing.T) {
	name := "shaakaal"
	want := regexp.MustCompile(`\b`+name+`\b`)
	msg, err := Hello("shaakaal")
	if !want.MatchString(msg) || err != nil {
		t.Fatalf(`Hello("shaakaal") = %q, %v, want match for %#q, nil`, msg, err, want)
	}
}

func TestHelloWithoutName(t *testing.T) {
	msg, err := Hello("")
	if msg != "" || err == nil {
		t.Fatalf(`Hello("") = %q, %v, want "", error`, msg, err)
	}
}