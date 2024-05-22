package async

import "fmt"

var logPersents map[string]uint64

func LogPresent(id, str string) {

	count, ok := logCounts[id]
	if ok {
		logCounts[id]++
	} else {
		logCounts[id] = 0
	}

	fmt.Println(count, " =>")

}
