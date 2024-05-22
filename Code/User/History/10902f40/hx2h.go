package async

import "fmt"

type logPersen struct {
	count, max int
}

var logPersents map[string]*logPersen

func LogPresent(id, str string) {

	count, ok := logPersents[id]
	if ok {
		logPersents[id].count++
	} else {
		logPersents[id].count = 0
	}

	fmt.Println(count, " =>")

}
