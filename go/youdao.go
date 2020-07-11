package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
	"time"
)

// go build -o bin/youdao.exe youdao.go
// 去除 Windows 有道云笔记主界面广告，必须以管理员权限运行
func main() {
	fmt.Println("GO")
	path := "C:/Program Files (x86)/Youdao/YoudaoNote/theme/build.xml"
	xml, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}
	str := strings.Replace(strings.Replace(string(xml), "161",
		"0", -1), "250,160", "0,0", -1)
	f, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		panic(err)
	}
	_, err = f.WriteString(str)
	if err != nil {
		panic(err)
	}
	fmt.Println("OK")
	time.Sleep(1 * time.Second)
}
