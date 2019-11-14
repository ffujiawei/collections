/*
	监听事件与邮件提醒
*/

package main

import (
	"fmt"
	"net/http"
	"net/smtp"
	"strings"
	"time"
)

// 一个表示运行中的动画
func spinner(d time.Duration) {
	for {
		for _, r := range `-\|/` {
			fmt.Printf("\r%c", r)
			time.Sleep(d)
		}
	}
}

func monitor() {
	c := &http.Client{}
	target := "http://xjqy.telefen.com/starlevel/yaduo/Commodity/Detail?commodityId=222432"
	r, _ := http.NewRequest("GET", target, nil)
	r.Header.Add("User-Agent", "Mozilla/5.0 (iPhone; CPU iPhone "+
		"OS 11_3_1 like Mac OS X) AppleWebKit/601.4.4 (KHTML, like Gecko) "+
		"Version/11.0 Mobile/15E302 Safari/601.4")
	resp, _ := c.Do(r)
	fmt.Println("Listening.......")
	go spinner(100)
	for resp.Request.URL.String() != target {
		time.Sleep(3 * time.Minute)
		resp, _ = c.Do(r)
	}
}

func SendMail(receiver []string) {
	sender := "1234567890@139.com"
	auth := smtp.PlainAuth("", sender, "123456", "smtp.139.com")
	myself := "Karl"
	subject := "Remainder"
	body := "Thank you!"
	msg := []byte("To: " + strings.Join(receiver, ",") + "\r\nFrom: " +
		myself + "<" + sender + ">\r\nSubject: " + subject + "\r\n" +
		"Content-Type: text/plain; charset=UTF-8" + "\r\n\r\n" + body)
	_ = smtp.SendMail("smtp.139.com:25", auth, sender, receiver, msg)
}

// go build -o bin/remainder.exe remainder.go
func main() {
	var receiver string
	fmt.Print("Please Input Your Email: ")
	_, _ = fmt.Scanln(&receiver)
	if len(receiver) < 1 {
		// 默认
		receiver = "123456@qq.com"
	}
	monitor()
	SendMail([]string{receiver})
	fmt.Println("\nOK")
}
