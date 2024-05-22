package async

import (
	"fmt"
	"os"

	"golang.org/x/sys/unix"
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

	ws, err := unix.IoctlGetWinsize(int(os.Stdout.Fd()), unix.TIOCGWINSZ)
	if err != nil {
		return nil, os.NewSyscallError("GetWinsize", err)
	}

	fmt.Print("\r", float32(lp.count)/float32(lp.max), "%")

}
