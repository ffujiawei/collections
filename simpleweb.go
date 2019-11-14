package main

import (
	"fmt"
	"net/http"
)

// go build -o bin/simpleweb.exe simpleweb.go
// 一个最简单的文件服务器
func main() {
	serveMux := http.NewServeMux()
	fileServer := http.FileServer(http.Dir("www"))
	serveMux.Handle("/", fileServer)
	server := &http.Server{
		Addr:    "0.0.0.0:8080",
		Handler: serveMux,
	}
	fmt.Println("服务器已启动，请访问 http://127.0.0.1:8080 " +
		"浏览你的网站\nCtrl+C 终止服务器")
	_ = server.ListenAndServe()
}
