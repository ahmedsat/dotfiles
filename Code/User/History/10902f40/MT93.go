package async

import "fmt"

type logPersen struct {
	count, max uint
}

func LogPresentSetMax(id string, max uint) {
	_, ok := logPersents[id]
	if ok {
		logPersents[id].max = max
	} else {
		logPersents[id] = &logPersen{max: max}
	}
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
