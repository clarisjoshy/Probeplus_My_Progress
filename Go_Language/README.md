# **Learning Go Language**

## Install Go
sudo apt install golang-go  # For Ubuntu/Debian-based systems

## Go Basics
In this folder, Go basics are explained, including topics such as variables, functions,loops, control structures and data types.

## Running a Go file
for running go file run:- go run <file_name>     eg: api/main.go

## go.mod and go.sum file
The go.mod and go.sum files are essential components of Go modules, a dependency management system introduced in Go.
go.mod defines the module's identity, dependencies, and other metadata.
go.sum ensures the security and integrity of those dependencies by storing checksums.

## Sample APIS using GIN Framework
In this folder,basic CRUD operations are included.Here I have explained it for Book and User CRUD Operations.I also included configuring a mongodb connection for the database.
### For Installing Gin framework
go get -u github.com/gin-gonic/gin      //For installing gin framework

### For Installing Mongodb Driver
go get go.mongodb.org/mongo-driver/mongo   //For mongodb driver