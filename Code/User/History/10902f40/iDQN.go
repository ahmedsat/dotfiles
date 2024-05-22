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

	lp, ok := logPersents[id]
	if ok {
		logPersents[id].count++
	} else {
		logPersents[id] = &logPersen{}
	}

	fmt.Printf("\033[u\033[K %d => %s \t\t %f%\n", lp.count, str, float32(lp.count)/float32(lp.max))

}
