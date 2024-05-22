package async

var logCounts map[string]uint64

func Log(id, str string) {

	count, ok := logCounts[id]
	if ok {
		logCounts[id]++
	}

}
