package async

import "fmt"

type logPersen struct {
	count, max int
}

var logPersents map[string]logPersen

func LogPresent(id, str string) {

	count, ok := logCounts[id]
	if ok {
		logCounts[id]++
	} else {
		logCounts[id] = 0
	}

	fmt.Println(count, " =>")

}
