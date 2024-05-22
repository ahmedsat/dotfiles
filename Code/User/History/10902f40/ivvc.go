package async

import (
	"fmt"
)

type logPersen struct {
	count, max uint
}

var logPersents map[string]*logPersen

func init() {
	logPersents = map[string]*logPersen{}
}

func LogPresentSetMax(id string, max uint) {
	_, ok := logPersents[id]
	if ok {
		logPersents[id].max = max
	} else {
		logPersents[id] = &logPersen{max: max}
	}
}

func LogPresent(id, str string) {

	lp, ok := logPersents[id]
	if ok {
		logPersents[id].count++
	} else {
		logPersents[id] = &logPersen{}
	}

	fmt.Printf("\r %.8f%%\t\t\t\t\t\t\t", float32(lp.count)/float32(lp.max))

}
