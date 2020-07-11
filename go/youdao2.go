package main

import (
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	p := "C:/Program Files (x86)/Youdao/YoudaoNote/theme/build.xml"
	c, err := ioutil.ReadFile(p)
	if err != nil {
		panic(err)
	}
	f, err := os.OpenFile(p, os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		panic(err)
	}
	replacer := strings.NewReplacer("161", "0", "250,160", "0,0")
	_, err = replacer.WriteString(f, string(c))
	if err != nil {
		panic(err)
	}
}
